"""
Qo'shimcha bo'limlar: valyuta kurslari, kargo kalkulyatori, "TOP sotuv" mahsulotlar,
B2B shaxsiy kabinet (balans/statistika) va bildirishnomalar (notifikatsiyalar).

MUHIM CHEKLOV (halollik uchun aniq yozilgan):
- `fx-rates` — bu yerdagi raqamlar Markaziy bank (cbu.uz) saytidan QO'LDA olingan
  SNAPSHOT qiymatlar (pastdagi FX_RATES o'zgaruvchisida "updated_at" sanasi bilan
  belgilangan). Ular avtomatik yangilanmaydi. Haqiqiy loyihada bu funksiya cbu.uz
  ning ochiq JSON API'siga serverdan so'rov yuborib, masalan har soatda keshlab
  turishi kerak (bu yerga shunchaki requests.get(...) qo'shish yetarli).
- `notifications` — bazadagi haqiqiy buyurtma/zaxira holatidan hisoblanadi, lekin
  "o'qilgan/o'qilmagan" holati saqlanmaydi (soddalashtirilgan v1). Haqiqiy SMS yoki
  qo'ng'iroq YUBORILMAYDI — buning uchun Eskiz.uz/Play Mobile kabi SMS-shlyuz yoki
  Twilio kabi qo'ng'iroq provayderida akkaunt va API kalit kerak bo'ladi. Pastdagi
  `notify_external()` funksiyasi aynan shu joyga ulanadigan joy sifatida tayyorlab
  qo'yilgan (hozircha faqat konsolga yozadi / no-op).
"""
import datetime
import os
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.deps import get_current_user
from app.models import (
    User, RoleEnum, Product, ProductStatus, OriginCountry,
    Order, OrderStatus, Inventory, CargoBatch, CargoStatus,
)
from app.schemas import (
    ProductOut, FxRatesOut, FxRateItem, CargoCalcOut,
    DashboardOut, DashboardOrderSummary, NotificationOut,
)

router = APIRouter(prefix="/api", tags=["Qo'shimcha"])


# ---------------------------------------------------------------------------
# 1) Valyuta kurslari
# ---------------------------------------------------------------------------

# cbu.uz (Markaziy bank) saytidan 2026-10-10 kuni olingan snapshot.
FX_RATES = {
    "updated_at": "2026-10-10",
    "source": "cbu.uz (Markaziy bank) — qo'lda olingan snapshot, avtomatik yangilanmaydi",
    "rates": [
        {"code": "USD", "name_uz": "AQSH dollari", "rate_uzs": Decimal("11897.90"), "symbol": "$"},
        {"code": "CNY", "name_uz": "Xitoy yuani", "rate_uzs": Decimal("1777.88"), "symbol": "¥"},
        {"code": "TRY", "name_uz": "Turk lirasi", "rate_uzs": Decimal("241.13"), "symbol": "₺"},
    ],
}


@router.get("/fx-rates", response_model=FxRatesOut)
def fx_rates():
    return FX_RATES


# ---------------------------------------------------------------------------
# 2) Kargo kalkulyatori (vazn asosida taxminiy narx)
# ---------------------------------------------------------------------------

# Taxminiy havo-kargo tariflari (USD/kg) — umumiy mo''ljal uchun. Haqiqiy narx
# yukning hajmi (CBM), tovar turi va joriy aviakompaniya tariflariga qarab farq qiladi.
CARGO_RATES_USD_PER_KG = {
    OriginCountry.china: Decimal("5.50"),
    OriginCountry.turkey: Decimal("4.20"),
    OriginCountry.other: Decimal("6.00"),
}
CARGO_LEAD_DAYS = {
    OriginCountry.china: "12-18",
    OriginCountry.turkey: "7-10",
    OriginCountry.other: "15-25",
}


@router.get("/cargo/calc", response_model=CargoCalcOut)
def cargo_calc(origin: OriginCountry, weight_kg: Decimal):
    if weight_kg <= 0:
        raise HTTPException(status_code=400, detail="Vazn 0 dan katta bo'lishi kerak")
    if weight_kg > 5000:
        raise HTTPException(status_code=400, detail="Juda katta vazn — operator bilan bog'laning")

    rate = CARGO_RATES_USD_PER_KG.get(origin, CARGO_RATES_USD_PER_KG[OriginCountry.other])
    usd_amount = (rate * weight_kg).quantize(Decimal("0.01"))
    usd_rate_uzs = next(r["rate_uzs"] for r in FX_RATES["rates"] if r["code"] == "USD")
    uzs_amount = (usd_amount * usd_rate_uzs).quantize(Decimal("1"))

    return CargoCalcOut(
        origin=origin.value,
        weight_kg=weight_kg,
        rate_per_kg_usd=rate,
        usd_amount=usd_amount,
        uzs_amount=uzs_amount,
        estimated_days=CARGO_LEAD_DAYS.get(origin, "15-25"),
        note="Taxminiy narx (havo-kargo, umumiy tovar). Hajmli (CBM) yuklar uchun aniq "
             "narxni operator bilan tasdiqlang.",
    )


# ---------------------------------------------------------------------------
# 3) "Ommabop / TOP sotuv" mahsulotlar
# ---------------------------------------------------------------------------

@router.get("/trending", response_model=list[ProductOut])
def trending_products(limit: int = 10, db: Session = Depends(get_db)):
    return (
        db.query(Product)
        .filter(Product.is_trending.is_(True), Product.status == ProductStatus.active)
        .limit(limit)
        .all()
    )


