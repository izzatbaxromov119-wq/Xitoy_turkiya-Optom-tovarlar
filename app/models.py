import enum
import datetime

from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, ForeignKey,
    Numeric, Enum as SAEnum, UniqueConstraint
)
from sqlalchemy.orm import relationship

from app.database import Base


def utcnow():
    return datetime.datetime.utcnow()


# ---------------------------------------------------------------------------
# ENUMS (TZ hujjatidagi ENUM ustunlarga mos)
# ---------------------------------------------------------------------------

class RoleEnum(str, enum.Enum):
    """
    TZ'dagi RBAC rollari:
      - Mehmon          -> tizimda saqlanmaydi (token yo'q holat, hamma uchun ochiq)
      - Ro'yxatdan o'tgan mijoz / Optom mijoz -> ROLENING O'ZI EMAS, balki `customer` +
        `ClientType` (retail/wholesale) orqali farqlanadi (quyida)
      - Operator        -> buyurtmalarni qayta ishlash (tasdiqlash/yig'ish holatini boshqarish)
      - Omborchi         -> ombor qoldig'i (stock-in/transfer)
      - Kuryer            -> faqat o'ziga biriktirilgan yetkazib berishlar
      - Admin / Super Admin -> to'liq boshqaruv (katalog, narx, foydalanuvchilar, rollar)
    """
    super_admin = "super_admin"
    admin = "admin"
    operator = "operator"
    warehouse_operator = "warehouse_operator"
    courier = "courier"
    customer = "customer"


class ClientType(str, enum.Enum):
    retail = "retail"
    wholesale = "wholesale"


class GenderEnum(str, enum.Enum):
    woman = "woman"
    man = "man"
    kids = "kids"
    baby = "baby"
    unisex = "unisex"


class OriginCountry(str, enum.Enum):
    china = "china"
    turkey = "turkey"
    other = "other"


class ProductStatus(str, enum.Enum):
    draft = "draft"
    active = "active"
    archived = "archived"


class OrderStatus(str, enum.Enum):
    new = "new"
    confirmed = "confirmed"
    packed = "packed"
    shipped = "shipped"
    delivered = "delivered"
    canceled = "canceled"
    returned = "returned"


class OrderType(str, enum.Enum):
    retail = "retail"
    wholesale = "wholesale"
    mixed = "mixed"


class PaymentStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"
    refunded = "refunded"


class DeliveryTypeEnum(str, enum.Enum):
    courier = "courier"
    post = "post"


class WarehouseType(str, enum.Enum):
    collection_hub = "collection_hub"
    main_warehouse = "main_warehouse"
    branch = "branch"


class MovementType(str, enum.Enum):
    income = "income"
    outcome = "outcome"
    transfer = "transfer"
    return_ = "return"
    adjustment = "adjustment"


class CargoStatus(str, enum.Enum):
    collecting = "collecting"
    in_transit = "in_transit"
    customs = "customs"
    arrived = "arrived"


class DeliveryStatus(str, enum.Enum):
    pending = "pending"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"
    failed = "failed"


# ---------------------------------------------------------------------------
# FOYDALANUVCHILAR VA HUQUQLAR
# ---------------------------------------------------------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(150), unique=True, nullable=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(SAEnum(RoleEnum), default=RoleEnum.customer, nullable=False)
    client_type = Column(SAEnum(ClientType), default=ClientType.retail, nullable=False)
    is_wholesale_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    # Namunaviy/ko'rsatkich balans — hech qanday to'lov provayderiga ulanmagan (demo maydon).
    # Haqiqiy loyihada bu yerga Payme/Click kabi to'lov tizimi orqali to'ldiriladigan balans keladi.
    balance = Column(Numeric(14, 2), default=0)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

    addresses = relationship("UserAddress", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return f"{self.full_name} ({self.phone})"


class UserAddress(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    region = Column(String(100))
    district = Column(String(100))
    street = Column(String(200))
    house = Column(String(20))
    landmark = Column(String(200))
    is_default = Column(Boolean, default=False)

    user = relationship("User", back_populates="addresses")


# ---------------------------------------------------------------------------
# KATALOG
# ---------------------------------------------------------------------------

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    name_uz = Column(String(120), nullable=False)
    name_ru = Column(String(120))
    slug = Column(String(140), unique=True, nullable=False, index=True)
    gender = Column(SAEnum(GenderEnum), default=GenderEnum.unisex)
    icon_url = Column(String(255))
    sort_order = Column(Integer, default=0)

    products = relationship("Product", back_populates="category")
    children = relationship("Category", backref="parent", remote_side=[id])

    def __str__(self):
        return self.name_uz


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    country_origin = Column(SAEnum(OriginCountry), default=OriginCountry.china)

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    image_url = Column(String(500), nullable=True)  # admin panel orqali yuklangan haqiqiy surat
    origin_country = Column(SAEnum(OriginCountry), default=OriginCountry.china)
    status = Column(SAEnum(ProductStatus), default=ProductStatus.draft)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=utcnow)
    # "Ommabop / TOP sotuv" bo'limi uchun qo'lda belgilanadigan bayroq
    is_trending = Column(Boolean, default=False)
    # Optom qadoq ma'lumoti: 1 quti/korobkada nechta dona va qanday assorti
    box_qty = Column(Integer, nullable=True)
    box_note = Column(String(200), nullable=True)

    category = relationship("Category", back_populates="products")
    brand = relationship("Brand")
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")

    def __str__(self):
        return self.title


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    size = Column(String(20))
    color = Column(String(40))
    sku = Column(String(60), unique=True, nullable=False, index=True)
    barcode = Column(String(60))
    weight_gram = Column(Integer, default=0)

    product = relationship("Product", back_populates="variants")
    price = relationship("Price", back_populates="variant", uselist=False, cascade="all, delete-orphan")
    price_tiers = relationship("PriceTier", back_populates="variant", cascade="all, delete-orphan")
    inventory_items = relationship("Inventory", back_populates="variant", cascade="all, delete-orphan")

    @property
    def available_qty(self) -> int:
        """Barcha omborlar bo'yicha jami bo'sh (sotishga tayyor) qoldiq."""
        return sum((i.quantity_available or 0) for i in self.inventory_items)

    def __str__(self):
        return self.sku


# ---------------------------------------------------------------------------
# NARXLASH (dona / optom)
# ---------------------------------------------------------------------------

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), unique=True, nullable=False)
    retail_price = Column(Numeric(12, 2), nullable=False)
    wholesale_price = Column(Numeric(12, 2), nullable=False)
    wholesale_min_qty = Column(Integer, default=5)
    currency = Column(String(6), default="UZS")
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

    variant = relationship("ProductVariant", back_populates="price")


