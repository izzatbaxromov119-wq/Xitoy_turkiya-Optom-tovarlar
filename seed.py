"""
Demo ma'lumotlar bilan bazani to'ldiradi: barcha RBAC rollari uchun test hisoblar,
8 ta kategoriya, 160 ta mahsulot (~480 variant), omborlar va qoldiqlar.

Ishga tushirish:
    python seed.py
"""
from app.database import Base, engine, SessionLocal
from app.models import (
    User, RoleEnum, ClientType,
    Category, GenderEnum,
    Product, ProductStatus, ProductVariant,
    Price, PriceTier,
    Warehouse, WarehouseType, Inventory,
    CargoBatch, CargoStatus, OriginCountry,
    Order, OrderItem, OrderStatus, OrderType, PaymentStatus, DeliveryTypeEnum,
    Courier, Delivery, DeliveryStatus,
)
from app.security import hash_password
from catalog_data import CATEGORIES, CATALOG

Base.metadata.create_all(bind=engine)
db = SessionLocal()


def get_or_create(model, defaults=None, **kwargs):
    instance = db.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    params = {**kwargs, **(defaults or {})}
    instance = model(**params)
    db.add(instance)
    db.flush()
    return instance, True


# ---------------------------------------------------------------------------
# Foydalanuvchilar — TZ'dagi barcha RBAC rollari uchun tayyor test hisoblar
# (Mehmon rol sifatida saqlanmaydi — u shunchaki tizimga kirmagan holat)
# ---------------------------------------------------------------------------

super_admin, _ = get_or_create(
    User, phone="+998900000001",
    defaults=dict(
        full_name="Super Admin", email="admin@optommarket.uz",
        password_hash=hash_password("Admin12345"),
        role=RoleEnum.super_admin, client_type=ClientType.retail, is_wholesale_verified=True,
    ),
)

admin, _ = get_or_create(
    User, phone="+998900000003",
    defaults=dict(
        full_name="Aziz Nazarov", password_hash=hash_password("Admin12345"),
        role=RoleEnum.admin,
    ),
)

operator, _ = get_or_create(
    User, phone="+998900000004",
    defaults=dict(
        full_name="Dilnoza Yusupova", password_hash=hash_password("Operator12345"),
        role=RoleEnum.operator,
    ),
)

get_or_create(
    User, phone="+998900000002",
    defaults=dict(
        full_name="Ombor Menejeri", password_hash=hash_password("Manager12345"),
        role=RoleEnum.warehouse_operator,
    ),
)

get_or_create(
    User, phone="+998901234567",
    defaults=dict(
        full_name="Aziza Karimova", password_hash=hash_password("Customer123"),
        role=RoleEnum.customer, client_type=ClientType.retail, balance=350_000,
    ),
)

# Optom mijoz — tasdiqlangan (is_wholesale_verified=True), 5+ dona qanday bo'lsa ham
# avtomatik optom narx ko'rinadi (miqdor - asosiy mezon), lekin bu hisob shuni
# namoyish etish uchun махсус tasdiqlangan optom mijoz sifatida belgilangan.
# balance — B2B kabinetdagi "Balans" blokini bo'sh ko'rsatmaslik uchun namunaviy qiymat
# (hech qanday to'lov tizimiga ulanmagan, faqat demo ko'rsatkich).
get_or_create(
    User, phone="+998907778899",
    defaults=dict(
        full_name="Bahrom Tursunov", password_hash=hash_password("Wholesale123"),
        role=RoleEnum.customer, client_type=ClientType.wholesale, is_wholesale_verified=True,
        balance=15_000_000,
    ),
)

# ---------------------------------------------------------------------------
# Kategoriyalar
# ---------------------------------------------------------------------------

category_by_slug = {}
for c in CATEGORIES:
    cat, _ = get_or_create(Category, slug=c["slug"], defaults=dict(
        name_uz=c["name_uz"], name_ru=c["name_ru"],
        gender=GenderEnum(c["gender"]), sort_order=c["sort_order"],
    ))
    category_by_slug[c["slug"]] = cat

# ---------------------------------------------------------------------------
# Omborlar
# ---------------------------------------------------------------------------

wh_china, _ = get_or_create(Warehouse, name="Guangzhou yig'uv punkti", defaults=dict(
    country="china", city="Guangzhou", type=WarehouseType.collection_hub))
wh_turkey, _ = get_or_create(Warehouse, name="Istanbul yig'uv punkti", defaults=dict(
    country="turkey", city="Istanbul", type=WarehouseType.collection_hub))
wh_main, _ = get_or_create(Warehouse, name="Toshkent asosiy ombor", defaults=dict(
    country="uzbekistan", city="Toshkent", type=WarehouseType.main_warehouse))

