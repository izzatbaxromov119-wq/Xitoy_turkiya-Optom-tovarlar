import datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel, EmailStr, ConfigDict, Field

from app.models import RoleEnum, ClientType, GenderEnum, OriginCountry, ProductStatus


# ---------------------------------------------------------------------------
# AUTH / USERS
# ---------------------------------------------------------------------------

class UserRegister(BaseModel):
    full_name: str = Field(min_length=2, max_length=150)
    phone: str = Field(min_length=7, max_length=20)
    email: Optional[EmailStr] = None
    password: str = Field(min_length=6, max_length=128)


class UserLogin(BaseModel):
    phone: str
    password: str


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    phone: str
    email: Optional[str] = None
    role: RoleEnum
    client_type: ClientType
    is_wholesale_verified: bool
    is_active: bool
    balance: Decimal = Decimal("0")
    created_at: datetime.datetime


class UserAddressCreate(BaseModel):
    region: str
    district: str
    street: str
    house: str
    landmark: Optional[str] = None
    is_default: bool = False


class UserAddressOut(UserAddressCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


# ---------------------------------------------------------------------------
# KATALOG
# ---------------------------------------------------------------------------

class CategoryCreate(BaseModel):
    parent_id: Optional[int] = None
    name_uz: str
    name_ru: Optional[str] = None
    slug: str
    gender: GenderEnum = GenderEnum.unisex
    icon_url: Optional[str] = None
    sort_order: int = 0


class CategoryOut(CategoryCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


class PriceTierIn(BaseModel):
    min_qty: int
    unit_price: Decimal


class PriceTierOut(PriceTierIn):
    model_config = ConfigDict(from_attributes=True)
    id: int


class PriceIn(BaseModel):
    retail_price: Decimal
    wholesale_price: Decimal
    wholesale_min_qty: int = 5
    currency: str = "UZS"


class PriceOut(PriceIn):
    model_config = ConfigDict(from_attributes=True)
    id: int


class VariantCreate(BaseModel):
    size: Optional[str] = None
    color: Optional[str] = None
    sku: str
    barcode: Optional[str] = None
    weight_gram: int = 0


class VariantOut(VariantCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    price: Optional[PriceOut] = None
    price_tiers: List[PriceTierOut] = []
    available_qty: int = 0


class ProductCreate(BaseModel):
    category_id: int
    brand_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    origin_country: OriginCountry = OriginCountry.china
    status: ProductStatus = ProductStatus.draft
    is_trending: bool = False
    box_qty: Optional[int] = None
    box_note: Optional[str] = None


class ProductOut(ProductCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime.datetime
    variants: List[VariantOut] = []


# ---------------------------------------------------------------------------
# SAVAT
# ---------------------------------------------------------------------------

class CartItemCreate(BaseModel):
    variant_id: int
    quantity: int = Field(gt=0)


class CartItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    variant_id: int
    quantity: int
    price_type: Optional[str]
    unit_price_snapshot: Optional[Decimal]
    line_total: Decimal


class CartOut(BaseModel):
    id: int
    items: List[CartItemOut]
    subtotal: Decimal
    order_type_preview: str


# ---------------------------------------------------------------------------
# BUYURTMA
# ---------------------------------------------------------------------------

class CheckoutRequest(BaseModel):
    delivery_address_id: Optional[int] = None
    delivery_type: str = "courier"  # courier | post
    warehouse_id: Optional[int] = None


class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    variant_id: int
    quantity: int
    price_type: str
    unit_price: Decimal
    total_price: Decimal


class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    order_number: str
    status: str
    order_type: str
    total_amount: Decimal
    delivery_type: str
    payment_status: str
    created_at: datetime.datetime
    items: List[OrderItemOut] = []


class OrderStatusUpdate(BaseModel):
    status: str


# ---------------------------------------------------------------------------
# OMBOR
# ---------------------------------------------------------------------------

class WarehouseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    country: str
    city: Optional[str]
    type: str


class StockInRequest(BaseModel):
    variant_id: int
    warehouse_id: int
    quantity: int = Field(gt=0)
    cargo_batch_id: Optional[int] = None


class StockTransferRequest(BaseModel):
    variant_id: int
    from_warehouse_id: int
    to_warehouse_id: int
    quantity: int = Field(gt=0)


class InventoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    variant_id: int
    warehouse_id: int
    quantity_available: int
    quantity_reserved: int
    quantity_in_transit: int
    min_stock_alert: int


# ---------------------------------------------------------------------------
# KARGO
# ---------------------------------------------------------------------------

class CargoBatchCreate(BaseModel):
    batch_number: str
    origin_country: OriginCountry
    carrier_name: Optional[str] = None
    departure_date: Optional[datetime.datetime] = None
    arrival_date_estimated: Optional[datetime.datetime] = None


class CargoBatchOut(CargoBatchCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str


class TrackingOut(BaseModel):
    tracking_number: str
    status: str
    delivery_method: str
    region: Optional[str]
    delivered_at: Optional[datetime.datetime]


# ---------------------------------------------------------------------------
# QO'SHIMCHA BO'LIMLAR: valyuta, kargo kalkulyatori, B2B kabinet, bildirishnomalar
# ---------------------------------------------------------------------------

class FxRateItem(BaseModel):
    code: str
    name_uz: str
    rate_uzs: Decimal
    symbol: str


class FxRatesOut(BaseModel):
    updated_at: str
    source: str
    rates: List[FxRateItem]


class CargoCalcOut(BaseModel):
    origin: str
    weight_kg: Decimal
    rate_per_kg_usd: Decimal
    usd_amount: Decimal
    uzs_amount: Decimal
    estimated_days: str
    note: str


class DashboardOrderSummary(BaseModel):
    order_number: str
    status: str
    total_amount: Decimal
    created_at: datetime.datetime


class DashboardOut(BaseModel):
    balance: Decimal
    client_type: str
    is_wholesale_verified: bool
    total_orders: int
    total_spent: Decimal
    orders_by_status: dict
    active_cargo_batches: int
    recent_orders: List[DashboardOrderSummary]
    low_stock_count: Optional[int] = None


class NotificationOut(BaseModel):
    id: str
    type: str
    level: str  # info | warning | success
    title: str
    message: str
    created_at: datetime.datetime
