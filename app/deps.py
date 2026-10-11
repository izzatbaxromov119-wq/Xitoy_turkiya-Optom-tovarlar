from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, RoleEnum
from app.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Kirish uchun token yaroqsiz yoki muddati o'tgan",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        raise credentials_error

    payload = decode_token(token)
    if not payload or payload.get("type") != "access":
        raise credentials_error

    user_id = payload.get("sub")
    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user or not user.is_active:
        raise credentials_error
    return user


def require_roles(*allowed_roles: RoleEnum):
    """
    RBAC dependency generator.
    Foydalanish: Depends(require_roles(RoleEnum.admin, RoleEnum.super_admin))
    """

    def checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Bu amal uchun sizda yetarli huquq yo'q",
            )
        return current_user

    return checker


# Tez-tez ishlatiladigan rol guruhlari (TZ'dagi RBAC sxemasiga mos)
require_admin = require_roles(RoleEnum.super_admin, RoleEnum.admin)
require_operator = require_roles(RoleEnum.super_admin, RoleEnum.admin, RoleEnum.operator)
require_warehouse = require_roles(RoleEnum.super_admin, RoleEnum.admin, RoleEnum.warehouse_operator)
