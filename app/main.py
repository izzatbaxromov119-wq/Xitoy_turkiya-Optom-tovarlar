import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.database import Base, engine, SessionLocal
from app.admin import register_admin
from app.routers import auth, catalog, cart, orders, inventory, cargo, extras
from app.models import Product

# Rivojlantirish uchun: jadvallarni avtomatik yaratish.
# Production muhitida buning o'rniga Alembic migratsiyalaridan foydalaning.
Base.metadata.create_all(bind=engine)

# Baza bo'sh bo'lsa (masalan, optom_market.db fayli hali seed qilinmagan bo'lsa),
# do'kon "0 ta mahsulot" ko'rinishida jim turib qolmasligi uchun konsolga aniq ogohlantirish
# chiqaramiz — aks holda bu xato tashqi ko'rinishda "nosoz sayt"dek ko'rinadi, aslida esa
# shunchaki `python seed.py` ishga tushirilmagan bo'ladi.
with SessionLocal() as _startup_db:
    if _startup_db.query(Product).first() is None:
        print(
            "\n"
            "!!! DIQQAT: bazada mahsulotlar topilmadi (optom_market.db bo'sh yoki hali seed "
            "qilinmagan).\n"
            "    Do'kon sahifasi '0 ta mahsulot' ko'rinishida ochiladi.\n"
            "    Buni tuzatish uchun serverni to'xtatib, quyidagini ishga tushiring:\n"
            "        python seed.py\n"
            "    So'ng serverni qayta ishga tushiring.\n"
        )

app = FastAPI(
    title=settings.app_name,
    description="Xitoy va Turkiyadan import qilinadigan kiyim-kechak va aksessuarlarni "
                "dona hamda optom shaklda sotuvchi internet do'kon uchun backend API.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origins] if settings.cors_origins != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLAdmin panel sessiya orqali autentifikatsiya qiladi
app.add_middleware(SessionMiddleware, secret_key=settings.admin_secret_key)

app.include_router(auth.router)
app.include_router(catalog.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(inventory.router)
app.include_router(cargo.router)
app.include_router(extras.router)

register_admin(app)

# Admin panel/API orqali yuklangan haqiqiy mahsulot suratlari shu yo'ldan xizmat qiladi
os.makedirs(settings.upload_dir, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.upload_dir), name="uploads")


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(LookupError)
async def lookup_error_handler(request: Request, exc: LookupError):
    return JSONResponse(status_code=400, content={"detail": "Noto'g'ri qiymat yuborildi"})


FRONTEND_INDEX = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")


@app.get("/", tags=["Frontend"])
def serve_frontend():
    """
    Do'kon frontendi — alohida .html fayldan xizmat qilinadi (Python satr ichiga
    joylashtirilmagan), shu bilan qochirish/escaping xatolaridan butunlay xoli.

    Cache-Control: no-store — bu sahifa tez-tez yangilanadigan loyiha bo'lgani uchun,
    brauzer uni eskirgan (keshlangan) holda ko'rsatib, "yangi funksiyalar ko'rinmayapti"
    kabi chalkashliklarga sabab bo'lmasligi uchun har doim serverdan yangi nusxa olinadi.
    """
    return FileResponse(
        FRONTEND_INDEX,
        media_type="text/html",
        headers={"Cache-Control": "no-store, no-cache, must-revalidate"},
    )


@app.get("/api/status", tags=["Xizmat holati"])
def status_check():
    return {
        "service": settings.app_name,
        "status": "ok",
        "docs": "/docs",
        "admin_panel": "/admin",
        "frontend": "/",
    }
