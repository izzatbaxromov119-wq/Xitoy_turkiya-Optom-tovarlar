from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from app.config import settings
from app.database import SessionLocal, engine
from app.models import (
    User, UserAddress, Category, Brand, Product, ProductVariant,
    Price, PriceTier, Warehouse, Inventory, StockMovement,
    Order, OrderItem, Payment, CargoBatch, Courier, Delivery, PromoCode,
    RoleEnum,
)
from app.security import verify_password, create_access_token, decode_token


# ---------------------------------------------------------------------------
# Admin panel autentifikatsiyasi
# Faqat super_admin / manager / content_manager / warehouse_operator rollari
# /admin panelga kira oladi (RBAC talabiga mos).
# ---------------------------------------------------------------------------

ADMIN_ALLOWED_ROLES = {
    RoleEnum.super_admin,
    RoleEnum.admin,
    RoleEnum.operator,
    RoleEnum.warehouse_operator,
}


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        phone = form.get("username")
        password = form.get("password")

        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user or not verify_password(password, user.password_hash):
                return False
            if user.role not in ADMIN_ALLOWED_ROLES or not user.is_active:
                return False

            token = create_access_token(user.id, user.role.value)
            request.session.update({"token": token})
            return True
        finally:
            db.close()

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        payload = decode_token(token)
        if not payload or payload.get("type") != "access":
            return False
        if payload.get("role") not in {r.value for r in ADMIN_ALLOWED_ROLES}:
            return False
        return True


def _base_columns(model, extra):
    return ["id"] + extra


class UserAdmin(ModelView, model=User):
    name = "Foydalanuvchi"
    name_plural = "Foydalanuvchilar"
    icon = "fa-solid fa-user"
    category = "Foydalanuvchilar"
    column_list = ["id", "full_name", "phone", "email", "role", "client_type", "is_wholesale_verified", "is_active", "balance"]
    column_searchable_list = ["full_name", "phone", "email"]
    column_sortable_list = ["id", "created_at"]
    form_excluded_columns = ["password_hash", "orders", "addresses", "created_at", "updated_at"]


class UserAddressAdmin(ModelView, model=UserAddress):
    name = "Manzil"
    name_plural = "Manzillar"
    icon = "fa-solid fa-location-dot"
    category = "Foydalanuvchilar"
    column_list = ["id", "user_id", "region", "district", "street", "is_default"]


class CategoryAdmin(ModelView, model=Category):
    name = "Kategoriya"
    name_plural = "Kategoriyalar"
    icon = "fa-solid fa-tags"
    category = "Katalog"
    column_list = ["id", "name_uz", "slug", "gender", "parent_id", "sort_order"]
    column_searchable_list = ["name_uz", "slug"]


class BrandAdmin(ModelView, model=Brand):
    name = "Brend"
    name_plural = "Brendlar"
    icon = "fa-solid fa-copyright"
    category = "Katalog"
    column_list = ["id", "name", "country_origin"]


class ProductAdmin(ModelView, model=Product):
    name = "Mahsulot"
    name_plural = "Mahsulotlar"
    icon = "fa-solid fa-shirt"
    category = "Katalog"
    column_list = [
        "id", "title", "category_id", "brand_id", "image_url", "origin_country", "status",
        "is_trending", "box_qty", "box_note",
    ]
    column_searchable_list = ["title"]
    column_sortable_list = ["id", "created_at"]


class ProductVariantAdmin(ModelView, model=ProductVariant):
    name = "Variant"
    name_plural = "Variantlar (o'lcham/rang)"
    icon = "fa-solid fa-ruler"
    category = "Katalog"
    column_list = ["id", "product_id", "sku", "size", "color", "weight_gram"]
    column_searchable_list = ["sku"]


class PriceAdmin(ModelView, model=Price):
    name = "Narx"
    name_plural = "Narxlar"
    icon = "fa-solid fa-money-bill"
    category = "Narxlash"
    column_list = ["id", "variant_id", "retail_price", "wholesale_price", "wholesale_min_qty", "currency"]


class PriceTierAdmin(ModelView, model=PriceTier):
    name = "Optom bosqich"
    name_plural = "Optom bosqichlari"
    icon = "fa-solid fa-layer-group"
    category = "Narxlash"
    column_list = ["id", "variant_id", "min_qty", "unit_price"]


