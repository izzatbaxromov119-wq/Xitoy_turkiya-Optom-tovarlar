# OPTOM MARKET — To'liq ishlaydigan backend + frontend (FastAPI)

Xitoy va Turkiyadan import qilinadigan kiyim-kechak, ich kiyim, oyoq kiyim va aksessuarlarni
**dona hamda optom** shaklda sotuvchi internet do'kon uchun **to'liq ishlaydigan** tizim.

Bu loyiha TZ hujjatidagi arxitekturaning haqiqiy dasturiy ko'rinishi: JWT autentifikatsiya,
RBAC, dona/optom narxlash algoritmi, savat (mehmon + login qilingan), buyurtma, ombor qoldig'i
boshqaruvi, kargo/tracking, to'liq ishlaydigan **admin panel** — va ularning barchasiga ulangan,
haqiqatda ishlaydigan **do'kon frontendi**, bittasi ikkinchisiga qaram bo'lmagan holda bir xil
FastAPI ilovasi orqali xizmat qiladi (`python -m uvicorn app.main:app` — bittagina buyruq).

---

## 1. Tezkor ishga tushirish

```bash
# 1) Virtual muhit (tavsiya etiladi)
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2) Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 3) .env faylini yaratish
cp .env.example .env
# .env ichidagi SECRET_KEY va ADMIN_SECRET_KEY ni albatta o'zgartiring

# 4) Demo ma'lumotlar bilan bazani to'ldirish (SQLite avtomatik yaratiladi)
python seed.py

# 5) Serverni ishga tushirish
uvicorn app.main:app --reload
```

Ishga tushgach, brauzeringizda **http://127.0.0.1:8000/** manzilini oching — to'liq ishlaydigan
do'kon darhol ochiladi (kategoriyalar, 160 mahsulot, savat, checkout, kargo tracking).

| Manzil | Tavsif |
|---|---|
| **http://127.0.0.1:8000/** | **Do'kon (frontend)** — katalog, savat, buyurtma, tracking |
| http://127.0.0.1:8000/admin | **Admin panel** |
| http://127.0.0.1:8000/docs | Avtomatik Swagger API hujjati |
| http://127.0.0.1:8000/api/status | Xizmat holati (JSON) |

### Tayyor test hisoblari (seed.py orqali yaratilgan)

| Rol | Telefon | Parol |
|---|---|---|
| Super Admin | `+998900000001` | `Admin12345` |
| Admin | `+998900000003` | `Admin12345` |
| Operator | `+998900000004` | `Operator12345` |
| Omborchi | `+998900000002` | `Manager12345` |
| Kuryer | `+998901110001` | `Courier12345` |
| Ro'yxatdan o'tgan mijoz | `+998901234567` | `Customer123` |
| **Optom mijoz** | `+998907778899` | `Wholesale123` |

Do'kon sahifasidagi login oynasida shu barcha rollar uchun **bir bosishda to'ldiriladigan
tugmalar** bor — birortasini eslab qolishning hojati yo'q.

Demo tracking raqami (Kargo tracking bo'limida sinab ko'ring): **`OM-DEMO-0001-TRK`**

> ⚠️ **Muhim:** yuqoridagi **4-qadam (`python seed.py`) albatta bajarilishi shart.**
> `optom_market.db` fayli arxivga **qo'shilmagan** (demo baza faylini tarqatish o'rniga,
> har doim bir xil, ishonchli natija berishi uchun u skript orqali generatsiya qilinadi).
> Agar `seed.py`ni ishga tushirmasdan to'g'ridan-to'g'ri `uvicorn`ni ishga tushirsangiz,
> FastAPI bo'sh jadvallar bilan yangi `optom_market.db` yaratadi va do'kon sahifasida
> **"0 ta mahsulot / 0 ta toifa"** ko'rinadi — bu xato emas, shunchaki baza hali
> to'ldirilmagan. (Serverni shu holatda ishga tushirsangiz, konsolda aniq ogohlantirish
> chiqadi va nima qilish kerakligini ko'rsatadi.) Tuzatish uchun: serverni to'xtating →
> `python seed.py` → serverni qayta ishga tushiring.
>
> `seed.py` to'g'ri ishlasa, baza **8 ta kategoriya (ayollar, erkaklar, bolalar,
> chaqaloqlar, ich kiyim, oyoq kiyim, sumkalar, bosh kiyimlar), 160 ta mahsulot (~480
> variant, har kategoriyada 20 tadan), 2 ta tayyor buyurtma va kargo tracking yozuvlari**
> bilan to'ladi.

