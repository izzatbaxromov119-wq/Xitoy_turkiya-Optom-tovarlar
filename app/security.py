import datetime
from typing import Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)


def _create_token(subject: str, expires_delta: datetime.timedelta, token_type: str, extra: Optional[dict] = None) -> str:
    now = datetime.datetime.utcnow()
    payload = {
        "sub": subject,
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def create_access_token(user_id: int, role: str) -> str:
    return _create_token(
        subject=str(user_id),
        expires_delta=datetime.timedelta(minutes=settings.access_token_expire_minutes),
        token_type="access",
        extra={"role": role},
    )


def create_refresh_token(user_id: int) -> str:
    return _create_token(
        subject=str(user_id),
        expires_delta=datetime.timedelta(days=settings.refresh_token_expire_days),
        token_type="refresh",
    )


def decode_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError:
        return None