class WarehouseAdmin(ModelView, model=Warehouse):
    name = "Ombor"
    name_plural = "Omborlar"
    icon = "fa-solid fa-warehouse"
    category = "Ombor"
    column_list = ["id", "name", "country", "city", "type"]


class InventoryAdmin(ModelView, model=Inventory):
    name = "Qoldiq"
    name_plural = "Ombor qoldig'i"
    icon = "fa-solid fa-boxes-stacked"
    category = "Ombor"
    column_list = [
        "id", "variant_id", "warehouse_id", "quantity_available",
        "quantity_reserved", "quantity_in_transit", "min_stock_alert",
    ]


class StockMovementAdmin(ModelView, model=StockMovement):
    name = "Ombor harakati"
    name_plural = "Ombor harakatlari (log)"
    icon = "fa-solid fa-arrow-right-arrow-left"
    category = "Ombor"
    column_list = ["id", "variant_id", "warehouse_id", "movement_type", "quantity", "created_at"]
    can_create = False
    can_edit = False


class OrderAdmin(ModelView, model=Order):
    name = "Buyurtma"
    name_plural = "Buyurtmalar"
    icon = "fa-solid fa-cart-shopping"
    category = "Savdo"
    column_list = [
        "id", "order_number", "user_id", "status", "order_type",
        "total_amount", "payment_status", "created_at",
    ]
    column_searchable_list = ["order_number"]
    column_sortable_list = ["id", "created_at", "total_amount"]


class OrderItemAdmin(ModelView, model=OrderItem):
    name = "Buyurtma qatori"
    name_plural = "Buyurtma qatorlari"
    icon = "fa-solid fa-list"
    category = "Savdo"
    column_list = ["id", "order_id", "variant_id", "quantity", "price_type", "unit_price", "total_price"]
    can_create = False


class PaymentAdmin(ModelView, model=Payment):
    name = "To'lov"
    name_plural = "To'lovlar"
    icon = "fa-solid fa-credit-card"
    category = "Savdo"
    column_list = ["id", "order_id", "provider", "amount", "status", "paid_at"]


class CargoBatchAdmin(ModelView, model=CargoBatch):
    name = "Kargo partiyasi"
    name_plural = "Kargo partiyalari"
    icon = "fa-solid fa-ship"
    category = "Kargo"
    column_list = ["id", "batch_number", "origin_country", "carrier_name", "status", "arrival_date_estimated"]


class CourierAdmin(ModelView, model=Courier):
    name = "Kuryer"
    name_plural = "Kuryerlar"
    icon = "fa-solid fa-motorcycle"
    category = "Kargo"
    column_list = ["id", "user_id", "region", "vehicle_type", "is_active"]


class DeliveryAdmin(ModelView, model=Delivery):
    name = "Yetkazib berish"
    name_plural = "Yetkazib berishlar"
    icon = "fa-solid fa-truck-fast"
    category = "Kargo"
    column_list = ["id", "order_id", "delivery_method", "courier_id", "region", "tracking_number", "status"]
    column_searchable_list = ["tracking_number"]


class PromoCodeAdmin(ModelView, model=PromoCode):
    name = "Promo-kod"
    name_plural = "Promo-kodlar"
    icon = "fa-solid fa-percent"
    category = "Savdo"
    column_list = ["id", "code", "discount_type", "discount_value", "min_order_amount", "usage_limit", "expires_at"]


def register_admin(app):
    admin = Admin(
        app,
        engine,
        authentication_backend=AdminAuth(secret_key=settings.admin_secret_key),
        title="OPTOM MARKET — Boshqaruv paneli",
    )
    for view in [
        UserAdmin, UserAddressAdmin,
        CategoryAdmin, BrandAdmin, ProductAdmin, ProductVariantAdmin,
        PriceAdmin, PriceTierAdmin,
        WarehouseAdmin, InventoryAdmin, StockMovementAdmin,
        OrderAdmin, OrderItemAdmin, PaymentAdmin, PromoCodeAdmin,
        CargoBatchAdmin, CourierAdmin, DeliveryAdmin,
    ]:
        admin.add_view(view)
    return admin