---

## 2. Loyiha tuzilishi

```
optom-market-backend/
├── app/
│   ├── main.py            # FastAPI ilova: routerlar, admin va frontend shu yerda ulanadi
│   ├── config.py          # .env dan o'qiladigan sozlamalar
│   ├── database.py        # SQLAlchemy engine/session
│   ├── models.py          # TZ dagi DB sxemasiga mos barcha jadvallar
│   ├── schemas.py         # Pydantic request/response modellari
│   ├── security.py        # Parol xeshlash + JWT yaratish/tekshirish
│   ├── deps.py             # get_current_user va RBAC (require_roles) dependency'lari
│   ├── pricing.py          # Dona/optom narx hisoblash algoritmi (TZ 04-bo'lim)
│   ├── admin.py            # SQLAdmin: to'liq CRUD admin panel + login
│   └── routers/
│       ├── auth.py         # Ro'yxatdan o'tish, login (+ mehmon savatini birlashtirish), profil
│       ├── catalog.py      # Kategoriya, mahsulot, variant, narx CRUD
│       ├── cart.py         # Savat + real-time narx hisoblash + mehmon savati mexanizmi
│       ├── orders.py       # Checkout, buyurtmalar, status boshqaruvi
│       ├── inventory.py    # Ombor qoldig'i: stock-in, transfer, low-stock
│       └── cargo.py        # Kargo partiyasi, tracking, yetkazib berish
├── frontend/
│   └── index.html          # Haqiqiy do'kon frontendi — alohida .html fayl (Python satr ICHIDA
│                            #  EMAS — shu orqali "\'" kabi escaping xatolaridan butunlay xoli),
│                            #  faqat vanilla JS + fetch() bilan yozilgan, hech qanday
│                            #  qo'shimcha frontend kutubxonasi/build jarayoni talab qilmaydi.
├── seed.py                 # Demo ma'lumotlar generatori (baza to'ldirish uchun)
├── catalog_data.py         # 8 kategoriya / 160 mahsulot / 480 variantlik katalog ma'lumotlari
├── requirements.txt
├── .env.example
└── README.md
```

---

## 3. Dona/optom narxlash algoritmi qanday ishlaydi (Smart Pricing)

`app/pricing.py` ichida joylashgan. TZ talabiga ko'ra **barcha 160 mahsulot uchun bir xil,
standart 4-bosqichli chegaralar** qo'llaniladi:

