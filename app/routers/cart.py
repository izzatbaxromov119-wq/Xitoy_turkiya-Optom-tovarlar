from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import oauth2_scheme
from app.models import Cart, CartItem, ProductVariant, User
from app.pricing import calculate_unit_price, determine_order_type
from app.schemas import CartItemCreate, CartOut, CartItemOut
from app.security import decode_token

router = APIRouter(prefix="/api/cart", tags=["Savat"])


def _current_user_optional(token: Optional[str] = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Optional[User]:
    if not token:
        return None
    payload = decode_token(token)
    if not payload or payload.get("type") != "access":
        return None
    return db.query(User).filter(User.id == int(payload["sub"])).first()


def _get_or_create_cart(db: Session, user: Optional[User], session_id: Optional[str]) -> Cart:
    if user:
        cart = db.query(Cart).filter(Cart.user_id == user.id).first()
        if not cart:
            cart = Cart(user_id=user.id)
            db.add(cart)
            db.commit()
            db.refresh(cart)
        return cart

    if not session_id:
        raise HTTPException(
            status_code=400,
            detail="Mehmon foydalanuvchi uchun 'X-Session-Id' sarlavhasi kerak, yoki tizimga kiring",
        )
    cart = db.query(Cart).filter(Cart.session_id == session_id).first()
    if not cart:
        cart = Cart(session_id=session_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart


def _serialize_cart(cart: Cart) -> CartOut:
    items_out = []
    subtotal = Decimal("0")
    for item in cart.items:
        line_total = (item.unit_price_snapshot or Decimal("0")) * item.quantity
        subtotal += line_total
        items_out.append(CartItemOut(
            id=item.id,
            variant_id=item.variant_id,
            quantity=item.quantity,
            price_type=item.price_type,
            unit_price_snapshot=item.unit_price_snapshot,
            line_total=line_total,
        ))
    order_type_preview = determine_order_type([i.price_type for i in cart.items]) if cart.items else "retail"
    return CartOut(id=cart.id, items=items_out, subtotal=subtotal, order_type_preview=order_type_preview)


def merge_guest_cart_into_user(db: Session, user: User, session_id: Optional[str]) -> None:
    """
    Mehmon sifatida (X-Session-Id orqali) yig'ilgan savatni, login qilingandan so'ng
    foydalanuvchining shaxsiy savatiga birlashtiradi. Miqdorlar qo'shiladi va narx
    calculate_unit_price orqali qayta hisoblanadi (chunki miqdor o'zgarishi optom
    bosqichga ta'sir qilishi mumkin).
    """
    if not session_id:
        return
    guest_cart = db.query(Cart).filter(Cart.session_id == session_id).first()
    if not guest_cart or not guest_cart.items:
        return

    user_cart = db.query(Cart).filter(Cart.user_id == user.id).first()
    if not user_cart:
        user_cart = Cart(user_id=user.id)
        db.add(user_cart)
        db.flush()

    for guest_item in list(guest_cart.items):
        variant = db.query(ProductVariant).get(guest_item.variant_id)
        if not variant or not variant.price:
            continue
        existing = next((i for i in user_cart.items if i.variant_id == guest_item.variant_id), None)
        quantity = (existing.quantity if existing else 0) + guest_item.quantity
        result = calculate_unit_price(variant.price, variant.price_tiers, quantity)
        if existing:
            existing.quantity = quantity
            existing.price_type = result.price_type
            existing.unit_price_snapshot = result.unit_price
        else:
            db.add(CartItem(
                cart_id=user_cart.id, variant_id=guest_item.variant_id,
                quantity=quantity, price_type=result.price_type,
                unit_price_snapshot=result.unit_price,
            ))

    db.delete(guest_cart)
    db.commit()


@router.get("", response_model=CartOut)
def get_cart(
    user: Optional[User] = Depends(_current_user_optional),
    x_session_id: Optional[str] = Header(default=None),
    db: Session = Depends(get_db),
):
    cart = _get_or_create_cart(db, user, x_session_id)
    return _serialize_cart(cart)


@router.post("/items", response_model=CartOut)
def add_item(
    payload: CartItemCreate,
    user: Optional[User] = Depends(_current_user_optional),
    x_session_id: Optional[str] = Header(default=None),
    db: Session = Depends(get_db),
):
    variant = db.query(ProductVariant).get(payload.variant_id)
    if not variant or not variant.price:
        raise HTTPException(status_code=404, detail="Variant yoki uning narxi topilmadi")

    cart = _get_or_create_cart(db, user, x_session_id)

    existing = next((i for i in cart.items if i.variant_id == payload.variant_id), None)
    quantity = (existing.quantity if existing else 0) + payload.quantity

    result = calculate_unit_price(variant.price, variant.price_tiers, quantity)

    if existing:
        existing.quantity = quantity
        existing.price_type = result.price_type
        existing.unit_price_snapshot = result.unit_price
    else:
        db.add(CartItem(
            cart_id=cart.id,
            variant_id=payload.variant_id,
            quantity=quantity,
            price_type=result.price_type,
            unit_price_snapshot=result.unit_price,
        ))

    db.commit()
    db.refresh(cart)
    return _serialize_cart(cart)


@router.put("/items/{item_id}", response_model=CartOut)
def update_item(
    item_id: int,
    payload: CartItemCreate,
    user: Optional[User] = Depends(_current_user_optional),
    x_session_id: Optional[str] = Header(default=None),
    db: Session = Depends(get_db),
):
    cart = _get_or_create_cart(db, user, x_session_id)
    item = next((i for i in cart.items if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Savat elementi topilmadi")

    variant = db.query(ProductVariant).get(item.variant_id)
    result = calculate_unit_price(variant.price, variant.price_tiers, payload.quantity)

    item.quantity = payload.quantity
    item.price_type = result.price_type
    item.unit_price_snapshot = result.unit_price

    db.commit()
    db.refresh(cart)
    return _serialize_cart(cart)


@router.delete("/items/{item_id}", response_model=CartOut)
def remove_item(
    item_id: int,
    user: Optional[User] = Depends(_current_user_optional),
    x_session_id: Optional[str] = Header(default=None),
    db: Session = Depends(get_db),
):
    cart = _get_or_create_cart(db, user, x_session_id)
    item = next((i for i in cart.items if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Savat elementi topilmadi")

    db.delete(item)
    db.commit()
    db.refresh(cart)
    return _serialize_cart(cart)
