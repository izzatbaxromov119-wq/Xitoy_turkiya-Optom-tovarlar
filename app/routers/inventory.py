from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import require_warehouse
from app.models import Inventory, StockMovement, MovementType, User
from app.schemas import (
    InventoryOut, StockInRequest, StockTransferRequest, WarehouseOut,
)
from app.models import Warehouse

router = APIRouter(prefix="/api/admin", tags=["Ombor"])


def _get_or_create_inventory(db: Session, variant_id: int, warehouse_id: int) -> Inventory:
    inv = db.query(Inventory).filter(
        Inventory.variant_id == variant_id, Inventory.warehouse_id == warehouse_id
    ).first()
    if not inv:
        inv = Inventory(variant_id=variant_id, warehouse_id=warehouse_id)
        db.add(inv)
        db.flush()
    return inv


@router.get("/warehouses", response_model=list[WarehouseOut], dependencies=[Depends(require_warehouse)])
def list_warehouses(db: Session = Depends(get_db)):
    return db.query(Warehouse).all()


@router.get("/inventory", response_model=list[InventoryOut], dependencies=[Depends(require_warehouse)])
def list_inventory(warehouse_id: Optional[int] = None, variant_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(Inventory)
    if warehouse_id:
        query = query.filter(Inventory.warehouse_id == warehouse_id)
    if variant_id:
        query = query.filter(Inventory.variant_id == variant_id)
    return query.all()


@router.get("/inventory/low-stock", response_model=list[InventoryOut], dependencies=[Depends(require_warehouse)])
def low_stock(db: Session = Depends(get_db)):
    items = db.query(Inventory).all()
    return [i for i in items if i.quantity_available <= i.min_stock_alert]


@router.post("/inventory/stock-in", response_model=InventoryOut, dependencies=[Depends(require_warehouse)])
def stock_in(payload: StockInRequest, current_user: User = Depends(require_warehouse), db: Session = Depends(get_db)):
    inv = _get_or_create_inventory(db, payload.variant_id, payload.warehouse_id)
    inv.quantity_available += payload.quantity

    db.add(StockMovement(
        variant_id=payload.variant_id,
        warehouse_id=payload.warehouse_id,
        movement_type=MovementType.income,
        quantity=payload.quantity,
        cargo_batch_id=payload.cargo_batch_id,
        created_by=current_user.id,
    ))
    db.commit()
    db.refresh(inv)
    return inv


@router.post("/inventory/transfer", dependencies=[Depends(require_warehouse)])
def transfer(payload: StockTransferRequest, current_user: User = Depends(require_warehouse), db: Session = Depends(get_db)):
    source = _get_or_create_inventory(db, payload.variant_id, payload.from_warehouse_id)
    if source.quantity_available < payload.quantity:
        raise HTTPException(status_code=400, detail="Manba omborda yetarli qoldiq yo'q")

    destination = _get_or_create_inventory(db, payload.variant_id, payload.to_warehouse_id)

    source.quantity_available -= payload.quantity
    destination.quantity_available += payload.quantity

    db.add(StockMovement(
        variant_id=payload.variant_id, warehouse_id=payload.from_warehouse_id,
        movement_type=MovementType.transfer, quantity=-payload.quantity, created_by=current_user.id,
    ))
    db.add(StockMovement(
        variant_id=payload.variant_id, warehouse_id=payload.to_warehouse_id,
        movement_type=MovementType.transfer, quantity=payload.quantity, created_by=current_user.id,
    ))

    db.commit()
    return {"detail": "Tovar muvaffaqiyatli ko'chirildi", "from": source.warehouse_id, "to": destination.warehouse_id}