class PriceTier(Base):
    __tablename__ = "price_tiers"

    id = Column(Integer, primary_key=True)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), nullable=False)
    min_qty = Column(Integer, nullable=False)
    unit_price = Column(Numeric(12, 2), nullable=False)

    variant = relationship("ProductVariant", back_populates="price_tiers")


# ---------------------------------------------------------------------------
# OMBOR VA QOLDIQ
# ---------------------------------------------------------------------------

class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    country = Column(String(30), nullable=False)
    city = Column(String(100))
    type = Column(SAEnum(WarehouseType), default=WarehouseType.main_warehouse)

    def __str__(self):
        return self.name


class Inventory(Base):
    __tablename__ = "inventory"
    __table_args__ = (UniqueConstraint("variant_id", "warehouse_id", name="uq_variant_warehouse"),)

    id = Column(Integer, primary_key=True)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    quantity_available = Column(Integer, default=0)
    quantity_reserved = Column(Integer, default=0)
    quantity_in_transit = Column(Integer, default=0)
    min_stock_alert = Column(Integer, default=5)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

    variant = relationship("ProductVariant", back_populates="inventory_items")
    warehouse = relationship("Warehouse")


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    movement_type = Column(SAEnum(MovementType), nullable=False)
    quantity = Column(Integer, nullable=False)
    related_order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    cargo_batch_id = Column(Integer, ForeignKey("cargo_batches.id"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=utcnow)


# ---------------------------------------------------------------------------
# SAVAT VA BUYURTMA
# ---------------------------------------------------------------------------

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    session_id = Column(String(80), nullable=True)
    created_at = Column(DateTime, default=utcnow)

    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_type = Column(String(20))
    unit_price_snapshot = Column(Numeric(12, 2))

    cart = relationship("Cart", back_populates="items")
    variant = relationship("ProductVariant")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_number = Column(String(30), unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(SAEnum(OrderStatus), default=OrderStatus.new)
    order_type = Column(SAEnum(OrderType), default=OrderType.retail)
    total_amount = Column(Numeric(14, 2), default=0)
    delivery_type = Column(SAEnum(DeliveryTypeEnum), default=DeliveryTypeEnum.courier)
    delivery_address_id = Column(Integer, ForeignKey("user_addresses.id"), nullable=True)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=True)
    payment_status = Column(SAEnum(PaymentStatus), default=PaymentStatus.pending)
    created_at = Column(DateTime, default=utcnow)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __str__(self):
        return self.order_number


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    variant_id = Column(Integer, ForeignKey("product_variants.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_type = Column(String(20))
    unit_price = Column(Numeric(12, 2))
    total_price = Column(Numeric(14, 2))

    order = relationship("Order", back_populates="items")
    variant = relationship("ProductVariant")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    provider = Column(String(20))
    amount = Column(Numeric(14, 2))
    status = Column(String(20), default="pending")
    transaction_id = Column(String(100))
    paid_at = Column(DateTime, nullable=True)


# ---------------------------------------------------------------------------
# KARGO VA YETKAZIB BERISH
# ---------------------------------------------------------------------------

class CargoBatch(Base):
    __tablename__ = "cargo_batches"

    id = Column(Integer, primary_key=True)
    batch_number = Column(String(40), unique=True, nullable=False)
    origin_country = Column(SAEnum(OriginCountry), default=OriginCountry.china)
    carrier_name = Column(String(100))
    departure_date = Column(DateTime, nullable=True)
    arrival_date_estimated = Column(DateTime, nullable=True)
    status = Column(SAEnum(CargoStatus), default=CargoStatus.collecting)

    def __str__(self):
        return self.batch_number


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    region = Column(String(100))
    vehicle_type = Column(String(50))
    is_active = Column(Boolean, default=True)

    user = relationship("User")


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    delivery_method = Column(SAEnum(DeliveryTypeEnum), default=DeliveryTypeEnum.courier)
    courier_id = Column(Integer, ForeignKey("couriers.id"), nullable=True)
    region = Column(String(100))
    tracking_number = Column(String(60), unique=True)
    status = Column(SAEnum(DeliveryStatus), default=DeliveryStatus.pending)
    delivered_at = Column(DateTime, nullable=True)

    order = relationship("Order")
    courier = relationship("Courier")


# ---------------------------------------------------------------------------
# QO'SHIMCHA
# ---------------------------------------------------------------------------

class PromoCode(Base):
    __tablename__ = "promocodes"

    id = Column(Integer, primary_key=True)
    code = Column(String(40), unique=True, nullable=False)
    discount_type = Column(String(20), default="percent")  # percent | fixed
    discount_value = Column(Numeric(12, 2), default=0)
    min_order_amount = Column(Numeric(14, 2), default=0)
    usage_limit = Column(Integer, default=0)
    expires_at = Column(DateTime, nullable=True)