# ---------------------------------------------------------------------------
# Mahsulotlar (avtomatik generatsiya qilingan 84 ta mahsulot, catalog_data.py)
# ---------------------------------------------------------------------------

ORIGIN_MAP = {"Turkiya": OriginCountry.turkey, "Xitoy": OriginCountry.china}
created_products = 0
created_variants = 0

# "Ommabop / TOP sotuv" bo'limi uchun — har bir kategoriyadan 1-2 tadan, qo'lda tanlangan
# mahsulotlar (ids). Haqiqiy loyihada bu real sotuv sonlariga qarab avtomatik hisoblanadi.
TRENDING_PRODUCT_IDS = {6, 12, 25, 45, 65, 85, 103, 108, 125, 145}

# Optom qadoq konvensiyasi: 1 quti/korobkada nechta dona (kategoriya bo'yicha taxminiy norma)
BOX_QTY_BY_CATEGORY = {
    "ayollar-kiyimi": 20, "erkaklar-kiyimi": 20, "bolalar-kiyimi": 24,
    "chaqaloqlar-kiyimi": 30, "ich-kiyim": 50, "oyoq-kiyim": 10,
    "sumkalar": 15, "bosh-kiyimlar": 30,
}

for item in CATALOG:
    box_qty = BOX_QTY_BY_CATEGORY.get(item["category_id"], 20)
    if len(item["variants"]) > 1:
        box_note = f"1 quti — {box_qty} dona, assorti o'lchamlar aralash"
    else:
        box_note = f"1 quti — {box_qty} dona, bir xil o'lcham"

    product, was_created = get_or_create(Product, title=item["title"], defaults=dict(
        category_id=category_by_slug[item["category_id"]].id,
        description=f"{item['title']} — {item['origin']}dan import qilingan, sifatli material.",
        origin_country=ORIGIN_MAP[item["origin"]],
        status=ProductStatus.active, created_by=admin.id,
        is_trending=item["id"] in TRENDING_PRODUCT_IDS,
        box_qty=box_qty, box_note=box_note,
    ))
    if not was_created:
        continue
    created_products += 1

    for vdata in item["variants"]:
        variant = ProductVariant(
            product_id=product.id, size=vdata["size"], color=vdata["color"],
            sku=vdata["sku"], weight_gram=300,
        )
        db.add(variant)
        db.flush()
        created_variants += 1

        db.add(Price(
            variant_id=variant.id, retail_price=vdata["retail"], wholesale_price=vdata["wholesale"],
            wholesale_min_qty=vdata["min_qty"],
        ))
        for min_qty, price in vdata["tiers"]:
            db.add(PriceTier(variant_id=variant.id, min_qty=min_qty, unit_price=price))

        db.add(Inventory(
            variant_id=variant.id, warehouse_id=wh_main.id,
            quantity_available=vdata["available"], min_stock_alert=10,
        ))

# ---------------------------------------------------------------------------
# Namunaviy kargo partiyasi
# ---------------------------------------------------------------------------

get_or_create(CargoBatch, batch_number="CN-2026-0912", defaults=dict(
    origin_country=OriginCountry.china, carrier_name="China Post Cargo", status=CargoStatus.arrived,
))
get_or_create(CargoBatch, batch_number="TR-2026-0630", defaults=dict(
    origin_country=OriginCountry.turkey, carrier_name="Turkish Cargo Express", status=CargoStatus.arrived,
))
# Hozir yo'lda bo'lgan partiya — Kabinet/Dashboard'dagi "Yo'ldagi kargo partiyalari" ko'rsatkichi
# bo'sh bo'lib qolmasligi uchun.
get_or_create(CargoBatch, batch_number="CN-2026-1004", defaults=dict(
    origin_country=OriginCountry.china, carrier_name="China Post Cargo", status=CargoStatus.in_transit,
))

# ---------------------------------------------------------------------------
# Namunaviy kuryer, tayyor buyurtma va kargo tracking
# (frontend "Buyurtmalarim" / "Kargo tracking" bo'limlari bo'sh bo'lib qolmasligi uchun)
# ---------------------------------------------------------------------------

customer = db.query(User).filter(User.phone == "+998901234567").first()

courier_user, _ = get_or_create(
    User, phone="+998901110001",
    defaults=dict(full_name="Sardor Rahimov", password_hash=hash_password("Courier12345"), role=RoleEnum.courier),
)
courier, _ = get_or_create(Courier, user_id=courier_user.id, defaults=dict(
    region="Toshkent shahri", vehicle_type="Motosikl", is_active=True,
))