# ---------------------------------------------------------------------------
# 4) B2B shaxsiy kabinet (balans, statistika, kargodagi partiyalar)
# ---------------------------------------------------------------------------

@router.get("/me/dashboard", response_model=DashboardOut)
def my_dashboard(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == current_user.id).all()

    orders_by_status: dict[str, int] = {}
    total_spent = Decimal("0")
    for o in orders:
        key = o.status.value if hasattr(o.status, "value") else str(o.status)
        orders_by_status[key] = orders_by_status.get(key, 0) + 1
        if o.status not in (OrderStatus.canceled, OrderStatus.returned):
            total_spent += Decimal(o.total_amount or 0)

    recent = sorted(orders, key=lambda o: o.created_at, reverse=True)[:5]
    recent_out = [
        DashboardOrderSummary(
            order_number=o.order_number, status=o.status.value,
            total_amount=o.total_amount or Decimal("0"), created_at=o.created_at,
        )
        for o in recent
    ]

    active_cargo = db.query(CargoBatch).filter(CargoBatch.status != CargoStatus.arrived).count()

    low_stock_count = None
    if current_user.role in (RoleEnum.super_admin, RoleEnum.admin, RoleEnum.warehouse_operator, RoleEnum.operator):
        low_stock_count = (
            db.query(Inventory)
            .filter(Inventory.quantity_available <= Inventory.min_stock_alert)
            .count()
        )

    return DashboardOut(
        balance=current_user.balance or Decimal("0"),
        client_type=current_user.client_type.value,
        is_wholesale_verified=current_user.is_wholesale_verified,
        total_orders=len(orders),
        total_spent=total_spent,
        orders_by_status=orders_by_status,
        active_cargo_batches=active_cargo,
        recent_orders=recent_out,
        low_stock_count=low_stock_count,
    )


# ---------------------------------------------------------------------------
# 5) Bildirishnomalar (buyurtma holati / yangi buyurtma / kam zaxira)
# ---------------------------------------------------------------------------

def notify_external(user: User, title: str, message: str) -> None:
    """
    SMS yoki qo'ng'iroq integratsiyasi uchun tayyorlab qo'yilgan joy.
    Hozircha hech narsa jo'natmaydi (no-op) — faqat qayerga ulash kerakligini ko'rsatadi.
    Masalan Eskiz.uz SMS API: https://eskiz.uz/ (ro'yxatdan o'ting, API token oling,
    so'ng shu yerga requests.post(...) chaqiruvini qo'shing).
    """
    return None


STATUS_LABEL_UZ = {
    "new": "Yangi", "confirmed": "Tasdiqlandi", "packed": "Yig'ildi",
    "shipped": "Jo'natildi", "delivered": "Yetkazildi", "canceled": "Bekor qilindi",
    "returned": "Qaytarildi",
}


@router.get("/notifications", response_model=list[NotificationOut])
def my_notifications(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    items: list[NotificationOut] = []

    staff_roles = (RoleEnum.super_admin, RoleEnum.admin, RoleEnum.operator, RoleEnum.warehouse_operator)
    if current_user.role in staff_roles:
        new_orders = (
            db.query(Order).filter(Order.status == OrderStatus.new)
            .order_by(Order.created_at.desc()).limit(10).all()
        )
        for o in new_orders:
            items.append(NotificationOut(
                id=f"neworder-{o.id}", type="new_order", level="info",
                title="Yangi buyurtma tushdi",
                message=f"{o.order_number} — {o.total_amount:,.0f} so'm".replace(",", " "),
                created_at=o.created_at,
            ))

        low_stock = (
            db.query(Inventory).filter(Inventory.quantity_available <= Inventory.min_stock_alert)
            .limit(10).all()
        )
        for inv in low_stock:
            title = inv.variant.product.title if inv.variant and inv.variant.product else f"Variant #{inv.variant_id}"
            items.append(NotificationOut(
                id=f"lowstock-{inv.id}", type="low_stock", level="warning",
                title="Zaxira kam qoldi",
                message=f"{title} ({inv.variant.size or ''}/{inv.variant.color or ''}) — {inv.quantity_available} dona qoldi",
                created_at=inv.updated_at or datetime.datetime.utcnow(),
            ))
    else:
        my_orders = (
            db.query(Order)
            .filter(Order.user_id == current_user.id, Order.status != OrderStatus.new)
            .order_by(Order.created_at.desc()).limit(10).all()
        )
        for o in my_orders:
            label = STATUS_LABEL_UZ.get(o.status.value, o.status.value)
            level = "success" if o.status == OrderStatus.delivered else (
                "warning" if o.status in (OrderStatus.canceled, OrderStatus.returned) else "info"
            )
            items.append(NotificationOut(
                id=f"order-{o.id}-{o.status.value}", type="order_status", level=level,
                title=f"Buyurtma holati: {label}",
                message=f"{o.order_number} — {o.total_amount:,.0f} so'm".replace(",", " "),
                created_at=o.created_at,
            ))

    items.sort(key=lambda n: n.created_at, reverse=True)
    return items[:15]


# ---------------------------------------------------------------------------
# 6) Hamkorlik shartnomasi — namunaviy hujjatni yuklab olish
# ---------------------------------------------------------------------------

@router.get("/documents/contract-template")
def download_contract_template():
    path = os.path.join(settings.documents_dir, "optom-market-shartnoma-namuna.docx")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Shartnoma namunasi hali yuklanmagan")
    return FileResponse(
        path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="OPTOM-MARKET-shartnoma-namuna.docx",
    )
