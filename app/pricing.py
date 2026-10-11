"""
Dona / optom narxlarni avtomatik hisoblash mantiqi.
TZ hujjatining "Smart Pricing" bo'limidagi algoritmning to'g'ridan-to'g'ri dasturiy ifodasi.

STANDART 4-BOSQICHLI NARXLASH (barcha mahsulotlar uchun bir xil chegaralar):
    1-4 dona    -> Dona narx     (retail_price)
    5-19 dona   -> Kichik optom  (price_tiers ichidan min_qty=5 bosqich)
    20-49 dona  -> Optom          (price_tiers ichidan min_qty=20 bosqich)
    50+ dona    -> Katta optom    (price_tiers ichidan min_qty=50 bosqich)

Qoida:
1) quantity < wholesale_min_qty  -> retail_price qo'llanadi.
2) quantity >= wholesale_min_qty -> price_tiers ichidan miqdorga mos ENG YUQORI
   bosqich tanlanadi.
3) Mos tier topilmasa -> bazaviy wholesale_price qo'llanadi.
4) Natija cart_items.unit_price_snapshot ga "muzlatiladi" -- keyinchalik admin
   narxni o'zgartirsa ham, mijozning savati/buyurtmasidagi narx o'zgarmaydi.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable

from app.models import Price, PriceTier


@dataclass
class PriceResult:
    unit_price: Decimal
    price_type: str  # "retail" | "wholesale"
    tier_label: str  # "Dona narx" | "Kichik optom" | "Optom" | "Katta optom"


def tier_label_for_quantity(quantity: int) -> str:
    """TZ'dagi standart 4-bosqichli nomlash — faqat miqdorga qarab (barcha mahsulotlar uchun bir xil)."""
    if quantity < 5:
        return "Dona narx"
    if quantity < 20:
        return "Kichik optom"
    if quantity < 50:
        return "Optom"
    return "Katta optom"


def calculate_unit_price(price: Price, tiers: Iterable[PriceTier], quantity: int) -> PriceResult:
    if price is None:
        raise ValueError("Ushbu variant uchun narx belgilanmagan")

    label = tier_label_for_quantity(quantity)

    if quantity < price.wholesale_min_qty:
        return PriceResult(unit_price=price.retail_price, price_type="retail", tier_label=label)

    # Miqdorga mos eng yuqori (eng foydali) optom bosqichini tanlaymiz
    matching_tiers = [t for t in tiers if quantity >= t.min_qty]
    if matching_tiers:
        best_tier = max(matching_tiers, key=lambda t: t.min_qty)
        return PriceResult(unit_price=best_tier.unit_price, price_type="wholesale", tier_label=label)

    return PriceResult(unit_price=price.wholesale_price, price_type="wholesale", tier_label=label)


def determine_order_type(price_types: Iterable[str]) -> str:
    """Savatdagi barcha price_type qiymatlariga qarab orders.order_type ni aniqlaydi."""
    unique_types = set(price_types)
    if unique_types == {"retail"}:
        return "retail"
    if unique_types == {"wholesale"}:
        return "wholesale"
    return "mixed"
