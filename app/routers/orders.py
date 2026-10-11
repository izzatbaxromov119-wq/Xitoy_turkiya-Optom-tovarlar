import uuid
from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.deps import get_current_user, require_operator
from app.models import (
    Cart, Order, OrderItem, Inventory, Warehouse, User,
    OrderStatus, OrderType, DeliveryTypeEnum, WarehouseType,
)
from app.pricing import determine_order_type
from app.schemas import CheckoutRequest, OrderOut, OrderStatusUpdate

router = APIRouter(prefix="/api", tags=["Buyurtmalar"])


def _generate_order_number() -> str:
    return f"ORD-{uuid.uuid4().hex[:10].upper()}"


def _default_warehouse(db: Session) -> Optional[Warehouse]:
    return db.query(Warehouse).filter(Warehouse.type == WarehouseType.main_warehouse).first()


@router.post("/orders", response_model=OrderOut)
def checkout(payload: CheckoutRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.user_id == current_user.id).first()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Savat bo'sh")

    warehouse = None
    if payload.warehouse_id:
        warehouse = db.query(Warehouse).get(payload.warehouse_id)
    if not warehouse:
        warehouse = _default_warehouse(db)
    if not warehouse:
        raise HTTPException(status_code=400, detail="Faol ombor topilmadi. Avval ombor yarating.")

    # Qoldiqni tekshirish va band qilish (available -> reserved)
    for item in cart.items:
        inv = db.query(Inventory).filter(
            Inventory.variant_id == item.variant_id,
            Inventory.warehouse_id == warehouse.id,
        ).first()
        if not inv or inv.quantity_available < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Variant #{item.variant_id} uchun omborda yetarli qoldiq yo'q",
            )

    try:
        delivery_type_value = DeliveryTypeEnum(payload.delivery_type)
    except ValueError:
        raise HTTPException(status_code=400, detail="delivery_type 'courier' yoki 'post' bo'lishi kerak")

    order = Order(
        order_number=_generate_order_number(),
        user_id=current_user.id,
        status=OrderStatus.new,
        order_type=OrderType(determine_order_type([i.price_type for i in cart.items])),
        delivery_type=delivery_type_value,
        delivery_address_id=payload.delivery_address_id,
        warehouse_id=warehouse.id,
    )
    db.add(order)
    db.flush()  # order.id kerak bo'ladi

    total = Decimal("0")
    for item in cart.items:
        line_total = item.unit_price_snapshot * item.quantity
        total += line_total
        db.add(OrderItem(
            order_id=order.id,
            variant_id=item.variant_id,
            quantity=item.quantity,
            price_type=item.price_type,
            unit_price=item.unit_price_snapshot,
            total_price=line_total,
        ))

        inv = db.query(Inventory).filter(
            Inventory.variant_id == item.variant_id,
            Inventory.warehouse_id == warehouse.id,
        ).first()
        inv.quantity_available -= item.quantity
        inv.quantity_reserved += item.quantity

    order.total_amount = total

    for item in list(cart.items):
        db.delete(item)

    db.commit()
    db.refresh(order)
    return order


@router.get("/orders", response_model=list[OrderOut])
def my_orders(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Order).options(joinedload(Order.items)).filter(
        Order.user_id == current_user.id
    ).order_by(Order.created_at.desc()).all()


@router.get("/orders/{order_id}", response_model=OrderOut)
def get_order(order_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    order = db.query(Order).options(joinedload(Order.items)).get(order_id)
    if not order or (order.user_id != current_user.id and current_user.role.value == "customer"):
        raise HTTPException(status_code=404, detail="Buyurtma topilmadi")
    return order


@router.post("/orders/{order_id}/cancel", response_model=OrderOut)
def cancel_order(order_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    order = db.query(Order).get(order_id)
    if not order or order.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Buyurtma topilmadi")
    if order.status in (OrderStatus.shipped, OrderStatus.delivered):
        raise HTTPException(status_code=400, detail="Jo'natilgan buyurtmani bekor qilib bo'lmaydi")

    # Band qilingan qoldiqni qaytarish (reserved -> available)
    for item in order.items:
        inv = db.query(Inventory).filter(
            Inventory.variant_id == item.variant_id,
            Inventory.warehouse_id == order.warehouse_id,
        ).first()
        if inv:
            inv.quantity_reserved = max(0, inv.quantity_reserved - item.quantity)
            inv.quantity_available += item.quantity

    order.status = OrderStatus.canceled
    db.commit()
    db.refresh(order)
    return order


# ---------------------------- Admin ----------------------------

@router.get("/admin/orders", response_model=list[OrderOut], dependencies=[Depends(require_operator)])
def admin_list_orders(status: Optional[str] = None, order_type: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Order).options(joinedload(Order.items))
    if status:
        query = query.filter(Order.status == status)
    if order_type:
        query = query.filter(Order.order_type == order_type)
    return query.order_by(Order.created_at.desc()).all()


@router.put("/admin/orders/{order_id}/status", response_model=OrderOut, dependencies=[Depends(require_operator)])
def admin_update_status(order_id: int, payload: OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Buyurtma topilmadi")

    try:
        new_status = OrderStatus(payload.status)
    except ValueError:
        valid = ", ".join(s.value for s in OrderStatus)
        raise HTTPException(status_code=400, detail=f"Noto'g'ri status qiymati. Mumkin bo'lganlar: {valid}")

    # Jo'natilganda: band qilingan qoldiq real chiqim bo'ladi (reserved -> 0)
    if new_status == OrderStatus.shipped and order.status != OrderStatus.shipped:
        for item in order.items:
            inv = db.query(Inventory).filter(
                Inventory.variant_id == item.variant_id,
                Inventory.warehouse_id == order.warehouse_id,
            ).first()
            if inv:
                inv.quantity_reserved = max(0, inv.quantity_reserved - item.quantity)

    order.status = new_status
    db.commit()
    db.refresh(order)
    return order
