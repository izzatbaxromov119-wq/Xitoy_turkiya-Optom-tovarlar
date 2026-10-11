from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models import User, UserAddress
from app.routers.cart import merge_guest_cart_into_user
from app.schemas import (
    UserRegister, UserLogin, TokenPair, RefreshRequest, UserOut,
    UserAddressCreate, UserAddressOut,
)
from app.security import hash_password, verify_password, create_access_token, create_refresh_token, decode_token

router = APIRouter(prefix="/api/auth", tags=["Autentifikatsiya"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserRegister, x_session_id: Optional[str] = Header(default=None), db: Session = Depends(get_db)):
    if db.query(User).filter(User.phone == payload.phone).first():
        raise HTTPException(status_code=400, detail="Bu telefon raqami allaqachon ro'yxatdan o'tgan")
    if payload.email and db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Bu email allaqachon ro'yxatdan o'tgan")

    user = User(
        full_name=payload.full_name,
        phone=payload.phone,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    merge_guest_cart_into_user(db, user, x_session_id)
    return user


@router.post("/login", response_model=TokenPair)
def login(payload: UserLogin, x_session_id: Optional[str] = Header(default=None), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == payload.phone).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Telefon raqami yoki parol noto'g'ri")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Hisob faol emas")

    # Login'dan oldin mehmon sifatida (X-Session-Id orqali) yig'ilgan savat bo'lsa,
    # uni foydalanuvchining shaxsiy savatiga birlashtiramiz.
    merge_guest_cart_into_user(db, user, x_session_id)

    return TokenPair(
        access_token=create_access_token(user.id, user.role.value),
        refresh_token=create_refresh_token(user.id),
    )


@router.post("/refresh", response_model=TokenPair)
def refresh(payload: RefreshRequest, db: Session = Depends(get_db)):
    data = decode_token(payload.refresh_token)
    if not data or data.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Refresh token yaroqsiz")

    user = db.query(User).filter(User.id == int(data["sub"])).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Foydalanuvchi topilmadi")

    return TokenPair(
        access_token=create_access_token(user.id, user.role.value),
        refresh_token=create_refresh_token(user.id),
    )


@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/me/addresses", response_model=list[UserAddressOut])
def list_addresses(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(UserAddress).filter(UserAddress.user_id == current_user.id).all()


@router.post("/me/addresses", response_model=UserAddressOut, status_code=status.HTTP_201_CREATED)
def add_address(payload: UserAddressCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    address = UserAddress(user_id=current_user.id, **payload.model_dump())
    db.add(address)
    db.commit()
    db.refresh(address)
    return address
