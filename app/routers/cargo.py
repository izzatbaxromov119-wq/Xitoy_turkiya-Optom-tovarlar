from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import require_admin, require_warehouse, require_operator, get_current_user
from app.models import CargoBatch, Delivery, DeliveryStatus, CargoStatus, Courier, User, RoleEnum
from app.schemas import CargoBatchCreate, CargoBatchOut, TrackingOut

router = APIRouter(prefix="/api", tags=["Kargo va yetkazib berish"])


@router.get("/tracking/{tracking_number}", response_model=TrackingOut)
def track(tracking_number: str, db: Session = Depends(get_db)):
    delivery = db.query(Delivery).filter(Delivery.tracking_number == tracking_number).first()
    if not delivery:
        raise HTTPException(status_code=404, detail="Bunday tracking raqam topilmadi")
    return TrackingOut(
        tracking_number=delivery.tracking_number,
        status=delivery.status.value,
        delivery_method=delivery.delivery_method.value,
        region=delivery.region,
        delivered_at=delivery.delivered_at,
    )


@router.post("/admin/cargo-batches", response_model=CargoBatchOut, dependencies=[Depends(require_admin)])
def create_cargo_batch(payload: CargoBatchCreate, db: Session = Depends(get_db)):
    if db.query(CargoBatch).filter(CargoBatch.batch_number == payload.batch_number).first():
        raise HTTPException(status_code=400, detail="Bu partiya raqami band")
    batch = CargoBatch(**payload.model_dump())
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return batch


@router.put("/admin/cargo-batches/{batch_id}/status", response_model=CargoBatchOut,
            dependencies=[Depends(require_warehouse)])
def update_cargo_status(batch_id: int, new_status: str, db: Session = Depends(get_db)):
    batch = db.query(CargoBatch).get(batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Kargo partiyasi topilmadi")
    try:
        batch.status = CargoStatus(new_status)
    except ValueError:
        valid = ", ".join(s.value for s in CargoStatus)
        raise HTTPException(status_code=400, detail=f"Noto'g'ri status qiymati. Mumkin bo'lganlar: {valid}")
    db.commit()
    db.refresh(batch)
    return batch


@router.post("/admin/deliveries/{delivery_id}/assign-courier", dependencies=[Depends(require_operator)])
def assign_courier(delivery_id: int, courier_id: int, db: Session = Depends(get_db)):
    delivery = db.query(Delivery).get(delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Yetkazib berish topilmadi")
    delivery.courier_id = courier_id
    db.commit()
    return {"detail": "Kuryer biriktirildi"}


@router.put("/admin/deliveries/{delivery_id}/status")
def update_delivery_status(
    delivery_id: int, new_status: str,
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db),
):
    """
    RBAC: operator/admin/super_admin — istalgan yetkazib berishni yangilay oladi.
    Kuryer — FAQAT o'ziga biriktirilgan yetkazib berishni yangilay oladi (obyekt darajasidagi tekshiruv).
    """
    delivery = db.query(Delivery).get(delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Yetkazib berish topilmadi")

    allowed_roles = {RoleEnum.super_admin, RoleEnum.admin, RoleEnum.operator}
    if current_user.role not in allowed_roles:
        if current_user.role == RoleEnum.courier:
            own_courier = db.query(Courier).filter(Courier.user_id == current_user.id).first()
            if not own_courier or delivery.courier_id != own_courier.id:
                raise HTTPException(status_code=403, detail="Faqat o'zingizga biriktirilgan yetkazib berishni yangilay olasiz")
        else:
            raise HTTPException(status_code=403, detail="Bu amal uchun sizda yetarli huquq yo'q")

    try:
        delivery.status = DeliveryStatus(new_status)
    except ValueError:
        valid = ", ".join(s.value for s in DeliveryStatus)
        raise HTTPException(status_code=400, detail=f"Noto'g'ri status qiymati. Mumkin bo'lganlar: {valid}")
    db.commit()
    return {"detail": "Status yangilandi"}