| Miqdor | Bosqich nomi | Taxminiy chegirma |
|---|---|---|
| 1–4 dona | **Dona narx** | — (to'liq narx) |
| 5–19 dona | **Kichik optom** | ~15% |
| 20–49 dona | **Optom** | ~28% |
| 50+ dona | **Katta optom** | ~40% |

Algoritm mantiqi:
1. Miqdor `wholesale_min_qty` (= har doim 5) dan kichik → **dona narx** (`retail_price`).
2. Miqdor yetarli → `price_tiers` ichidan miqdorga mos **eng yuqori bosqich** tanlanadi.
3. Mos bosqich topilmasa → bazaviy `wholesale_price`.
4. Natija `cart_items.unit_price_snapshot` ga yoziladi — admin keyinchalik narxni
   o'zgartirsa ham, mijozning mavjud savati/buyurtmasi ta'sirlanmaydi.

`tier_label_for_quantity()` funksiyasi — shu 4 nomni (Dona narx / Kichik optom / Optom /
Katta optom) markazlashtirilgan holda qaytaradi; frontend ham xuddi shu chegaralarni
(`tierLabel()`) ishlatadi, shunday qilib backend va frontend hech qachon bir-biridan farq
qilmaydi.

**Muhim arxitektura qarori:** narx `client_type` (retail/wholesale) emas, balki bevosita
**miqdor**ga qarab tanlanadi — bu har qanday mijoz (hatto "Optom mijoz" deb belgilanmagan
oddiy mijoz ham) yetarli miqdor olsa optom narxdan foydalanishiga imkon beradi. "Optom
mijoz" roli (`client_type='wholesale'`, `is_wholesale_verified=True`) kelajakda qo'shimcha
imtiyozlar (masalan, min buyurtma talabisiz optom narx) uchun ishlatilishi mumkin.

Buni o'zingiz sinab ko'rishingiz mumkin: `/docs` orqali bir xil variantni turli miqdorda
(3, 5, 20, 50 dona) savatga qo'shib ko'ring — narx aniq shu jadvalga mos ravishda avtomatik
o'zgarganini ko'rasiz.

---

## 4. Ombor qoldig'i mexanizmi

Har bir `(variant, ombor)` juftligi uchun uchta holat kuzatiladi:

`quantity_available` → (buyurtma) → `quantity_reserved` → (jo'natildi) → chiqim

- **Checkout** (`POST /api/orders`) — `available` dan `reserved` ga o'tkazadi.
- **Status "shipped"** ga o'tganda (`PUT /api/admin/orders/{id}/status`) — `reserved`
  nolga tushadi, real chiqim hisoblanadi.
- **Bekor qilinganda** (`POST /api/orders/{id}/cancel`) — band qilingan miqdor
  qayta `available` ga qaytadi.
- **Stock-in** (`POST /api/admin/inventory/stock-in`) — kargo/ombor qabul qilishda
  `available` ga qo'shiladi, `stock_movements` jadvaliga audit yozuvi tushadi.

---

## 5. Frontend (`/`) va mehmon savati

`frontend/index.html` — hech qanday build jarayoni yoki tashqi frontend freymvorki talab
qilmaydigan, sof vanilla JS bilan yozilgan, haqiqiy backend API'siga ulangan do'kon sahifasi:

- Kategoriya bo'yicha filtr, 160 mahsulot, variant (o'lcham/rang) tanlash
- Miqdor o'zgarganda **dona → optom narx real vaqtda** ko'rsatiladi (frontendda darhol
  ko'rsatish uchun, lekin **haqiqiy hisob-kitob har doim serverda** — `unit_price_snapshot`
  orqali)
- **Mehmon savati**: login qilmasdan turib ham savatga mahsulot qo'shish mumkin
  (`X-Session-Id` sarlavhasi orqali brauzerda saqlanadigan noyob ID bilan)
- **Login qilinganda mehmon savati avtomatik foydalanuvchi savatiga ko'chadi**
  (`app/routers/cart.py` dagi `merge_guest_cart_into_user()` — miqdorlar qo'shiladi va
  narx qayta hisoblanadi, chunki yangi umumiy miqdor optom bosqichga tushishi mumkin)
- Checkout, "Buyurtmalarim", va **Kargo tracking** — barchasi haqiqiy endpointlarga ulangan
- **Mahsulot suratlari**: standart holatda har bir mahsulot o'zimiz chizgan, brendga mos
  SVG ikonka bilan ko'rsatiladi (mualliflik huquqisiz, tezkor, internetga bog'liq emas).
  Admin/Super Admin **"Rasmlar"** bo'limidan (yoki `/docs` orqali
  `POST /api/admin/products/{id}/image`) har bir mahsulotga **haqiqiy suratini** yuklashi
  mumkin — yuklangan rasm avtomatik ko'rsatiladi, rasm yo'q yoki yuklanishda xato bo'lsa
  ikonkaga qaytadi (`onerror` fallback, hech qachon bo'sh joy qolmaydi). Boshqa saytlardan
  olingan (mualliflik huquqi ostidagi) suratlarni yuklashdan saqlaning — faqat o'zingizning
  mahsulotlaringizning suratlarini yuklang.

---

## 6. Admin panel (`/admin`) va RBAC rollari

[SQLAdmin](https://aminalaee.github.io/sqladmin/) asosida qurilgan, quyidagilarni beradi:

- Foydalanuvchilar, manzillar
- Kategoriya, brend, mahsulot, variant
- Narx va optom bosqichlari
- Omborlar, qoldiq, ombor harakatlari logi
- Buyurtmalar, buyurtma qatorlari, to'lovlar, promo-kodlar
- Kargo partiyalari, kuryerlar, yetkazib berishlar

Kirish faqat `super_admin`, `admin`, `operator`, `warehouse_operator`
rollariga ruxsat etilgan (`app/admin.py` ichidagi `AdminAuth` klassi RBAC ni
avtomatik tekshiradi). `customer` va `courier` rollari bilan `/admin` panelga kirib bo'lmaydi.

### RBAC rol jadvali (TZ'ga to'liq mos)

| Rol | Kirish huquqi |
|---|---|
| **Mehmon** | Tizimda saqlanmaydi — token yo'q holat. Katalogni ko'rish, mehmon savati (`X-Session-Id`) |
| **Ro'yxatdan o'tgan mijoz** | `customer` + `client_type=retail`. Xarid, buyurtma tarixi |
| **Optom mijoz** | `customer` + `client_type=wholesale`. Xuddi shu huquqlar (narx miqdorga qarab avtomatik) |
| **Operator** | Buyurtmalarni ko'rish/status yangilash (`/api/admin/orders`), kuryer biriktirish, yetkazib berish holatini yangilash |
| **Omborchi** (`warehouse_operator`) | Ombor qoldig'i, stock-in/transfer, kargo qabul qilish |
| **Kuryer** | Faqat **o'ziga biriktirilgan** yetkazib berish holatini yangilash (obyekt darajasidagi tekshiruv) |
| **Admin** | To'liq boshqaruv: katalog, narx, foydalanuvchilar, buyurtmalar, ombor |
| **Super Admin** | Admin bilan bir xil + tizim darajasidagi sozlamalar |

---

## 7. Tekshirilgan (test qilingan) funksionallik

Ushbu loyiha bir necha bosqichda avtomatlashtirilgan tarzda test qilindi:

**Backend (API darajasida):**
- ✅ Ro'yxatdan o'tish / login / JWT access+refresh
- ✅ RBAC: `customer` admin endpointga kira olmaydi (403), tokensiz so'rov 401 qaytaradi
- ✅ Barcha 7 ta rol (Super Admin, Admin, Operator, Omborchi, Kuryer, Mijoz, Optom mijoz) muvaffaqiyatli login qiladi
- ✅ Operator buyurtmalarni boshqara oladi, lekin omborga kira olmaydi (to'g'ri ajratilgan)
- ✅ **Xavfsizlik tuzatishi tasdiqlandi**: avval himoyasiz bo'lgan `PUT /api/admin/deliveries/{id}/status`
  endpointi endi to'g'ri himoyalangan (tokensiz — 401, ruxsatsiz — 403)
- ✅ Standart 4-bosqichli narxlash: 3/5/19/20/49/50 dona uchun narx ANIQ jadvalga mos hisoblanadi
- ✅ Checkout: savatdan buyurtma yaratish + ombor bandlash (`available → reserved`)
- ✅ Status "shipped" ga o'tganda ombordan real chiqim (`reserved → 0`)
- ✅ Noto'g'ri qiymat yuborilganda (masalan yaroqsiz status) 500 emas, aniq 400 xabari
- ✅ Admin panel login sahifasi va CRUD view'lari

**Frontend + backend birgalikda (end-to-end, haqiqiy serverga haqiqiy `fetch()` so'rovlari bilan):**
- ✅ Bosh sahifa haqiqiy HTML frontendni qaytaradi
- ✅ 8 kategoriya, 160 mahsulot to'g'ri yuklanadi
- ✅ Mehmon savatga qo'shadi → login qiladi → **savat avtomatik ko'chadi** (birlashadi)
- ✅ 8 dona qo'shilganda narx avtomatik optom bosqichga o'tadi (82 000 so'm, to'g'ri hisoblandi)
- ✅ Checkout, buyurtmalar ro'yxati, kargo tracking (demo va noto'g'ri raqam bilan)
- ✅ RBAC, admin/kuryer/mijoz login — barchasi to'g'ri ishladi
- ✅ Server logida **0 ta xato/traceback**

---

## 8. Keyingi bosqichlar (production uchun TODO)

Bu — **ishlaydigan arxitektura skeleti**, lekin productionga chiqishdan oldin quyidagilar qo'shilishi kerak:

- [ ] **Alembic** migratsiyalari (`Base.metadata.create_all` faqat dev uchun)
- [ ] PostgreSQL ga o'tish (`.env` dagi `DATABASE_URL` ni o'zgartirish yetarli)
- [ ] Payme / Click **webhook** integratsiyasi va imzo tekshiruvi
- [ ] SMS-OTP (Eskiz.uz) va Telegram bot xabarnomalari
- [ ] Refresh tokenlarni bazada saqlash va bekor qilish (revocation) mexanizmi
- [ ] Rasm/video yuklash uchun S3/MinIO integratsiyasi
- [ ] Sharh (reviews), wishlist va bildirishnoma (notifications) endpointlari
- [ ] Redis keshlash va Celery fon vazifalari (tracking yangilanishi va h.k.)
- [ ] Avtomatlashtirilgan testlar (pytest) va CI/CD

---

## 9. Texnologiyalar

FastAPI · SQLAlchemy 2.0 · Pydantic v2 · SQLite (dev) / PostgreSQL (prod) ·
python-jose (JWT) · passlib+bcrypt · SQLAdmin · Vanilla JS frontend (build jarayonisiz)