demo_variant = db.query(ProductVariant).filter(ProductVariant.sku == "WM-01-S").first()
if demo_variant:
    demo_order, order_created = get_or_create(Order, order_number="OM-DEMO-0001", defaults=dict(
        user_id=customer.id, status=OrderStatus.shipped, order_type=OrderType.retail,
        total_amount=demo_variant.price.retail_price * 2 if demo_variant.price else 0,
        delivery_type=DeliveryTypeEnum.courier, warehouse_id=wh_main.id,
        payment_status=PaymentStatus.paid,
    ))
    if order_created:
        db.add(OrderItem(
            order_id=demo_order.id, variant_id=demo_variant.id, quantity=2,
            price_type="retail", unit_price=demo_variant.price.retail_price,
            total_price=demo_variant.price.retail_price * 2,
        ))
        get_or_create(Delivery, tracking_number="OM-DEMO-0001-TRK", defaults=dict(
            order_id=demo_order.id, delivery_method=DeliveryTypeEnum.courier, courier_id=courier.id,
            region="Toshkent shahri, Chilonzor tumani", status=DeliveryStatus.out_for_delivery,
        ))
        # ombordan mos ravishda kamaytiramiz, chunki bu buyurtma "shipped" holatida
        inv = db.query(Inventory).filter(Inventory.variant_id == demo_variant.id, Inventory.warehouse_id == wh_main.id).first()
        if inv and inv.quantity_available >= 2:
            inv.quantity_available -= 2

# Ikkinchi namunaviy buyurtma — optom mijoz tomonidan, "Yangi" holatida qoldiriladi,
# shunda admin/operator uchun "Yangi buyurtma tushdi" bildirishnomasi va Kabinet
# statistikasi bo'sh bo'lib qolmaydi.
wholesale_user = db.query(User).filter(User.phone == "+998907778899").first()
demo_variant2 = db.query(ProductVariant).filter(ProductVariant.sku == "WM-02-M").first()
if wholesale_user and demo_variant2 and demo_variant2.price:
    qty2 = 10
    unit2 = demo_variant2.price.wholesale_price
    demo_order2, order2_created = get_or_create(Order, order_number="OM-DEMO-0002", defaults=dict(
        user_id=wholesale_user.id, status=OrderStatus.new, order_type=OrderType.wholesale,
        total_amount=unit2 * qty2, delivery_type=DeliveryTypeEnum.post, warehouse_id=wh_main.id,
        payment_status=PaymentStatus.pending,
    ))
    if order2_created:
        db.add(OrderItem(
            order_id=demo_order2.id, variant_id=demo_variant2.id, quantity=qty2,
            price_type="wholesale", unit_price=unit2, total_price=unit2 * qty2,
        ))
        inv2 = db.query(Inventory).filter(
            Inventory.variant_id == demo_variant2.id, Inventory.warehouse_id == wh_main.id
        ).first()
        if inv2 and inv2.quantity_available >= qty2:
            inv2.quantity_available -= qty2
            inv2.quantity_reserved += qty2

# Bir nechta variant uchun ogohlantirish chegarasini real qoldiqdan yuqori qilib
# qo'yamiz — shunda admin/omborchi "Zaxira kam qoldi" bildirishnomasini ham ko'radi
# (haqiqiy funksiya ishlayotganini namoyish etish uchun).
for low_sku in ("WM-03-S", "WM-05-L"):
    v = db.query(ProductVariant).filter(ProductVariant.sku == low_sku).first()
    if v:
        inv_low = db.query(Inventory).filter(
            Inventory.variant_id == v.id, Inventory.warehouse_id == wh_main.id
        ).first()
        if inv_low:
            inv_low.min_stock_alert = max(inv_low.min_stock_alert, inv_low.quantity_available + 5)

db.commit()
db.close()

print("=" * 60)
print("BAZA MUVAFFAQIYATLI TO'LDIRILDI")
print("=" * 60)
print(f"Kategoriyalar: {len(CATEGORIES)} ta")
print(f"Yangi mahsulotlar: {created_products} ta")
print(f"Yangi variantlar: {created_variants} ta")
print()
print("Admin panel:  http://127.0.0.1:8000/admin")
print()
print("TAYYOR TEST HISOBLARI (barcha parol hammasida ko'rsatilgan):")
print("  Super Admin   : +998900000001 / Admin12345")
print("  Admin         : +998900000003 / Admin12345")
print("  Operator      : +998900000004 / Operator12345")
print("  Omborchi      : +998900000002 / Manager12345")
print("  Kuryer        : +998901110001 / Courier12345")
print("  Mijoz (dona)  : +998901234567 / Customer123")
print("  Optom mijoz   : +998907778899 / Wholesale123")
print()
print("API hujjatlari: http://127.0.0.1:8000/docs")
print()
print("Namunaviy tracking raqam (Kargo tracking bo'limida sinab ko'ring):")
print("  OM-DEMO-0001-TRK")
print("=" * 60)
