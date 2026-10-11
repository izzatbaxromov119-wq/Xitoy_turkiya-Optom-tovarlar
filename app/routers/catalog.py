import os
import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session, joinedload

from app.config import settings
from app.database import get_db
from app.deps import require_admin
from app.models import Category, Product, ProductVariant, Price, PriceTier, ProductStatus, GenderEnum
from app.schemas import (
    CategoryCreate, CategoryOut, ProductCreate, ProductOut,
    VariantCreate, VariantOut, PriceIn, PriceOut, PriceTierIn, PriceTierOut,
)

router = APIRouter(prefix="/api", tags=["Katalog"])

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}
MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB


# ---------------------------- Kategoriyalar ----------------------------

@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).order_by(Category.sort_order).all()


@router.post("/admin/categories", response_model=CategoryOut, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(require_admin)])
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    if db.query(Category).filter(Category.slug == payload.slug).first():
        raise HTTPException(status_code=400, detail="Bu slug band")
    category = Category(**payload.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.put("/admin/categories/{category_id}", response_model=CategoryOut,
            dependencies=[Depends(require_admin)])
def update_category(category_id: int, payload: CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Category).get(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Kategoriya topilmadi")
    for field, value in payload.model_dump().items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category


@router.delete("/admin/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(require_admin)])
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).get(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Kategoriya topilmadi")
    db.delete(category)
    db.commit()


# ---------------------------- Mahsulotlar ----------------------------

@router.get("/products", response_model=list[ProductOut])
def list_products(
    category_id: Optional[int] = None,
    gender: Optional[GenderEnum] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Product).options(
        joinedload(Product.variants).joinedload(ProductVariant.price),
        joinedload(Product.variants).joinedload(ProductVariant.price_tiers),
    ).filter(Product.status == ProductStatus.active)

    if category_id:
        query = query.filter(Product.category_id == category_id)
    if gender:
        query = query.join(Category).filter(Category.gender == gender)

    return query.all()


@router.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).options(
        joinedload(Product.variants).joinedload(ProductVariant.price),
        joinedload(Product.variants).joinedload(ProductVariant.price_tiers),
    ).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    return product


@router.post("/admin/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(require_admin)])
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    if not db.query(Category).get(payload.category_id):
        raise HTTPException(status_code=400, detail="Kategoriya topilmadi")
    product = Product(**payload.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.put("/admin/products/{product_id}", response_model=ProductOut,
            dependencies=[Depends(require_admin)])
def update_product(product_id: int, payload: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    for field, value in payload.model_dump().items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


@router.delete("/admin/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(require_admin)])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    db.delete(product)
    db.commit()


@router.post("/admin/products/{product_id}/image", response_model=ProductOut,
             dependencies=[Depends(require_admin)])
async def upload_product_image(product_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Mahsulotga HAQIQIY surat yuklash. Bu yerga faqat sizning o'z mahsulotlaringizning
    (ta'minotchidan olingan yoki o'zingiz suratga olgan) rasmlarini yuklang — boshqa
    saytlardan olingan tovar suratlarini emas (mualliflik huquqi).

    Rasm yuklanmagan mahsulotlar frontendda avtomatik ikonka bilan ko'rsatiladi.
    """
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Faqat JPEG, PNG, WEBP yoki GIF fayllar qabul qilinadi")

    contents = await file.read()
    if len(contents) > MAX_IMAGE_SIZE_BYTES:
        raise HTTPException(status_code=400, detail="Rasm hajmi 5 MB dan oshmasligi kerak")

    ext = os.path.splitext(file.filename or "")[1].lower() or ".jpg"
    if ext not in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
        ext = ".jpg"
    filename = f"product-{product_id}-{uuid.uuid4().hex[:10]}{ext}"

    os.makedirs(settings.upload_dir, exist_ok=True)
    filepath = os.path.join(settings.upload_dir, filename)
    with open(filepath, "wb") as f:
        f.write(contents)

    product.image_url = f"/uploads/{filename}"
    db.commit()
    db.refresh(product)
    return product


# ---------------------------- Variantlar ----------------------------

@router.post("/admin/products/{product_id}/variants", response_model=VariantOut,
             status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_admin)])
def create_variant(product_id: int, payload: VariantCreate, db: Session = Depends(get_db)):
    if not db.query(Product).get(product_id):
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")
    if db.query(ProductVariant).filter(ProductVariant.sku == payload.sku).first():
        raise HTTPException(status_code=400, detail="Bu SKU band")

    variant = ProductVariant(product_id=product_id, **payload.model_dump())
    db.add(variant)
    db.commit()
    db.refresh(variant)
    return variant


# ---------------------------- Narxlash ----------------------------

@router.put("/admin/variants/{variant_id}/price", response_model=PriceOut,
            dependencies=[Depends(require_admin)])
def set_price(variant_id: int, payload: PriceIn, db: Session = Depends(get_db)):
    variant = db.query(ProductVariant).get(variant_id)
    if not variant:
        raise HTTPException(status_code=404, detail="Variant topilmadi")

    price = db.query(Price).filter(Price.variant_id == variant_id).first()
    if price:
        for field, value in payload.model_dump().items():
            setattr(price, field, value)
    else:
        price = Price(variant_id=variant_id, **payload.model_dump())
        db.add(price)

    db.commit()
    db.refresh(price)
    return price


@router.post("/admin/variants/{variant_id}/price-tiers", response_model=PriceTierOut,
             status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_admin)])
def add_price_tier(variant_id: int, payload: PriceTierIn, db: Session = Depends(get_db)):
    if not db.query(ProductVariant).get(variant_id):
        raise HTTPException(status_code=404, detail="Variant topilmadi")

    tier = PriceTier(variant_id=variant_id, **payload.model_dump())
    db.add(tier)
    db.commit()
    db.refresh(tier)
    return tier
