"""
OPTOM MARKET — kengaytirilgan demo katalog ma'lumotlari.
Avtomatik generatsiya qilingan: 8 kategoriya (ayollar, erkaklar, bolalar, chaqaloqlar,
ich kiyim, oyoq kiyim, sumkalar, bosh kiyimlar), har birida 20 tadan mahsulot
(jami 160 ta, 480 variant). Barcha mahsulotlar STANDART 4-bosqichli narxlash
tizimiga ega: 1-4 dona (dona narxi), 5-19 (kichik optom), 20-49 (optom), 50+ (katta optom).
seed.py shu faylni import qilib bazani to'ldiradi.
"""

CATEGORIES = [
    {"slug": "ayollar-kiyimi", "name_uz": "Ayollar kiyimi", "name_ru": "Женская одежда", "gender": "woman", "sort_order": 1},
    {"slug": "erkaklar-kiyimi", "name_uz": "Erkaklar kiyimi", "name_ru": "Мужская одежда", "gender": "man", "sort_order": 2},
    {"slug": "bolalar-kiyimi", "name_uz": "Bolalar kiyimi", "name_ru": "Детская одежда", "gender": "kids", "sort_order": 3},
    {"slug": "chaqaloqlar-kiyimi", "name_uz": "Chaqaloqlar kiyimi", "name_ru": "Одежда для малышей", "gender": "baby", "sort_order": 4},
    {"slug": "ich-kiyim", "name_uz": "Ich kiyim", "name_ru": "Нижнее бельё", "gender": "unisex", "sort_order": 5},
    {"slug": "oyoq-kiyim", "name_uz": "Oyoq kiyim", "name_ru": "Обувь", "gender": "unisex", "sort_order": 6},
    {"slug": "sumkalar", "name_uz": "Sumkalar", "name_ru": "Сумки", "gender": "unisex", "sort_order": 7},
    {"slug": "bosh-kiyimlar", "name_uz": "Bosh kiyimlar", "name_ru": "Головные уборы", "gender": "unisex", "sort_order": 8},
]

CATALOG = [
    {
        'id': 1, 'title': "Yozgi ko'ylak “Bosphorus”", 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=101, size='S', color='Qizil', sku='WM-01-S', retail=113000, wholesale=81000, min_qty=5, tiers=[(5, 96000), (20, 81000), (50, 68000)], available=85, reserved=0),
            dict(id=102, size='M', color='Qizil', sku='WM-01-M', retail=113000, wholesale=81000, min_qty=5, tiers=[(5, 96000), (20, 81000), (50, 68000)], available=77, reserved=0),
            dict(id=103, size='L', color='Qizil', sku='WM-01-L', retail=113000, wholesale=81000, min_qty=5, tiers=[(5, 96000), (20, 81000), (50, 68000)], available=72, reserved=0),
        ],
    },
    {
        'id': 2, 'title': 'Bluzka “Istanbul Moda”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=104, size='S', color='Qora', sku='WM-02-S', retail=75000, wholesale=54000, min_qty=5, tiers=[(5, 64000), (20, 54000), (50, 45000)], available=154, reserved=0),
            dict(id=105, size='M', color='Qora', sku='WM-02-M', retail=75000, wholesale=54000, min_qty=5, tiers=[(5, 64000), (20, 54000), (50, 45000)], available=37, reserved=0),
            dict(id=106, size='L', color='Qora', sku='WM-02-L', retail=75000, wholesale=54000, min_qty=5, tiers=[(5, 64000), (20, 54000), (50, 45000)], available=166, reserved=0),
        ],
    },
    {
        'id': 3, 'title': 'Yubka “Ankara Style”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=107, size='S', color='Qizil', sku='WM-03-S', retail=97000, wholesale=70000, min_qty=5, tiers=[(5, 82000), (20, 70000), (50, 58000)], available=38, reserved=0),
            dict(id=108, size='M', color='Qizil', sku='WM-03-M', retail=97000, wholesale=70000, min_qty=5, tiers=[(5, 82000), (20, 70000), (50, 58000)], available=70, reserved=0),
            dict(id=109, size='L', color='Qizil', sku='WM-03-L', retail=97000, wholesale=70000, min_qty=5, tiers=[(5, 82000), (20, 70000), (50, 58000)], available=74, reserved=0),
        ],
    },
    {
        'id': 4, 'title': 'Klassik shim “Izmir Belle”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=110, size='S', color='Qizil', sku='WM-04-S', retail=103000, wholesale=74000, min_qty=5, tiers=[(5, 88000), (20, 74000), (50, 62000)], available=158, reserved=0),
            dict(id=111, size='M', color='Qizil', sku='WM-04-M', retail=103000, wholesale=74000, min_qty=5, tiers=[(5, 88000), (20, 74000), (50, 62000)], available=65, reserved=0),
            dict(id=112, size='L', color='Qizil', sku='WM-04-L', retail=103000, wholesale=74000, min_qty=5, tiers=[(5, 88000), (20, 74000), (50, 62000)], available=154, reserved=0),
        ],
    },
    {
        'id': 5, 'title': 'Kurtka “Selin”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=113, size='S', color='Kulrang', sku='WM-05-S', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=165, reserved=0),
            dict(id=114, size='M', color='Kulrang', sku='WM-05-M', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=86, reserved=0),
            dict(id=115, size='L', color='Kulrang', sku='WM-05-L', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=16, reserved=0),
        ],
    },
    {
        'id': 6, 'title': 'Sviter “Aylin”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=116, size='S', color="Ko'k", sku='WM-06-S', retail=122000, wholesale=88000, min_qty=5, tiers=[(5, 104000), (20, 88000), (50, 73000)], available=123, reserved=0),
            dict(id=117, size='M', color="Ko'k", sku='WM-06-M', retail=122000, wholesale=88000, min_qty=5, tiers=[(5, 104000), (20, 88000), (50, 73000)], available=102, reserved=0),
            dict(id=118, size='L', color="Ko'k", sku='WM-06-L', retail=122000, wholesale=88000, min_qty=5, tiers=[(5, 104000), (20, 88000), (50, 73000)], available=86, reserved=0),
        ],
    },
    {
        'id': 7, 'title': 'Kombinezon “Nazli”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=119, size='S', color='Pushti', sku='WM-07-S', retail=77000, wholesale=55000, min_qty=5, tiers=[(5, 65000), (20, 55000), (50, 46000)], available=41, reserved=0),
            dict(id=120, size='M', color='Pushti', sku='WM-07-M', retail=77000, wholesale=55000, min_qty=5, tiers=[(5, 65000), (20, 55000), (50, 46000)], available=38, reserved=0),
            dict(id=121, size='L', color='Pushti', sku='WM-07-L', retail=77000, wholesale=55000, min_qty=5, tiers=[(5, 65000), (20, 55000), (50, 46000)], available=112, reserved=0),
        ],
    },
    {
        'id': 8, 'title': 'Palto “Ceylan”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=122, size='S', color='Pushti', sku='WM-08-S', retail=72000, wholesale=52000, min_qty=5, tiers=[(5, 61000), (20, 52000), (50, 43000)], available=169, reserved=0),
            dict(id=123, size='M', color='Pushti', sku='WM-08-M', retail=72000, wholesale=52000, min_qty=5, tiers=[(5, 61000), (20, 52000), (50, 43000)], available=82, reserved=0),
            dict(id=124, size='L', color='Pushti', sku='WM-08-L', retail=72000, wholesale=52000, min_qty=5, tiers=[(5, 61000), (20, 52000), (50, 43000)], available=26, reserved=0),
        ],
    },
    {
        'id': 9, 'title': 'Jinsi shim “Ege Trend”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=125, size='S', color='Qora', sku='WM-09-S', retail=120000, wholesale=86000, min_qty=5, tiers=[(5, 102000), (20, 86000), (50, 72000)], available=111, reserved=0),
            dict(id=126, size='M', color='Qora', sku='WM-09-M', retail=120000, wholesale=86000, min_qty=5, tiers=[(5, 102000), (20, 86000), (50, 72000)], available=35, reserved=0),
            dict(id=127, size='L', color='Qora', sku='WM-09-L', retail=120000, wholesale=86000, min_qty=5, tiers=[(5, 102000), (20, 86000), (50, 72000)], available=156, reserved=0),
        ],
    },
    {
        'id': 10, 'title': 'Sarafan “Lale”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=128, size='S', color='Pushti', sku='WM-10-S', retail=87000, wholesale=63000, min_qty=5, tiers=[(5, 74000), (20, 63000), (50, 52000)], available=162, reserved=0),
            dict(id=129, size='M', color='Pushti', sku='WM-10-M', retail=87000, wholesale=63000, min_qty=5, tiers=[(5, 74000), (20, 63000), (50, 52000)], available=64, reserved=0),
            dict(id=130, size='L', color='Pushti', sku='WM-10-L', retail=87000, wholesale=63000, min_qty=5, tiers=[(5, 74000), (20, 63000), (50, 52000)], available=32, reserved=0),
        ],
    },
    {
        'id': 11, 'title': 'Kardigan “Yasemin”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=131, size='S', color='Bej', sku='WM-11-S', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=89, reserved=0),
            dict(id=132, size='M', color='Bej', sku='WM-11-M', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=35, reserved=0),
            dict(id=133, size='L', color='Bej', sku='WM-11-L', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=74, reserved=0),
        ],
    },
    {
        'id': 12, 'title': 'Tunika “Defne”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=134, size='S', color='Oq', sku='WM-12-S', retail=130000, wholesale=94000, min_qty=5, tiers=[(5, 110000), (20, 94000), (50, 78000)], available=86, reserved=0),
            dict(id=135, size='M', color='Oq', sku='WM-12-M', retail=130000, wholesale=94000, min_qty=5, tiers=[(5, 110000), (20, 94000), (50, 78000)], available=131, reserved=0),
            dict(id=136, size='L', color='Oq', sku='WM-12-L', retail=130000, wholesale=94000, min_qty=5, tiers=[(5, 110000), (20, 94000), (50, 78000)], available=177, reserved=0),
        ],
    },
    {
        'id': 13, 'title': 'Trench palto “Sultanah”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=137, size='S', color="Ko'k", sku='WM-13-S', retail=128000, wholesale=92000, min_qty=5, tiers=[(5, 109000), (20, 92000), (50, 77000)], available=109, reserved=0),
            dict(id=138, size='M', color="Ko'k", sku='WM-13-M', retail=128000, wholesale=92000, min_qty=5, tiers=[(5, 109000), (20, 92000), (50, 77000)], available=105, reserved=0),
            dict(id=139, size='L', color="Ko'k", sku='WM-13-L', retail=128000, wholesale=92000, min_qty=5, tiers=[(5, 109000), (20, 92000), (50, 77000)], available=68, reserved=0),
        ],
    },
    {
        'id': 14, 'title': 'Sport kostyum “Zumrut”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=140, size='S', color='Qora', sku='WM-14-S', retail=115000, wholesale=83000, min_qty=5, tiers=[(5, 98000), (20, 83000), (50, 69000)], available=170, reserved=0),
            dict(id=141, size='M', color='Qora', sku='WM-14-M', retail=115000, wholesale=83000, min_qty=5, tiers=[(5, 98000), (20, 83000), (50, 69000)], available=177, reserved=0),
            dict(id=142, size='L', color='Qora', sku='WM-14-L', retail=115000, wholesale=83000, min_qty=5, tiers=[(5, 98000), (20, 83000), (50, 69000)], available=58, reserved=0),
        ],
    },
    {
        'id': 15, 'title': "Uzun ko'ylak “Nergiz”", 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=143, size='S', color='Bej', sku='WM-15-S', retail=105000, wholesale=76000, min_qty=5, tiers=[(5, 89000), (20, 76000), (50, 63000)], available=56, reserved=0),
            dict(id=144, size='M', color='Bej', sku='WM-15-M', retail=105000, wholesale=76000, min_qty=5, tiers=[(5, 89000), (20, 76000), (50, 63000)], available=133, reserved=0),
            dict(id=145, size='L', color='Bej', sku='WM-15-L', retail=105000, wholesale=76000, min_qty=5, tiers=[(5, 89000), (20, 76000), (50, 63000)], available=112, reserved=0),
        ],
    },
    {
        'id': 16, 'title': 'Yengil jaket “Damla”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=146, size='S', color='Bej', sku='WM-16-S', retail=85000, wholesale=61000, min_qty=5, tiers=[(5, 72000), (20, 61000), (50, 51000)], available=98, reserved=0),
            dict(id=147, size='M', color='Bej', sku='WM-16-M', retail=85000, wholesale=61000, min_qty=5, tiers=[(5, 72000), (20, 61000), (50, 51000)], available=29, reserved=0),
            dict(id=148, size='L', color='Bej', sku='WM-16-L', retail=85000, wholesale=61000, min_qty=5, tiers=[(5, 72000), (20, 61000), (50, 51000)], available=73, reserved=0),
        ],
    },
    {
        'id': 17, 'title': 'Trikotaj bluzka “Elif Line”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=149, size='S', color='Pushti', sku='WM-17-S', retail=127000, wholesale=91000, min_qty=5, tiers=[(5, 108000), (20, 91000), (50, 76000)], available=117, reserved=0),
            dict(id=150, size='M', color='Pushti', sku='WM-17-M', retail=127000, wholesale=91000, min_qty=5, tiers=[(5, 108000), (20, 91000), (50, 76000)], available=83, reserved=0),
            dict(id=151, size='L', color='Pushti', sku='WM-17-L', retail=127000, wholesale=91000, min_qty=5, tiers=[(5, 108000), (20, 91000), (50, 76000)], available=31, reserved=0),
        ],
    },
    {
        'id': 18, 'title': "Maxsi ko'ylak “Sude”", 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=152, size='S', color='Pushti', sku='WM-18-S', retail=81000, wholesale=58000, min_qty=5, tiers=[(5, 69000), (20, 58000), (50, 49000)], available=69, reserved=0),
            dict(id=153, size='M', color='Pushti', sku='WM-18-M', retail=81000, wholesale=58000, min_qty=5, tiers=[(5, 69000), (20, 58000), (50, 49000)], available=142, reserved=0),
            dict(id=154, size='L', color='Pushti', sku='WM-18-L', retail=81000, wholesale=58000, min_qty=5, tiers=[(5, 69000), (20, 58000), (50, 49000)], available=116, reserved=0),
        ],
    },
    {
        'id': 19, 'title': 'Yozgi shorty “Perihan”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=155, size='S', color='Kulrang', sku='WM-19-S', retail=131000, wholesale=94000, min_qty=5, tiers=[(5, 111000), (20, 94000), (50, 79000)], available=51, reserved=0),
            dict(id=156, size='M', color='Kulrang', sku='WM-19-M', retail=131000, wholesale=94000, min_qty=5, tiers=[(5, 111000), (20, 94000), (50, 79000)], available=82, reserved=0),
            dict(id=157, size='L', color='Kulrang', sku='WM-19-L', retail=131000, wholesale=94000, min_qty=5, tiers=[(5, 111000), (20, 94000), (50, 79000)], available=50, reserved=0),
        ],
    },
    {
        'id': 20, 'title': 'Klassik jaket “Gonca”', 'category_id': 'ayollar-kiyimi',
        'origin': 'Turkiya', 'icon': '👗', 'variants': [
            dict(id=158, size='S', color='Yashil', sku='WM-20-S', retail=83000, wholesale=60000, min_qty=5, tiers=[(5, 71000), (20, 60000), (50, 50000)], available=164, reserved=0),
            dict(id=159, size='M', color='Yashil', sku='WM-20-M', retail=83000, wholesale=60000, min_qty=5, tiers=[(5, 71000), (20, 60000), (50, 50000)], available=124, reserved=0),
            dict(id=160, size='L', color='Yashil', sku='WM-20-L', retail=83000, wholesale=60000, min_qty=5, tiers=[(5, 71000), (20, 60000), (50, 50000)], available=164, reserved=0),
        ],
    },
    {
        'id': 21, 'title': "Klassik ko'ylak “Anadolu”", 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=161, size='S', color="Ko'k", sku='MN-01-S', retail=117000, wholesale=84000, min_qty=5, tiers=[(5, 99000), (20, 84000), (50, 70000)], available=50, reserved=0),
            dict(id=162, size='M', color="Ko'k", sku='MN-01-M', retail=117000, wholesale=84000, min_qty=5, tiers=[(5, 99000), (20, 84000), (50, 70000)], available=145, reserved=0),
            dict(id=163, size='L', color="Ko'k", sku='MN-01-L', retail=117000, wholesale=84000, min_qty=5, tiers=[(5, 99000), (20, 84000), (50, 70000)], available=141, reserved=0),
            dict(id=164, size='XL', color="Ko'k", sku='MN-01-XL', retail=117000, wholesale=84000, min_qty=5, tiers=[(5, 99000), (20, 84000), (50, 70000)], available=38, reserved=0),
        ],
    },
    {
        'id': 22, 'title': 'Shim “Kapadokya”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=165, size='S', color='Qora', sku='MN-02-S', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=54, reserved=0),
            dict(id=166, size='M', color='Qora', sku='MN-02-M', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=175, reserved=0),
            dict(id=167, size='L', color='Qora', sku='MN-02-L', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=55, reserved=0),
            dict(id=168, size='XL', color='Qora', sku='MN-02-XL', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=123, reserved=0),
        ],
    },
    {
        'id': 23, 'title': 'Kostyum “Galata Man”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=169, size='S', color='Xaki', sku='MN-03-S', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=112, reserved=0),
            dict(id=170, size='M', color='Xaki', sku='MN-03-M', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=167, reserved=0),
            dict(id=171, size='L', color='Xaki', sku='MN-03-L', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=134, reserved=0),
            dict(id=172, size='XL', color='Xaki', sku='MN-03-XL', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=150, reserved=0),
        ],
    },
    {
        'id': 24, 'title': 'Kurtka “Marmara”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=173, size='S', color='Oq', sku='MN-04-S', retail=101000, wholesale=73000, min_qty=5, tiers=[(5, 86000), (20, 73000), (50, 61000)], available=17, reserved=0),
            dict(id=174, size='M', color='Oq', sku='MN-04-M', retail=101000, wholesale=73000, min_qty=5, tiers=[(5, 86000), (20, 73000), (50, 61000)], available=44, reserved=0),
            dict(id=175, size='L', color='Oq', sku='MN-04-L', retail=101000, wholesale=73000, min_qty=5, tiers=[(5, 86000), (20, 73000), (50, 61000)], available=152, reserved=0),
            dict(id=176, size='XL', color='Oq', sku='MN-04-XL', retail=101000, wholesale=73000, min_qty=5, tiers=[(5, 86000), (20, 73000), (50, 61000)], available=83, reserved=0),
        ],
    },
    {
        'id': 25, 'title': 'Futbolka “Bodrum”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=177, size='S', color='Kulrang', sku='MN-05-S', retail=156000, wholesale=112000, min_qty=5, tiers=[(5, 133000), (20, 112000), (50, 94000)], available=43, reserved=0),
            dict(id=178, size='M', color='Kulrang', sku='MN-05-M', retail=156000, wholesale=112000, min_qty=5, tiers=[(5, 133000), (20, 112000), (50, 94000)], available=90, reserved=0),
            dict(id=179, size='L', color='Kulrang', sku='MN-05-L', retail=156000, wholesale=112000, min_qty=5, tiers=[(5, 133000), (20, 112000), (50, 94000)], available=126, reserved=0),
            dict(id=180, size='XL', color='Kulrang', sku='MN-05-XL', retail=156000, wholesale=112000, min_qty=5, tiers=[(5, 133000), (20, 112000), (50, 94000)], available=55, reserved=0),
        ],
    },
    {
        'id': 26, 'title': 'Sviter “Toros”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=181, size='S', color='Jigarrang', sku='MN-06-S', retail=123000, wholesale=89000, min_qty=5, tiers=[(5, 105000), (20, 89000), (50, 74000)], available=82, reserved=0),
            dict(id=182, size='M', color='Jigarrang', sku='MN-06-M', retail=123000, wholesale=89000, min_qty=5, tiers=[(5, 105000), (20, 89000), (50, 74000)], available=143, reserved=0),
            dict(id=183, size='L', color='Jigarrang', sku='MN-06-L', retail=123000, wholesale=89000, min_qty=5, tiers=[(5, 105000), (20, 89000), (50, 74000)], available=60, reserved=0),
            dict(id=184, size='XL', color='Jigarrang', sku='MN-06-XL', retail=123000, wholesale=89000, min_qty=5, tiers=[(5, 105000), (20, 89000), (50, 74000)], available=144, reserved=0),
        ],
    },
    {
        'id': 27, 'title': 'Jinsi shim “Sultan Line”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=185, size='S', color='Jigarrang', sku='MN-07-S', retail=171000, wholesale=123000, min_qty=5, tiers=[(5, 145000), (20, 123000), (50, 103000)], available=91, reserved=0),
            dict(id=186, size='M', color='Jigarrang', sku='MN-07-M', retail=171000, wholesale=123000, min_qty=5, tiers=[(5, 145000), (20, 123000), (50, 103000)], available=178, reserved=0),
            dict(id=187, size='L', color='Jigarrang', sku='MN-07-L', retail=171000, wholesale=123000, min_qty=5, tiers=[(5, 145000), (20, 123000), (50, 103000)], available=144, reserved=0),
            dict(id=188, size='XL', color='Jigarrang', sku='MN-07-XL', retail=171000, wholesale=123000, min_qty=5, tiers=[(5, 145000), (20, 123000), (50, 103000)], available=170, reserved=0),
        ],
    },
    {
        'id': 28, 'title': 'Palto “Bosfor Man”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=189, size='S', color='Kulrang', sku='MN-08-S', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=56, reserved=0),
            dict(id=190, size='M', color='Kulrang', sku='MN-08-M', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=153, reserved=0),
            dict(id=191, size='L', color='Kulrang', sku='MN-08-L', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=150, reserved=0),
            dict(id=192, size='XL', color='Kulrang', sku='MN-08-XL', retail=96000, wholesale=69000, min_qty=5, tiers=[(5, 82000), (20, 69000), (50, 58000)], available=15, reserved=0),
        ],
    },
    {
        'id': 29, 'title': 'Sportivka “Trabzon”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=193, size='S', color='Xaki', sku='MN-09-S', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=19, reserved=0),
            dict(id=194, size='M', color='Xaki', sku='MN-09-M', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=43, reserved=0),
            dict(id=195, size='L', color='Xaki', sku='MN-09-L', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=107, reserved=0),
            dict(id=196, size='XL', color='Xaki', sku='MN-09-XL', retail=138000, wholesale=99000, min_qty=5, tiers=[(5, 117000), (20, 99000), (50, 83000)], available=93, reserved=0),
        ],
    },
    {
        'id': 30, 'title': 'Trenchcoat “Konya”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=197, size='S', color="Ko'k", sku='MN-10-S', retail=100000, wholesale=72000, min_qty=5, tiers=[(5, 85000), (20, 72000), (50, 60000)], available=160, reserved=0),
            dict(id=198, size='M', color="Ko'k", sku='MN-10-M', retail=100000, wholesale=72000, min_qty=5, tiers=[(5, 85000), (20, 72000), (50, 60000)], available=35, reserved=0),
            dict(id=199, size='L', color="Ko'k", sku='MN-10-L', retail=100000, wholesale=72000, min_qty=5, tiers=[(5, 85000), (20, 72000), (50, 60000)], available=36, reserved=0),
            dict(id=200, size='XL', color="Ko'k", sku='MN-10-XL', retail=100000, wholesale=72000, min_qty=5, tiers=[(5, 85000), (20, 72000), (50, 60000)], available=139, reserved=0),
        ],
    },
    {
        'id': 31, 'title': 'Jilet “Antalya”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=201, size='S', color='Oq', sku='MN-11-S', retail=161000, wholesale=116000, min_qty=5, tiers=[(5, 137000), (20, 116000), (50, 97000)], available=47, reserved=0),
            dict(id=202, size='M', color='Oq', sku='MN-11-M', retail=161000, wholesale=116000, min_qty=5, tiers=[(5, 137000), (20, 116000), (50, 97000)], available=47, reserved=0),
            dict(id=203, size='L', color='Oq', sku='MN-11-L', retail=161000, wholesale=116000, min_qty=5, tiers=[(5, 137000), (20, 116000), (50, 97000)], available=136, reserved=0),
            dict(id=204, size='XL', color='Oq', sku='MN-11-XL', retail=161000, wholesale=116000, min_qty=5, tiers=[(5, 137000), (20, 116000), (50, 97000)], available=155, reserved=0),
        ],
    },
    {
        'id': 32, 'title': 'Shorty “Efes”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=205, size='S', color='Oq', sku='MN-12-S', retail=92000, wholesale=66000, min_qty=5, tiers=[(5, 78000), (20, 66000), (50, 55000)], available=170, reserved=0),
            dict(id=206, size='M', color='Oq', sku='MN-12-M', retail=92000, wholesale=66000, min_qty=5, tiers=[(5, 78000), (20, 66000), (50, 55000)], available=123, reserved=0),
            dict(id=207, size='L', color='Oq', sku='MN-12-L', retail=92000, wholesale=66000, min_qty=5, tiers=[(5, 78000), (20, 66000), (50, 55000)], available=69, reserved=0),
            dict(id=208, size='XL', color='Oq', sku='MN-12-XL', retail=92000, wholesale=66000, min_qty=5, tiers=[(5, 78000), (20, 66000), (50, 55000)], available=153, reserved=0),
        ],
    },
    {
        'id': 33, 'title': 'Polo futbolka “Kayseri”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=209, size='S', color='Jigarrang', sku='MN-13-S', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=66, reserved=0),
            dict(id=210, size='M', color='Jigarrang', sku='MN-13-M', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=94, reserved=0),
            dict(id=211, size='L', color='Jigarrang', sku='MN-13-L', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=117, reserved=0),
            dict(id=212, size='XL', color='Jigarrang', sku='MN-13-XL', retail=154000, wholesale=111000, min_qty=5, tiers=[(5, 131000), (20, 111000), (50, 92000)], available=110, reserved=0),
        ],
    },
    {
        'id': 34, 'title': 'Denim kurtka “Erzurum”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=213, size='S', color='Oq', sku='MN-14-S', retail=121000, wholesale=87000, min_qty=5, tiers=[(5, 103000), (20, 87000), (50, 73000)], available=130, reserved=0),
            dict(id=214, size='M', color='Oq', sku='MN-14-M', retail=121000, wholesale=87000, min_qty=5, tiers=[(5, 103000), (20, 87000), (50, 73000)], available=45, reserved=0),
            dict(id=215, size='L', color='Oq', sku='MN-14-L', retail=121000, wholesale=87000, min_qty=5, tiers=[(5, 103000), (20, 87000), (50, 73000)], available=78, reserved=0),
            dict(id=216, size='XL', color='Oq', sku='MN-14-XL', retail=121000, wholesale=87000, min_qty=5, tiers=[(5, 103000), (20, 87000), (50, 73000)], available=72, reserved=0),
        ],
    },
    {
        'id': 35, 'title': 'Yengil kurtka “Edirne”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=217, size='S', color='Qora', sku='MN-15-S', retail=82000, wholesale=59000, min_qty=5, tiers=[(5, 70000), (20, 59000), (50, 49000)], available=165, reserved=0),
            dict(id=218, size='M', color='Qora', sku='MN-15-M', retail=82000, wholesale=59000, min_qty=5, tiers=[(5, 70000), (20, 59000), (50, 49000)], available=156, reserved=0),
            dict(id=219, size='L', color='Qora', sku='MN-15-L', retail=82000, wholesale=59000, min_qty=5, tiers=[(5, 70000), (20, 59000), (50, 49000)], available=73, reserved=0),
            dict(id=220, size='XL', color='Qora', sku='MN-15-XL', retail=82000, wholesale=59000, min_qty=5, tiers=[(5, 70000), (20, 59000), (50, 49000)], available=165, reserved=0),
        ],
    },
    {
        'id': 36, 'title': "Termo kiyim to'plami “Samsun Line”", 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=221, size='S', color='Qora', sku='MN-16-S', retail=98000, wholesale=71000, min_qty=5, tiers=[(5, 83000), (20, 71000), (50, 59000)], available=176, reserved=0),
            dict(id=222, size='M', color='Qora', sku='MN-16-M', retail=98000, wholesale=71000, min_qty=5, tiers=[(5, 83000), (20, 71000), (50, 59000)], available=30, reserved=0),
            dict(id=223, size='L', color='Qora', sku='MN-16-L', retail=98000, wholesale=71000, min_qty=5, tiers=[(5, 83000), (20, 71000), (50, 59000)], available=73, reserved=0),
            dict(id=224, size='XL', color='Qora', sku='MN-16-XL', retail=98000, wholesale=71000, min_qty=5, tiers=[(5, 83000), (20, 71000), (50, 59000)], available=32, reserved=0),
        ],
    },
    {
        'id': 37, 'title': 'Sport shorty “Rize”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=225, size='S', color='Kulrang', sku='MN-17-S', retail=170000, wholesale=122000, min_qty=5, tiers=[(5, 144000), (20, 122000), (50, 102000)], available=33, reserved=0),
            dict(id=226, size='M', color='Kulrang', sku='MN-17-M', retail=170000, wholesale=122000, min_qty=5, tiers=[(5, 144000), (20, 122000), (50, 102000)], available=146, reserved=0),
            dict(id=227, size='L', color='Kulrang', sku='MN-17-L', retail=170000, wholesale=122000, min_qty=5, tiers=[(5, 144000), (20, 122000), (50, 102000)], available=75, reserved=0),
            dict(id=228, size='XL', color='Kulrang', sku='MN-17-XL', retail=170000, wholesale=122000, min_qty=5, tiers=[(5, 144000), (20, 122000), (50, 102000)], available=86, reserved=0),
        ],
    },
    {
        'id': 38, 'title': "Katakli ko'ylak “Van Style”", 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=229, size='S', color="Ko'k", sku='MN-18-S', retail=145000, wholesale=104000, min_qty=5, tiers=[(5, 123000), (20, 104000), (50, 87000)], available=153, reserved=0),
            dict(id=230, size='M', color="Ko'k", sku='MN-18-M', retail=145000, wholesale=104000, min_qty=5, tiers=[(5, 123000), (20, 104000), (50, 87000)], available=48, reserved=0),
            dict(id=231, size='L', color="Ko'k", sku='MN-18-L', retail=145000, wholesale=104000, min_qty=5, tiers=[(5, 123000), (20, 104000), (50, 87000)], available=161, reserved=0),
            dict(id=232, size='XL', color="Ko'k", sku='MN-18-XL', retail=145000, wholesale=104000, min_qty=5, tiers=[(5, 123000), (20, 104000), (50, 87000)], available=162, reserved=0),
        ],
    },
    {
        'id': 39, 'title': 'Kardigan “Mersin”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=233, size='S', color='Xaki', sku='MN-19-S', retail=125000, wholesale=90000, min_qty=5, tiers=[(5, 106000), (20, 90000), (50, 75000)], available=119, reserved=0),
            dict(id=234, size='M', color='Xaki', sku='MN-19-M', retail=125000, wholesale=90000, min_qty=5, tiers=[(5, 106000), (20, 90000), (50, 75000)], available=63, reserved=0),
            dict(id=235, size='L', color='Xaki', sku='MN-19-L', retail=125000, wholesale=90000, min_qty=5, tiers=[(5, 106000), (20, 90000), (50, 75000)], available=39, reserved=0),
            dict(id=236, size='XL', color='Xaki', sku='MN-19-XL', retail=125000, wholesale=90000, min_qty=5, tiers=[(5, 106000), (20, 90000), (50, 75000)], available=39, reserved=0),
        ],
    },
    {
        'id': 40, 'title': 'Klassik jaket “Adana”', 'category_id': 'erkaklar-kiyimi',
        'origin': 'Turkiya', 'icon': '👔', 'variants': [
            dict(id=237, size='S', color='Kulrang', sku='MN-20-S', retail=144000, wholesale=104000, min_qty=5, tiers=[(5, 122000), (20, 104000), (50, 86000)], available=123, reserved=0),
            dict(id=238, size='M', color='Kulrang', sku='MN-20-M', retail=144000, wholesale=104000, min_qty=5, tiers=[(5, 122000), (20, 104000), (50, 86000)], available=120, reserved=0),
            dict(id=239, size='L', color='Kulrang', sku='MN-20-L', retail=144000, wholesale=104000, min_qty=5, tiers=[(5, 122000), (20, 104000), (50, 86000)], available=134, reserved=0),
            dict(id=240, size='XL', color='Kulrang', sku='MN-20-XL', retail=144000, wholesale=104000, min_qty=5, tiers=[(5, 122000), (20, 104000), (50, 86000)], available=28, reserved=0),
        ],
    },
    {
        'id': 41, 'title': "Ko'ylakcha “Panda Kids”", 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=241, size='92-98', color='Sariq', sku='KD-01-92-98', retail=79000, wholesale=57000, min_qty=5, tiers=[(5, 67000), (20, 57000), (50, 47000)], available=30, reserved=0),
            dict(id=242, size='98-104', color='Sariq', sku='KD-01-98-104', retail=79000, wholesale=57000, min_qty=5, tiers=[(5, 67000), (20, 57000), (50, 47000)], available=118, reserved=0),
            dict(id=243, size='104-110', color='Sariq', sku='KD-01-104-110', retail=79000, wholesale=57000, min_qty=5, tiers=[(5, 67000), (20, 57000), (50, 47000)], available=101, reserved=0),
            dict(id=244, size='110-116', color='Sariq', sku='KD-01-110-116', retail=79000, wholesale=57000, min_qty=5, tiers=[(5, 67000), (20, 57000), (50, 47000)], available=42, reserved=0),
        ],
    },
    {
        'id': 42, 'title': 'Shimcha “Little Dragon”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=245, size='92-98', color='Pushti', sku='KD-02-92-98', retail=57000, wholesale=41000, min_qty=5, tiers=[(5, 48000), (20, 41000), (50, 34000)], available=152, reserved=0),
            dict(id=246, size='98-104', color='Pushti', sku='KD-02-98-104', retail=57000, wholesale=41000, min_qty=5, tiers=[(5, 48000), (20, 41000), (50, 34000)], available=129, reserved=0),
            dict(id=247, size='104-110', color='Pushti', sku='KD-02-104-110', retail=57000, wholesale=41000, min_qty=5, tiers=[(5, 48000), (20, 41000), (50, 34000)], available=50, reserved=0),
            dict(id=248, size='110-116', color='Pushti', sku='KD-02-110-116', retail=57000, wholesale=41000, min_qty=5, tiers=[(5, 48000), (20, 41000), (50, 34000)], available=123, reserved=0),
        ],
    },
    {
        'id': 43, 'title': 'Kombinezon “Sunny Bear”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=249, size='92-98', color='Assorti', sku='KD-03-92-98', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=78, reserved=0),
            dict(id=250, size='98-104', color='Assorti', sku='KD-03-98-104', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=34, reserved=0),
            dict(id=251, size='104-110', color='Assorti', sku='KD-03-104-110', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=128, reserved=0),
            dict(id=252, size='110-116', color='Assorti', sku='KD-03-110-116', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=155, reserved=0),
        ],
    },
    {
        'id': 44, 'title': 'Sviter “Happy Cloud”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=253, size='92-98', color='Yashil', sku='KD-04-92-98', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=18, reserved=0),
            dict(id=254, size='98-104', color='Yashil', sku='KD-04-98-104', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=38, reserved=0),
            dict(id=255, size='104-110', color='Yashil', sku='KD-04-104-110', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=75, reserved=0),
            dict(id=256, size='110-116', color='Yashil', sku='KD-04-110-116', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=57, reserved=0),
        ],
    },
    {
        'id': 45, 'title': 'Kurtkacha “Kids Comfort”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=257, size='92-98', color='Assorti', sku='KD-05-92-98', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=69, reserved=0),
            dict(id=258, size='98-104', color='Assorti', sku='KD-05-98-104', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=117, reserved=0),
            dict(id=259, size='104-110', color='Assorti', sku='KD-05-104-110', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=30, reserved=0),
            dict(id=260, size='110-116', color='Assorti', sku='KD-05-110-116', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=57, reserved=0),
        ],
    },
    {
        'id': 46, 'title': 'Sarafancha “Little Star”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=261, size='92-98', color='Assorti', sku='KD-06-92-98', retail=64000, wholesale=46000, min_qty=5, tiers=[(5, 54000), (20, 46000), (50, 38000)], available=82, reserved=0),
            dict(id=262, size='98-104', color='Assorti', sku='KD-06-98-104', retail=64000, wholesale=46000, min_qty=5, tiers=[(5, 54000), (20, 46000), (50, 38000)], available=131, reserved=0),
            dict(id=263, size='104-110', color='Assorti', sku='KD-06-104-110', retail=64000, wholesale=46000, min_qty=5, tiers=[(5, 54000), (20, 46000), (50, 38000)], available=88, reserved=0),
            dict(id=264, size='110-116', color='Assorti', sku='KD-06-110-116', retail=64000, wholesale=46000, min_qty=5, tiers=[(5, 54000), (20, 46000), (50, 38000)], available=123, reserved=0),
        ],
    },
    {
        'id': 47, 'title': 'Futbolkacha “Bamboo Kids”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=265, size='92-98', color='Yashil', sku='KD-07-92-98', retail=80000, wholesale=58000, min_qty=5, tiers=[(5, 68000), (20, 58000), (50, 48000)], available=139, reserved=0),
            dict(id=266, size='98-104', color='Yashil', sku='KD-07-98-104', retail=80000, wholesale=58000, min_qty=5, tiers=[(5, 68000), (20, 58000), (50, 48000)], available=54, reserved=0),
            dict(id=267, size='104-110', color='Yashil', sku='KD-07-104-110', retail=80000, wholesale=58000, min_qty=5, tiers=[(5, 68000), (20, 58000), (50, 48000)], available=63, reserved=0),
            dict(id=268, size='110-116', color='Yashil', sku='KD-07-110-116', retail=80000, wholesale=58000, min_qty=5, tiers=[(5, 68000), (20, 58000), (50, 48000)], available=90, reserved=0),
        ],
    },
    {
        'id': 48, 'title': 'Shortikcha “Rainbow Line”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=269, size='92-98', color='Sariq', sku='KD-08-92-98', retail=56000, wholesale=40000, min_qty=5, tiers=[(5, 48000), (20, 40000), (50, 34000)], available=163, reserved=0),
            dict(id=270, size='98-104', color='Sariq', sku='KD-08-98-104', retail=56000, wholesale=40000, min_qty=5, tiers=[(5, 48000), (20, 40000), (50, 34000)], available=153, reserved=0),
            dict(id=271, size='104-110', color='Sariq', sku='KD-08-104-110', retail=56000, wholesale=40000, min_qty=5, tiers=[(5, 48000), (20, 40000), (50, 34000)], available=30, reserved=0),
            dict(id=272, size='110-116', color='Sariq', sku='KD-08-110-116', retail=56000, wholesale=40000, min_qty=5, tiers=[(5, 48000), (20, 40000), (50, 34000)], available=95, reserved=0),
        ],
    },
    {
        'id': 49, 'title': 'Kostyumcha “Cheerful Kids”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=273, size='92-98', color='Yashil', sku='KD-09-92-98', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=137, reserved=0),
            dict(id=274, size='98-104', color='Yashil', sku='KD-09-98-104', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=143, reserved=0),
            dict(id=275, size='104-110', color='Yashil', sku='KD-09-104-110', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=150, reserved=0),
            dict(id=276, size='110-116', color='Yashil', sku='KD-09-110-116', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=55, reserved=0),
        ],
    },
    {
        'id': 50, 'title': 'Yengil palto “Tiny Trend”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=277, size='92-98', color='Yashil', sku='KD-10-92-98', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=35, reserved=0),
            dict(id=278, size='98-104', color='Yashil', sku='KD-10-98-104', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=62, reserved=0),
            dict(id=279, size='104-110', color='Yashil', sku='KD-10-104-110', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=32, reserved=0),
            dict(id=280, size='110-116', color='Yashil', sku='KD-10-110-116', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=167, reserved=0),
        ],
    },
    {
        'id': 51, 'title': "Trikotaj to'plam “Sweet Panda”", 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=281, size='92-98', color='Pushti', sku='KD-11-92-98', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=118, reserved=0),
            dict(id=282, size='98-104', color='Pushti', sku='KD-11-98-104', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=45, reserved=0),
            dict(id=283, size='104-110', color='Pushti', sku='KD-11-104-110', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=160, reserved=0),
            dict(id=284, size='110-116', color='Pushti', sku='KD-11-110-116', retail=48000, wholesale=35000, min_qty=5, tiers=[(5, 41000), (20, 35000), (50, 29000)], available=78, reserved=0),
        ],
    },
    {
        'id': 52, 'title': 'Pijama “Baby Silk”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=285, size='92-98', color='Sariq', sku='KD-12-92-98', retail=74000, wholesale=53000, min_qty=5, tiers=[(5, 63000), (20, 53000), (50, 44000)], available=173, reserved=0),
            dict(id=286, size='98-104', color='Sariq', sku='KD-12-98-104', retail=74000, wholesale=53000, min_qty=5, tiers=[(5, 63000), (20, 53000), (50, 44000)], available=35, reserved=0),
            dict(id=287, size='104-110', color='Sariq', sku='KD-12-104-110', retail=74000, wholesale=53000, min_qty=5, tiers=[(5, 63000), (20, 53000), (50, 44000)], available=122, reserved=0),
            dict(id=288, size='110-116', color='Sariq', sku='KD-12-110-116', retail=74000, wholesale=53000, min_qty=5, tiers=[(5, 63000), (20, 53000), (50, 44000)], available=164, reserved=0),
        ],
    },
    {
        'id': 53, 'title': 'Qishki kurtka “Kids Joy”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=289, size='92-98', color="Ko'k", sku='KD-13-92-98', retail=73000, wholesale=53000, min_qty=5, tiers=[(5, 62000), (20, 53000), (50, 44000)], available=81, reserved=0),
            dict(id=290, size='98-104', color="Ko'k", sku='KD-13-98-104', retail=73000, wholesale=53000, min_qty=5, tiers=[(5, 62000), (20, 53000), (50, 44000)], available=67, reserved=0),
            dict(id=291, size='104-110', color="Ko'k", sku='KD-13-104-110', retail=73000, wholesale=53000, min_qty=5, tiers=[(5, 62000), (20, 53000), (50, 44000)], available=95, reserved=0),
            dict(id=292, size='110-116', color="Ko'k", sku='KD-13-110-116', retail=73000, wholesale=53000, min_qty=5, tiers=[(5, 62000), (20, 53000), (50, 44000)], available=76, reserved=0),
        ],
    },
    {
        'id': 54, 'title': 'Sport kostyumcha “Little Fox”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=293, size='92-98', color='Pushti', sku='KD-14-92-98', retail=58000, wholesale=42000, min_qty=5, tiers=[(5, 49000), (20, 42000), (50, 35000)], available=180, reserved=0),
            dict(id=294, size='98-104', color='Pushti', sku='KD-14-98-104', retail=58000, wholesale=42000, min_qty=5, tiers=[(5, 49000), (20, 42000), (50, 35000)], available=91, reserved=0),
            dict(id=295, size='104-110', color='Pushti', sku='KD-14-104-110', retail=58000, wholesale=42000, min_qty=5, tiers=[(5, 49000), (20, 42000), (50, 35000)], available=132, reserved=0),
            dict(id=296, size='110-116', color='Pushti', sku='KD-14-110-116', retail=58000, wholesale=42000, min_qty=5, tiers=[(5, 49000), (20, 42000), (50, 35000)], available=95, reserved=0),
        ],
    },
    {
        'id': 55, 'title': 'Jinsi shimcha “Playful Bear”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=297, size='92-98', color='Sariq', sku='KD-15-92-98', retail=91000, wholesale=66000, min_qty=5, tiers=[(5, 77000), (20, 66000), (50, 55000)], available=17, reserved=0),
            dict(id=298, size='98-104', color='Sariq', sku='KD-15-98-104', retail=91000, wholesale=66000, min_qty=5, tiers=[(5, 77000), (20, 66000), (50, 55000)], available=132, reserved=0),
            dict(id=299, size='104-110', color='Sariq', sku='KD-15-104-110', retail=91000, wholesale=66000, min_qty=5, tiers=[(5, 77000), (20, 66000), (50, 55000)], available=174, reserved=0),
            dict(id=300, size='110-116', color='Sariq', sku='KD-15-110-116', retail=91000, wholesale=66000, min_qty=5, tiers=[(5, 77000), (20, 66000), (50, 55000)], available=159, reserved=0),
        ],
    },
    {
        'id': 56, 'title': 'Yubkacha “Sunshine Kids”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=301, size='92-98', color='Sariq', sku='KD-16-92-98', retail=95000, wholesale=68000, min_qty=5, tiers=[(5, 81000), (20, 68000), (50, 57000)], available=152, reserved=0),
            dict(id=302, size='98-104', color='Sariq', sku='KD-16-98-104', retail=95000, wholesale=68000, min_qty=5, tiers=[(5, 81000), (20, 68000), (50, 57000)], available=69, reserved=0),
            dict(id=303, size='104-110', color='Sariq', sku='KD-16-104-110', retail=95000, wholesale=68000, min_qty=5, tiers=[(5, 81000), (20, 68000), (50, 57000)], available=144, reserved=0),
            dict(id=304, size='110-116', color='Sariq', sku='KD-16-110-116', retail=95000, wholesale=68000, min_qty=5, tiers=[(5, 81000), (20, 68000), (50, 57000)], available=82, reserved=0),
        ],
    },
    {
        'id': 57, 'title': 'Maykacha “Baby Cloud”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=305, size='92-98', color="Ko'k", sku='KD-17-92-98', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=32, reserved=0),
            dict(id=306, size='98-104', color="Ko'k", sku='KD-17-98-104', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=77, reserved=0),
            dict(id=307, size='104-110', color="Ko'k", sku='KD-17-104-110', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=109, reserved=0),
            dict(id=308, size='110-116', color="Ko'k", sku='KD-17-110-116', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=87, reserved=0),
        ],
    },
    {
        'id': 58, 'title': 'Qishki kombinezon “Kids Bloom”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=309, size='92-98', color='Yashil', sku='KD-18-92-98', retail=53000, wholesale=38000, min_qty=5, tiers=[(5, 45000), (20, 38000), (50, 32000)], available=92, reserved=0),
            dict(id=310, size='98-104', color='Yashil', sku='KD-18-98-104', retail=53000, wholesale=38000, min_qty=5, tiers=[(5, 45000), (20, 38000), (50, 32000)], available=171, reserved=0),
            dict(id=311, size='104-110', color='Yashil', sku='KD-18-104-110', retail=53000, wholesale=38000, min_qty=5, tiers=[(5, 45000), (20, 38000), (50, 32000)], available=150, reserved=0),
            dict(id=312, size='110-116', color='Yashil', sku='KD-18-110-116', retail=53000, wholesale=38000, min_qty=5, tiers=[(5, 45000), (20, 38000), (50, 32000)], available=17, reserved=0),
        ],
    },
    {
        'id': 59, 'title': 'Trikotaj sviter “Little Moon”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=313, size='92-98', color='Yashil', sku='KD-19-92-98', retail=78000, wholesale=56000, min_qty=5, tiers=[(5, 66000), (20, 56000), (50, 47000)], available=91, reserved=0),
            dict(id=314, size='98-104', color='Yashil', sku='KD-19-98-104', retail=78000, wholesale=56000, min_qty=5, tiers=[(5, 66000), (20, 56000), (50, 47000)], available=41, reserved=0),
            dict(id=315, size='104-110', color='Yashil', sku='KD-19-104-110', retail=78000, wholesale=56000, min_qty=5, tiers=[(5, 66000), (20, 56000), (50, 47000)], available=49, reserved=0),
            dict(id=316, size='110-116', color='Yashil', sku='KD-19-110-116', retail=78000, wholesale=56000, min_qty=5, tiers=[(5, 66000), (20, 56000), (50, 47000)], available=82, reserved=0),
        ],
    },
    {
        'id': 60, 'title': 'Yengil jaketcha “Giggle Line”', 'category_id': 'bolalar-kiyimi',
        'origin': 'Xitoy', 'icon': '🧸', 'variants': [
            dict(id=317, size='92-98', color='Sariq', sku='KD-20-92-98', retail=51000, wholesale=37000, min_qty=5, tiers=[(5, 43000), (20, 37000), (50, 31000)], available=156, reserved=0),
            dict(id=318, size='98-104', color='Sariq', sku='KD-20-98-104', retail=51000, wholesale=37000, min_qty=5, tiers=[(5, 43000), (20, 37000), (50, 31000)], available=54, reserved=0),
            dict(id=319, size='104-110', color='Sariq', sku='KD-20-104-110', retail=51000, wholesale=37000, min_qty=5, tiers=[(5, 43000), (20, 37000), (50, 31000)], available=84, reserved=0),
            dict(id=320, size='110-116', color='Sariq', sku='KD-20-110-116', retail=51000, wholesale=37000, min_qty=5, tiers=[(5, 43000), (20, 37000), (50, 31000)], available=87, reserved=0),
        ],
    },
    {
        'id': 61, 'title': 'Chaqaloq bodisi “Tiny Angel”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=321, size='0-3 oy', color='Pushti', sku='BB-01-0-3OY', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=67, reserved=0),
            dict(id=322, size='3-6 oy', color='Pushti', sku='BB-01-3-6OY', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=177, reserved=0),
            dict(id=323, size='6-9 oy', color='Pushti', sku='BB-01-6-9OY', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=82, reserved=0),
            dict(id=324, size='9-12 oy', color='Pushti', sku='BB-01-9-12OY', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=144, reserved=0),
        ],
    },
    {
        'id': 62, 'title': 'Chaqaloq kombinezoni “Soft Cloud Baby”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=325, size='0-3 oy', color='Oq', sku='BB-02-0-3OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=38, reserved=0),
            dict(id=326, size='3-6 oy', color='Oq', sku='BB-02-3-6OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=177, reserved=0),
            dict(id=327, size='6-9 oy', color='Oq', sku='BB-02-6-9OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=123, reserved=0),
            dict(id=328, size='9-12 oy', color='Oq', sku='BB-02-9-12OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=85, reserved=0),
        ],
    },
    {
        'id': 63, 'title': "Chaqaloq ko'ylakchasi “Little Bunny”", 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=329, size='0-3 oy', color='Pushti', sku='BB-03-0-3OY', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=48, reserved=0),
            dict(id=330, size='3-6 oy', color='Pushti', sku='BB-03-3-6OY', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=178, reserved=0),
            dict(id=331, size='6-9 oy', color='Pushti', sku='BB-03-6-9OY', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=82, reserved=0),
            dict(id=332, size='9-12 oy', color='Pushti', sku='BB-03-9-12OY', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=56, reserved=0),
        ],
    },
    {
        'id': 64, 'title': 'Chaqaloq shimchasi “Cozy Nest”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=333, size='0-3 oy', color='Assorti', sku='BB-04-0-3OY', retail=60000, wholesale=43000, min_qty=5, tiers=[(5, 51000), (20, 43000), (50, 36000)], available=124, reserved=0),
            dict(id=334, size='3-6 oy', color='Assorti', sku='BB-04-3-6OY', retail=60000, wholesale=43000, min_qty=5, tiers=[(5, 51000), (20, 43000), (50, 36000)], available=158, reserved=0),
            dict(id=335, size='6-9 oy', color='Assorti', sku='BB-04-6-9OY', retail=60000, wholesale=43000, min_qty=5, tiers=[(5, 51000), (20, 43000), (50, 36000)], available=17, reserved=0),
            dict(id=336, size='9-12 oy', color='Assorti', sku='BB-04-9-12OY', retail=60000, wholesale=43000, min_qty=5, tiers=[(5, 51000), (20, 43000), (50, 36000)], available=43, reserved=0),
        ],
    },
    {
        'id': 65, 'title': 'Chaqaloq sviterchasi “Baby Dream”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=337, size='0-3 oy', color='Sariq', sku='BB-05-0-3OY', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=154, reserved=0),
            dict(id=338, size='3-6 oy', color='Sariq', sku='BB-05-3-6OY', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=24, reserved=0),
            dict(id=339, size='6-9 oy', color='Sariq', sku='BB-05-6-9OY', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=109, reserved=0),
            dict(id=340, size='9-12 oy', color='Sariq', sku='BB-05-9-12OY', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=164, reserved=0),
        ],
    },
    {
        'id': 66, 'title': 'Chaqaloq kurtkachasi “Sweet Cocoon”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=341, size='0-3 oy', color="Ko'k", sku='BB-06-0-3OY', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=47, reserved=0),
            dict(id=342, size='3-6 oy', color="Ko'k", sku='BB-06-3-6OY', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=25, reserved=0),
            dict(id=343, size='6-9 oy', color="Ko'k", sku='BB-06-6-9OY', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=93, reserved=0),
            dict(id=344, size='9-12 oy', color="Ko'k", sku='BB-06-9-12OY', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=108, reserved=0),
        ],
    },
    {
        'id': 67, 'title': 'Chaqaloq adyol-konverti “Little Lamb”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=345, size='0-3 oy', color='Oq', sku='BB-07-0-3OY', retail=66000, wholesale=48000, min_qty=5, tiers=[(5, 56000), (20, 48000), (50, 40000)], available=106, reserved=0),
            dict(id=346, size='3-6 oy', color='Oq', sku='BB-07-3-6OY', retail=66000, wholesale=48000, min_qty=5, tiers=[(5, 56000), (20, 48000), (50, 40000)], available=68, reserved=0),
            dict(id=347, size='6-9 oy', color='Oq', sku='BB-07-6-9OY', retail=66000, wholesale=48000, min_qty=5, tiers=[(5, 56000), (20, 48000), (50, 40000)], available=78, reserved=0),
            dict(id=348, size='9-12 oy', color='Oq', sku='BB-07-9-12OY', retail=66000, wholesale=48000, min_qty=5, tiers=[(5, 56000), (20, 48000), (50, 40000)], available=41, reserved=0),
        ],
    },
    {
        'id': 68, 'title': 'Chaqaloq shapkachasi “Gentle Start”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=349, size='0-3 oy', color='Assorti', sku='BB-08-0-3OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=119, reserved=0),
            dict(id=350, size='3-6 oy', color='Assorti', sku='BB-08-3-6OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=173, reserved=0),
            dict(id=351, size='6-9 oy', color='Assorti', sku='BB-08-6-9OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=54, reserved=0),
            dict(id=352, size='9-12 oy', color='Assorti', sku='BB-08-9-12OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=75, reserved=0),
        ],
    },
    {
        'id': 69, 'title': "Chaqaloq qo'lqopchasi “Baby Bloom”", 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=353, size='0-3 oy', color='Sariq', sku='BB-09-0-3OY', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=120, reserved=0),
            dict(id=354, size='3-6 oy', color='Sariq', sku='BB-09-3-6OY', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=21, reserved=0),
            dict(id=355, size='6-9 oy', color='Sariq', sku='BB-09-6-9OY', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=60, reserved=0),
            dict(id=356, size='9-12 oy', color='Sariq', sku='BB-09-9-12OY', retail=65000, wholesale=47000, min_qty=5, tiers=[(5, 55000), (20, 47000), (50, 39000)], available=100, reserved=0),
        ],
    },
    {
        'id': 70, 'title': 'Chaqaloq noskichasi “Tender Moon”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=357, size='0-3 oy', color="Ko'k", sku='BB-10-0-3OY', retail=61000, wholesale=44000, min_qty=5, tiers=[(5, 52000), (20, 44000), (50, 37000)], available=78, reserved=0),
            dict(id=358, size='3-6 oy', color="Ko'k", sku='BB-10-3-6OY', retail=61000, wholesale=44000, min_qty=5, tiers=[(5, 52000), (20, 44000), (50, 37000)], available=83, reserved=0),
            dict(id=359, size='6-9 oy', color="Ko'k", sku='BB-10-6-9OY', retail=61000, wholesale=44000, min_qty=5, tiers=[(5, 52000), (20, 44000), (50, 37000)], available=55, reserved=0),
            dict(id=360, size='9-12 oy', color="Ko'k", sku='BB-10-9-12OY', retail=61000, wholesale=44000, min_qty=5, tiers=[(5, 52000), (20, 44000), (50, 37000)], available=42, reserved=0),
        ],
    },
    {
        'id': 71, 'title': 'Chaqaloq pijamachasi “Little Whisper”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=361, size='0-3 oy', color='Oq', sku='BB-11-0-3OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=135, reserved=0),
            dict(id=362, size='3-6 oy', color='Oq', sku='BB-11-3-6OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=71, reserved=0),
            dict(id=363, size='6-9 oy', color='Oq', sku='BB-11-6-9OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=66, reserved=0),
            dict(id=364, size='9-12 oy', color='Oq', sku='BB-11-9-12OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=132, reserved=0),
        ],
    },
    {
        'id': 72, 'title': 'Chaqaloq sarafonchasi “Baby Cuddle”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=365, size='0-3 oy', color='Sariq', sku='BB-12-0-3OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=72, reserved=0),
            dict(id=366, size='3-6 oy', color='Sariq', sku='BB-12-3-6OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=21, reserved=0),
            dict(id=367, size='6-9 oy', color='Sariq', sku='BB-12-6-9OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=64, reserved=0),
            dict(id=368, size='9-12 oy', color='Sariq', sku='BB-12-9-12OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=117, reserved=0),
        ],
    },
    {
        'id': 73, 'title': 'Chaqaloq fartukchasi “Soft Petal”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=369, size='0-3 oy', color='Oq', sku='BB-13-0-3OY', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=86, reserved=0),
            dict(id=370, size='3-6 oy', color='Oq', sku='BB-13-3-6OY', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=104, reserved=0),
            dict(id=371, size='6-9 oy', color='Oq', sku='BB-13-6-9OY', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=179, reserved=0),
            dict(id=372, size='9-12 oy', color='Oq', sku='BB-13-9-12OY', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=145, reserved=0),
        ],
    },
    {
        'id': 74, 'title': 'Chaqaloq uxlash qopi “Little Sunbeam”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=373, size='0-3 oy', color='Assorti', sku='BB-14-0-3OY', retail=46000, wholesale=33000, min_qty=5, tiers=[(5, 39000), (20, 33000), (50, 28000)], available=99, reserved=0),
            dict(id=374, size='3-6 oy', color='Assorti', sku='BB-14-3-6OY', retail=46000, wholesale=33000, min_qty=5, tiers=[(5, 39000), (20, 33000), (50, 28000)], available=22, reserved=0),
            dict(id=375, size='6-9 oy', color='Assorti', sku='BB-14-6-9OY', retail=46000, wholesale=33000, min_qty=5, tiers=[(5, 39000), (20, 33000), (50, 28000)], available=44, reserved=0),
            dict(id=376, size='9-12 oy', color='Assorti', sku='BB-14-9-12OY', retail=46000, wholesale=33000, min_qty=5, tiers=[(5, 39000), (20, 33000), (50, 28000)], available=81, reserved=0),
        ],
    },
    {
        'id': 75, 'title': "Chaqaloq ust-bosh to'plami “Baby Nest”", 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=377, size='0-3 oy', color='Pushti', sku='BB-15-0-3OY', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=24, reserved=0),
            dict(id=378, size='3-6 oy', color='Pushti', sku='BB-15-3-6OY', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=42, reserved=0),
            dict(id=379, size='6-9 oy', color='Pushti', sku='BB-15-6-9OY', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=167, reserved=0),
            dict(id=380, size='9-12 oy', color='Pushti', sku='BB-15-9-12OY', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=126, reserved=0),
        ],
    },
    {
        'id': 76, 'title': 'Chaqaloq yozgi kiyimi “Cozy Cub”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=381, size='0-3 oy', color='Pushti', sku='BB-16-0-3OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=126, reserved=0),
            dict(id=382, size='3-6 oy', color='Pushti', sku='BB-16-3-6OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=170, reserved=0),
            dict(id=383, size='6-9 oy', color='Pushti', sku='BB-16-6-9OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=145, reserved=0),
            dict(id=384, size='9-12 oy', color='Pushti', sku='BB-16-9-12OY', retail=44000, wholesale=32000, min_qty=5, tiers=[(5, 37000), (20, 32000), (50, 26000)], available=44, reserved=0),
        ],
    },
    {
        'id': 77, 'title': 'Chaqaloq qishki kombinezoni “Little Feather”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=385, size='0-3 oy', color='Assorti', sku='BB-17-0-3OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=63, reserved=0),
            dict(id=386, size='3-6 oy', color='Assorti', sku='BB-17-3-6OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=80, reserved=0),
            dict(id=387, size='6-9 oy', color='Assorti', sku='BB-17-6-9OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=26, reserved=0),
            dict(id=388, size='9-12 oy', color='Assorti', sku='BB-17-9-12OY', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=126, reserved=0),
        ],
    },
    {
        'id': 78, 'title': 'Chaqaloq panamasi “Baby Melody”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=389, size='0-3 oy', color='Assorti', sku='BB-18-0-3OY', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=65, reserved=0),
            dict(id=390, size='3-6 oy', color='Assorti', sku='BB-18-3-6OY', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=108, reserved=0),
            dict(id=391, size='6-9 oy', color='Assorti', sku='BB-18-6-9OY', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=125, reserved=0),
            dict(id=392, size='9-12 oy', color='Assorti', sku='BB-18-9-12OY', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=32, reserved=0),
        ],
    },
    {
        'id': 79, 'title': 'Chaqaloq oyoq kiyimi “Tiny Star”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=393, size='0-3 oy', color='Pushti', sku='BB-19-0-3OY', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=174, reserved=0),
            dict(id=394, size='3-6 oy', color='Pushti', sku='BB-19-3-6OY', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=95, reserved=0),
            dict(id=395, size='6-9 oy', color='Pushti', sku='BB-19-6-9OY', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=46, reserved=0),
            dict(id=396, size='9-12 oy', color='Pushti', sku='BB-19-9-12OY', retail=68000, wholesale=49000, min_qty=5, tiers=[(5, 58000), (20, 49000), (50, 41000)], available=91, reserved=0),
        ],
    },
    {
        'id': 80, 'title': 'Chaqaloq xalatchasi “Sweet Beginning”', 'category_id': 'chaqaloqlar-kiyimi',
        'origin': 'Xitoy', 'icon': '👶', 'variants': [
            dict(id=397, size='0-3 oy', color="Ko'k", sku='BB-20-0-3OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=98, reserved=0),
            dict(id=398, size='3-6 oy', color="Ko'k", sku='BB-20-3-6OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=118, reserved=0),
            dict(id=399, size='6-9 oy', color="Ko'k", sku='BB-20-6-9OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=90, reserved=0),
            dict(id=400, size='9-12 oy', color="Ko'k", sku='BB-20-9-12OY', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=156, reserved=0),
        ],
    },
    {
        'id': 81, 'title': "Ayollar liflik to'plami “Comfort Line”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=401, size='S', color='Bej', sku='UN-01-S', retail=29000, wholesale=21000, min_qty=5, tiers=[(5, 25000), (20, 21000), (50, 17000)], available=112, reserved=0),
            dict(id=402, size='M', color='Bej', sku='UN-01-M', retail=29000, wholesale=21000, min_qty=5, tiers=[(5, 25000), (20, 21000), (50, 17000)], available=59, reserved=0),
            dict(id=403, size='L', color='Bej', sku='UN-01-L', retail=29000, wholesale=21000, min_qty=5, tiers=[(5, 25000), (20, 21000), (50, 17000)], available=172, reserved=0),
        ],
    },
    {
        'id': 82, 'title': "Erkaklar boxer to'plami (3 dona) “Soft Touch”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=404, size='S', color='Bej', sku='UN-02-S', retail=42000, wholesale=30000, min_qty=5, tiers=[(5, 36000), (20, 30000), (50, 25000)], available=155, reserved=0),
            dict(id=405, size='M', color='Bej', sku='UN-02-M', retail=42000, wholesale=30000, min_qty=5, tiers=[(5, 36000), (20, 30000), (50, 25000)], available=15, reserved=0),
            dict(id=406, size='L', color='Bej', sku='UN-02-L', retail=42000, wholesale=30000, min_qty=5, tiers=[(5, 36000), (20, 30000), (50, 25000)], available=92, reserved=0),
        ],
    },
    {
        'id': 83, 'title': 'Bolalar paxta ich kiyim “Pure Cotton”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=407, size='S', color='Bej', sku='UN-03-S', retail=34000, wholesale=24000, min_qty=5, tiers=[(5, 29000), (20, 24000), (50, 20000)], available=163, reserved=0),
            dict(id=408, size='M', color='Bej', sku='UN-03-M', retail=34000, wholesale=24000, min_qty=5, tiers=[(5, 29000), (20, 24000), (50, 20000)], available=170, reserved=0),
            dict(id=409, size='L', color='Bej', sku='UN-03-L', retail=34000, wholesale=24000, min_qty=5, tiers=[(5, 29000), (20, 24000), (50, 20000)], available=97, reserved=0),
        ],
    },
    {
        'id': 84, 'title': 'Termo komplekt “Silk Road”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=410, size='S', color='Bej', sku='UN-04-S', retail=39000, wholesale=28000, min_qty=5, tiers=[(5, 33000), (20, 28000), (50, 23000)], available=69, reserved=0),
            dict(id=411, size='M', color='Bej', sku='UN-04-M', retail=39000, wholesale=28000, min_qty=5, tiers=[(5, 33000), (20, 28000), (50, 23000)], available=145, reserved=0),
            dict(id=412, size='L', color='Bej', sku='UN-04-L', retail=39000, wholesale=28000, min_qty=5, tiers=[(5, 33000), (20, 28000), (50, 23000)], available=136, reserved=0),
        ],
    },
    {
        'id': 85, 'title': 'Ayollar trusigi (5 dona) “East Comfort”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=413, size='S', color='Qora', sku='UN-05-S', retail=49000, wholesale=35000, min_qty=5, tiers=[(5, 42000), (20, 35000), (50, 29000)], available=36, reserved=0),
            dict(id=414, size='M', color='Qora', sku='UN-05-M', retail=49000, wholesale=35000, min_qty=5, tiers=[(5, 42000), (20, 35000), (50, 29000)], available=87, reserved=0),
            dict(id=415, size='L', color='Qora', sku='UN-05-L', retail=49000, wholesale=35000, min_qty=5, tiers=[(5, 42000), (20, 35000), (50, 29000)], available=146, reserved=0),
        ],
    },
    {
        'id': 86, 'title': 'Erkaklar maykasi “Cloud Soft”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=416, size='S', color="Ko'k", sku='UN-06-S', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=100, reserved=0),
            dict(id=417, size='M', color="Ko'k", sku='UN-06-M', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=38, reserved=0),
            dict(id=418, size='L', color="Ko'k", sku='UN-06-L', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=75, reserved=0),
        ],
    },
    {
        'id': 87, 'title': 'Sport liflik “Modal Line”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=419, size='S', color='Qora', sku='UN-07-S', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=65, reserved=0),
            dict(id=420, size='M', color='Qora', sku='UN-07-M', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=52, reserved=0),
            dict(id=421, size='L', color='Qora', sku='UN-07-L', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=21, reserved=0),
        ],
    },
    {
        'id': 88, 'title': "Modal ich kiyim to'plami “Daily Wear”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=422, size='S', color='Bej', sku='UN-08-S', retail=26000, wholesale=19000, min_qty=5, tiers=[(5, 22000), (20, 19000), (50, 16000)], available=171, reserved=0),
            dict(id=423, size='M', color='Bej', sku='UN-08-M', retail=26000, wholesale=19000, min_qty=5, tiers=[(5, 22000), (20, 19000), (50, 16000)], available=33, reserved=0),
            dict(id=424, size='L', color='Bej', sku='UN-08-L', retail=26000, wholesale=19000, min_qty=5, tiers=[(5, 22000), (20, 19000), (50, 16000)], available=131, reserved=0),
        ],
    },
    {
        'id': 89, 'title': "Bolalar shortik to'plami “Gentle Fit”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=425, size='S', color="Ko'k", sku='UN-09-S', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=64, reserved=0),
            dict(id=426, size='M', color="Ko'k", sku='UN-09-M', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=113, reserved=0),
            dict(id=427, size='L', color="Ko'k", sku='UN-09-L', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=141, reserved=0),
        ],
    },
    {
        'id': 90, 'title': 'Paxta noski (5 juft) “Homey Line”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=428, size='S', color='Qora', sku='UN-10-S', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=16, reserved=0),
            dict(id=429, size='M', color='Qora', sku='UN-10-M', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=42, reserved=0),
            dict(id=430, size='L', color='Qora', sku='UN-10-L', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=123, reserved=0),
        ],
    },
    {
        'id': 91, 'title': 'Korset “Breeze”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=431, size='S', color="Ko'k", sku='UN-11-S', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=133, reserved=0),
            dict(id=432, size='M', color="Ko'k", sku='UN-11-M', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=27, reserved=0),
            dict(id=433, size='L', color="Ko'k", sku='UN-11-L', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=157, reserved=0),
        ],
    },
    {
        'id': 92, 'title': "Uy kiyimi (pijama) to'plami “Calm Line”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=434, size='S', color='Oq', sku='UN-12-S', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=131, reserved=0),
            dict(id=435, size='M', color='Oq', sku='UN-12-M', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=49, reserved=0),
            dict(id=436, size='L', color='Oq', sku='UN-12-L', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=133, reserved=0),
        ],
    },
    {
        'id': 93, 'title': "Ayollar shortigi to'plami “Cozy Line”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=437, size='S', color="Ko'k", sku='UN-13-S', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=167, reserved=0),
            dict(id=438, size='M', color="Ko'k", sku='UN-13-M', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=96, reserved=0),
            dict(id=439, size='L', color="Ko'k", sku='UN-13-L', retail=45000, wholesale=32000, min_qty=5, tiers=[(5, 38000), (20, 32000), (50, 27000)], available=128, reserved=0),
        ],
    },
    {
        'id': 94, 'title': "Erkaklar maykasi to'plami (3 dona) “Light Touch”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=440, size='S', color="Ko'k", sku='UN-14-S', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=124, reserved=0),
            dict(id=441, size='M', color="Ko'k", sku='UN-14-M', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=155, reserved=0),
            dict(id=442, size='L', color="Ko'k", sku='UN-14-L', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=129, reserved=0),
        ],
    },
    {
        'id': 95, 'title': 'Sport shortik “Pure Line”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=443, size='S', color='Bej', sku='UN-15-S', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=130, reserved=0),
            dict(id=444, size='M', color='Bej', sku='UN-15-M', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=81, reserved=0),
            dict(id=445, size='L', color='Bej', sku='UN-15-L', retail=52000, wholesale=37000, min_qty=5, tiers=[(5, 44000), (20, 37000), (50, 31000)], available=78, reserved=0),
        ],
    },
    {
        'id': 96, 'title': 'Bolalar maykachasi “Soft Cloud”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=446, size='S', color='Assorti', sku='UN-16-S', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=148, reserved=0),
            dict(id=447, size='M', color='Assorti', sku='UN-16-M', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=139, reserved=0),
            dict(id=448, size='L', color='Assorti', sku='UN-16-L', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=175, reserved=0),
        ],
    },
    {
        'id': 97, 'title': 'Termo shim “Tender Fit”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=449, size='S', color='Bej', sku='UN-17-S', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=34, reserved=0),
            dict(id=450, size='M', color='Bej', sku='UN-17-M', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=88, reserved=0),
            dict(id=451, size='L', color='Bej', sku='UN-17-L', retail=32000, wholesale=23000, min_qty=5, tiers=[(5, 27000), (20, 23000), (50, 19000)], available=75, reserved=0),
        ],
    },
    {
        'id': 98, 'title': "Ayollar tungi ko'ylagi “Easy Wear”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=452, size='S', color='Assorti', sku='UN-18-S', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=153, reserved=0),
            dict(id=453, size='M', color='Assorti', sku='UN-18-M', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=35, reserved=0),
            dict(id=454, size='L', color='Assorti', sku='UN-18-L', retail=33000, wholesale=24000, min_qty=5, tiers=[(5, 28000), (20, 24000), (50, 20000)], available=50, reserved=0),
        ],
    },
    {
        'id': 99, 'title': 'Erkaklar uy kiyimi “Night Comfort”', 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=455, size='S', color='Bej', sku='UN-19-S', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=54, reserved=0),
            dict(id=456, size='M', color='Bej', sku='UN-19-M', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=69, reserved=0),
            dict(id=457, size='L', color='Bej', sku='UN-19-L', retail=30000, wholesale=22000, min_qty=5, tiers=[(5, 26000), (20, 22000), (50, 18000)], available=31, reserved=0),
        ],
    },
    {
        'id': 100, 'title': "Bolalar pijama to'plami “Fresh Line”", 'category_id': 'ich-kiyim',
        'origin': 'Xitoy', 'icon': '🩱', 'variants': [
            dict(id=458, size='S', color='Assorti', sku='UN-20-S', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=153, reserved=0),
            dict(id=459, size='M', color='Assorti', sku='UN-20-M', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=134, reserved=0),
            dict(id=460, size='L', color='Assorti', sku='UN-20-L', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=121, reserved=0),
        ],
    },
    {
        'id': 101, 'title': 'Sport krossovka “Marmaris”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=461, size='39', color='Kulrang', sku='SH-01-39', retail=195000, wholesale=140000, min_qty=5, tiers=[(5, 166000), (20, 140000), (50, 117000)], available=114, reserved=0),
            dict(id=462, size='40', color='Kulrang', sku='SH-01-40', retail=195000, wholesale=140000, min_qty=5, tiers=[(5, 166000), (20, 140000), (50, 117000)], available=164, reserved=0),
            dict(id=463, size='41', color='Kulrang', sku='SH-01-41', retail=195000, wholesale=140000, min_qty=5, tiers=[(5, 166000), (20, 140000), (50, 117000)], available=20, reserved=0),
            dict(id=464, size='42', color='Kulrang', sku='SH-01-42', retail=195000, wholesale=140000, min_qty=5, tiers=[(5, 166000), (20, 140000), (50, 117000)], available=162, reserved=0),
        ],
    },
    {
        'id': 102, 'title': 'Botinka “Cesme”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=465, size='39', color='Qora', sku='SH-02-39', retail=271000, wholesale=195000, min_qty=5, tiers=[(5, 230000), (20, 195000), (50, 163000)], available=105, reserved=0),
            dict(id=466, size='40', color='Qora', sku='SH-02-40', retail=271000, wholesale=195000, min_qty=5, tiers=[(5, 230000), (20, 195000), (50, 163000)], available=91, reserved=0),
            dict(id=467, size='41', color='Qora', sku='SH-02-41', retail=271000, wholesale=195000, min_qty=5, tiers=[(5, 230000), (20, 195000), (50, 163000)], available=114, reserved=0),
            dict(id=468, size='42', color='Qora', sku='SH-02-42', retail=271000, wholesale=195000, min_qty=5, tiers=[(5, 230000), (20, 195000), (50, 163000)], available=122, reserved=0),
        ],
    },
    {
        'id': 103, 'title': 'Klassik tufli “Fethiye”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=469, size='39', color='Oq', sku='SH-03-39', retail=309000, wholesale=222000, min_qty=5, tiers=[(5, 263000), (20, 222000), (50, 185000)], available=139, reserved=0),
            dict(id=470, size='40', color='Oq', sku='SH-03-40', retail=309000, wholesale=222000, min_qty=5, tiers=[(5, 263000), (20, 222000), (50, 185000)], available=71, reserved=0),
            dict(id=471, size='41', color='Oq', sku='SH-03-41', retail=309000, wholesale=222000, min_qty=5, tiers=[(5, 263000), (20, 222000), (50, 185000)], available=84, reserved=0),
            dict(id=472, size='42', color='Oq', sku='SH-03-42', retail=309000, wholesale=222000, min_qty=5, tiers=[(5, 263000), (20, 222000), (50, 185000)], available=126, reserved=0),
        ],
    },
    {
        'id': 104, 'title': 'Sandal “Pamukkale”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=473, size='39', color='Kulrang', sku='SH-04-39', retail=297000, wholesale=214000, min_qty=5, tiers=[(5, 252000), (20, 214000), (50, 178000)], available=101, reserved=0),
            dict(id=474, size='40', color='Kulrang', sku='SH-04-40', retail=297000, wholesale=214000, min_qty=5, tiers=[(5, 252000), (20, 214000), (50, 178000)], available=118, reserved=0),
            dict(id=475, size='41', color='Kulrang', sku='SH-04-41', retail=297000, wholesale=214000, min_qty=5, tiers=[(5, 252000), (20, 214000), (50, 178000)], available=57, reserved=0),
            dict(id=476, size='42', color='Kulrang', sku='SH-04-42', retail=297000, wholesale=214000, min_qty=5, tiers=[(5, 252000), (20, 214000), (50, 178000)], available=134, reserved=0),
        ],
    },
    {
        'id': 105, 'title': 'Uy shippagi “Alanya”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=477, size='39', color='Qora', sku='SH-05-39', retail=401000, wholesale=289000, min_qty=5, tiers=[(5, 341000), (20, 289000), (50, 241000)], available=115, reserved=0),
            dict(id=478, size='40', color='Qora', sku='SH-05-40', retail=401000, wholesale=289000, min_qty=5, tiers=[(5, 341000), (20, 289000), (50, 241000)], available=166, reserved=0),
            dict(id=479, size='41', color='Qora', sku='SH-05-41', retail=401000, wholesale=289000, min_qty=5, tiers=[(5, 341000), (20, 289000), (50, 241000)], available=159, reserved=0),
            dict(id=480, size='42', color='Qora', sku='SH-05-42', retail=401000, wholesale=289000, min_qty=5, tiers=[(5, 341000), (20, 289000), (50, 241000)], available=21, reserved=0),
        ],
    },
    {
        'id': 106, 'title': "Yig'ma etik “Side Step”", 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=481, size='39', color='Kulrang', sku='SH-06-39', retail=200000, wholesale=144000, min_qty=5, tiers=[(5, 170000), (20, 144000), (50, 120000)], available=49, reserved=0),
            dict(id=482, size='40', color='Kulrang', sku='SH-06-40', retail=200000, wholesale=144000, min_qty=5, tiers=[(5, 170000), (20, 144000), (50, 120000)], available=133, reserved=0),
            dict(id=483, size='41', color='Kulrang', sku='SH-06-41', retail=200000, wholesale=144000, min_qty=5, tiers=[(5, 170000), (20, 144000), (50, 120000)], available=61, reserved=0),
            dict(id=484, size='42', color='Kulrang', sku='SH-06-42', retail=200000, wholesale=144000, min_qty=5, tiers=[(5, 170000), (20, 144000), (50, 120000)], available=27, reserved=0),
        ],
    },
    {
        'id': 107, 'title': 'Mokasin “Kusadasi”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=485, size='39', color='Jigarrang', sku='SH-07-39', retail=242000, wholesale=174000, min_qty=5, tiers=[(5, 206000), (20, 174000), (50, 145000)], available=69, reserved=0),
            dict(id=486, size='40', color='Jigarrang', sku='SH-07-40', retail=242000, wholesale=174000, min_qty=5, tiers=[(5, 206000), (20, 174000), (50, 145000)], available=131, reserved=0),
            dict(id=487, size='41', color='Jigarrang', sku='SH-07-41', retail=242000, wholesale=174000, min_qty=5, tiers=[(5, 206000), (20, 174000), (50, 145000)], available=98, reserved=0),
            dict(id=488, size='42', color='Jigarrang', sku='SH-07-42', retail=242000, wholesale=174000, min_qty=5, tiers=[(5, 206000), (20, 174000), (50, 145000)], available=101, reserved=0),
        ],
    },
    {
        'id': 108, 'title': 'Yengil kedi “Bursa Step”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=489, size='39', color='Kulrang', sku='SH-08-39', retail=363000, wholesale=261000, min_qty=5, tiers=[(5, 309000), (20, 261000), (50, 218000)], available=86, reserved=0),
            dict(id=490, size='40', color='Kulrang', sku='SH-08-40', retail=363000, wholesale=261000, min_qty=5, tiers=[(5, 309000), (20, 261000), (50, 218000)], available=122, reserved=0),
            dict(id=491, size='41', color='Kulrang', sku='SH-08-41', retail=363000, wholesale=261000, min_qty=5, tiers=[(5, 309000), (20, 261000), (50, 218000)], available=79, reserved=0),
            dict(id=492, size='42', color='Kulrang', sku='SH-08-42', retail=363000, wholesale=261000, min_qty=5, tiers=[(5, 309000), (20, 261000), (50, 218000)], available=35, reserved=0),
        ],
    },
    {
        'id': 109, 'title': 'Bolalar krossovkasi “Denizli Sole”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=493, size='39', color='Qora', sku='SH-09-39', retail=293000, wholesale=211000, min_qty=5, tiers=[(5, 249000), (20, 211000), (50, 176000)], available=104, reserved=0),
            dict(id=494, size='40', color='Qora', sku='SH-09-40', retail=293000, wholesale=211000, min_qty=5, tiers=[(5, 249000), (20, 211000), (50, 176000)], available=72, reserved=0),
            dict(id=495, size='41', color='Qora', sku='SH-09-41', retail=293000, wholesale=211000, min_qty=5, tiers=[(5, 249000), (20, 211000), (50, 176000)], available=32, reserved=0),
            dict(id=496, size='42', color='Qora', sku='SH-09-42', retail=293000, wholesale=211000, min_qty=5, tiers=[(5, 249000), (20, 211000), (50, 176000)], available=25, reserved=0),
        ],
    },
    {
        'id': 110, 'title': 'Baland poshnali tufli “Usak”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=497, size='39', color='Oq', sku='SH-10-39', retail=361000, wholesale=260000, min_qty=5, tiers=[(5, 307000), (20, 260000), (50, 217000)], available=66, reserved=0),
            dict(id=498, size='40', color='Oq', sku='SH-10-40', retail=361000, wholesale=260000, min_qty=5, tiers=[(5, 307000), (20, 260000), (50, 217000)], available=20, reserved=0),
            dict(id=499, size='41', color='Oq', sku='SH-10-41', retail=361000, wholesale=260000, min_qty=5, tiers=[(5, 307000), (20, 260000), (50, 217000)], available=174, reserved=0),
            dict(id=500, size='42', color='Oq', sku='SH-10-42', retail=361000, wholesale=260000, min_qty=5, tiers=[(5, 307000), (20, 260000), (50, 217000)], available=54, reserved=0),
        ],
    },
    {
        'id': 111, 'title': 'Erkaklar klassik tufli “Nevsehir”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=501, size='39', color='Kulrang', sku='SH-11-39', retail=237000, wholesale=171000, min_qty=5, tiers=[(5, 201000), (20, 171000), (50, 142000)], available=44, reserved=0),
            dict(id=502, size='40', color='Kulrang', sku='SH-11-40', retail=237000, wholesale=171000, min_qty=5, tiers=[(5, 201000), (20, 171000), (50, 142000)], available=159, reserved=0),
            dict(id=503, size='41', color='Kulrang', sku='SH-11-41', retail=237000, wholesale=171000, min_qty=5, tiers=[(5, 201000), (20, 171000), (50, 142000)], available=70, reserved=0),
            dict(id=504, size='42', color='Kulrang', sku='SH-11-42', retail=237000, wholesale=171000, min_qty=5, tiers=[(5, 201000), (20, 171000), (50, 142000)], available=134, reserved=0),
        ],
    },
    {
        'id': 112, 'title': 'Yugurish krossovkasi “Safranbolu”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=505, size='39', color='Jigarrang', sku='SH-12-39', retail=348000, wholesale=251000, min_qty=5, tiers=[(5, 296000), (20, 251000), (50, 209000)], available=57, reserved=0),
            dict(id=506, size='40', color='Jigarrang', sku='SH-12-40', retail=348000, wholesale=251000, min_qty=5, tiers=[(5, 296000), (20, 251000), (50, 209000)], available=170, reserved=0),
            dict(id=507, size='41', color='Jigarrang', sku='SH-12-41', retail=348000, wholesale=251000, min_qty=5, tiers=[(5, 296000), (20, 251000), (50, 209000)], available=170, reserved=0),
            dict(id=508, size='42', color='Jigarrang', sku='SH-12-42', retail=348000, wholesale=251000, min_qty=5, tiers=[(5, 296000), (20, 251000), (50, 209000)], available=44, reserved=0),
        ],
    },
    {
        'id': 113, 'title': 'Qishki botinka “Bolu Step”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=509, size='39', color='Oq', sku='SH-13-39', retail=367000, wholesale=264000, min_qty=5, tiers=[(5, 312000), (20, 264000), (50, 220000)], available=94, reserved=0),
            dict(id=510, size='40', color='Oq', sku='SH-13-40', retail=367000, wholesale=264000, min_qty=5, tiers=[(5, 312000), (20, 264000), (50, 220000)], available=42, reserved=0),
            dict(id=511, size='41', color='Oq', sku='SH-13-41', retail=367000, wholesale=264000, min_qty=5, tiers=[(5, 312000), (20, 264000), (50, 220000)], available=163, reserved=0),
            dict(id=512, size='42', color='Oq', sku='SH-13-42', retail=367000, wholesale=264000, min_qty=5, tiers=[(5, 312000), (20, 264000), (50, 220000)], available=21, reserved=0),
        ],
    },
    {
        'id': 114, 'title': 'Ayollar bolen tuflisi “Amasya”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=513, size='39', color='Kulrang', sku='SH-14-39', retail=403000, wholesale=290000, min_qty=5, tiers=[(5, 343000), (20, 290000), (50, 242000)], available=116, reserved=0),
            dict(id=514, size='40', color='Kulrang', sku='SH-14-40', retail=403000, wholesale=290000, min_qty=5, tiers=[(5, 343000), (20, 290000), (50, 242000)], available=65, reserved=0),
            dict(id=515, size='41', color='Kulrang', sku='SH-14-41', retail=403000, wholesale=290000, min_qty=5, tiers=[(5, 343000), (20, 290000), (50, 242000)], available=34, reserved=0),
            dict(id=516, size='42', color='Kulrang', sku='SH-14-42', retail=403000, wholesale=290000, min_qty=5, tiers=[(5, 343000), (20, 290000), (50, 242000)], available=166, reserved=0),
        ],
    },
    {
        'id': 115, 'title': 'Bolalar sandali “Corum”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=517, size='39', color='Oq', sku='SH-15-39', retail=346000, wholesale=249000, min_qty=5, tiers=[(5, 294000), (20, 249000), (50, 208000)], available=41, reserved=0),
            dict(id=518, size='40', color='Oq', sku='SH-15-40', retail=346000, wholesale=249000, min_qty=5, tiers=[(5, 294000), (20, 249000), (50, 208000)], available=92, reserved=0),
            dict(id=519, size='41', color='Oq', sku='SH-15-41', retail=346000, wholesale=249000, min_qty=5, tiers=[(5, 294000), (20, 249000), (50, 208000)], available=168, reserved=0),
            dict(id=520, size='42', color='Oq', sku='SH-15-42', retail=346000, wholesale=249000, min_qty=5, tiers=[(5, 294000), (20, 249000), (50, 208000)], available=45, reserved=0),
        ],
    },
    {
        'id': 116, 'title': 'Sport shippak “Sinop Line”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=521, size='39', color='Qora', sku='SH-16-39', retail=371000, wholesale=267000, min_qty=5, tiers=[(5, 315000), (20, 267000), (50, 223000)], available=103, reserved=0),
            dict(id=522, size='40', color='Qora', sku='SH-16-40', retail=371000, wholesale=267000, min_qty=5, tiers=[(5, 315000), (20, 267000), (50, 223000)], available=151, reserved=0),
            dict(id=523, size='41', color='Qora', sku='SH-16-41', retail=371000, wholesale=267000, min_qty=5, tiers=[(5, 315000), (20, 267000), (50, 223000)], available=124, reserved=0),
            dict(id=524, size='42', color='Qora', sku='SH-16-42', retail=371000, wholesale=267000, min_qty=5, tiers=[(5, 315000), (20, 267000), (50, 223000)], available=109, reserved=0),
        ],
    },
    {
        'id': 117, 'title': 'Trekking botinka “Giresun”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=525, size='39', color='Jigarrang', sku='SH-17-39', retail=197000, wholesale=142000, min_qty=5, tiers=[(5, 167000), (20, 142000), (50, 118000)], available=18, reserved=0),
            dict(id=526, size='40', color='Jigarrang', sku='SH-17-40', retail=197000, wholesale=142000, min_qty=5, tiers=[(5, 167000), (20, 142000), (50, 118000)], available=122, reserved=0),
            dict(id=527, size='41', color='Jigarrang', sku='SH-17-41', retail=197000, wholesale=142000, min_qty=5, tiers=[(5, 167000), (20, 142000), (50, 118000)], available=140, reserved=0),
            dict(id=528, size='42', color='Jigarrang', sku='SH-17-42', retail=197000, wholesale=142000, min_qty=5, tiers=[(5, 167000), (20, 142000), (50, 118000)], available=42, reserved=0),
        ],
    },
    {
        'id': 118, 'title': 'Charm mokasin “Ordu Step”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=529, size='39', color='Jigarrang', sku='SH-18-39', retail=284000, wholesale=204000, min_qty=5, tiers=[(5, 241000), (20, 204000), (50, 170000)], available=177, reserved=0),
            dict(id=530, size='40', color='Jigarrang', sku='SH-18-40', retail=284000, wholesale=204000, min_qty=5, tiers=[(5, 241000), (20, 204000), (50, 170000)], available=132, reserved=0),
            dict(id=531, size='41', color='Jigarrang', sku='SH-18-41', retail=284000, wholesale=204000, min_qty=5, tiers=[(5, 241000), (20, 204000), (50, 170000)], available=54, reserved=0),
            dict(id=532, size='42', color='Jigarrang', sku='SH-18-42', retail=284000, wholesale=204000, min_qty=5, tiers=[(5, 241000), (20, 204000), (50, 170000)], available=126, reserved=0),
        ],
    },
    {
        'id': 119, 'title': 'Bolalar qishki poyabzali “Rize Sole”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=533, size='39', color='Jigarrang', sku='SH-19-39', retail=222000, wholesale=160000, min_qty=5, tiers=[(5, 189000), (20, 160000), (50, 133000)], available=172, reserved=0),
            dict(id=534, size='40', color='Jigarrang', sku='SH-19-40', retail=222000, wholesale=160000, min_qty=5, tiers=[(5, 189000), (20, 160000), (50, 133000)], available=152, reserved=0),
            dict(id=535, size='41', color='Jigarrang', sku='SH-19-41', retail=222000, wholesale=160000, min_qty=5, tiers=[(5, 189000), (20, 160000), (50, 133000)], available=138, reserved=0),
            dict(id=536, size='42', color='Jigarrang', sku='SH-19-42', retail=222000, wholesale=160000, min_qty=5, tiers=[(5, 189000), (20, 160000), (50, 133000)], available=134, reserved=0),
        ],
    },
    {
        'id': 120, 'title': 'Baland poshnali sandal “Artvin”', 'category_id': 'oyoq-kiyim',
        'origin': 'Turkiya', 'icon': '👟', 'variants': [
            dict(id=537, size='39', color='Jigarrang', sku='SH-20-39', retail=285000, wholesale=205000, min_qty=5, tiers=[(5, 242000), (20, 205000), (50, 171000)], available=97, reserved=0),
            dict(id=538, size='40', color='Jigarrang', sku='SH-20-40', retail=285000, wholesale=205000, min_qty=5, tiers=[(5, 242000), (20, 205000), (50, 171000)], available=77, reserved=0),
            dict(id=539, size='41', color='Jigarrang', sku='SH-20-41', retail=285000, wholesale=205000, min_qty=5, tiers=[(5, 242000), (20, 205000), (50, 171000)], available=37, reserved=0),
            dict(id=540, size='42', color='Jigarrang', sku='SH-20-42', retail=285000, wholesale=205000, min_qty=5, tiers=[(5, 242000), (20, 205000), (50, 171000)], available=86, reserved=0),
        ],
    },
    {
        'id': 121, 'title': "Qo'l sumkasi “Galata Leather”", 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=541, size='Universal', color='Jigarrang', sku='BG-01-UNIVERSAL', retail=441000, wholesale=318000, min_qty=5, tiers=[(5, 375000), (20, 318000), (50, 265000)], available=133, reserved=0),
        ],
    },
    {
        'id': 122, 'title': 'Ryukzak “Beyoglu”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=542, size='Universal', color="Ko'k", sku='BG-02-UNIVERSAL', retail=338000, wholesale=243000, min_qty=5, tiers=[(5, 287000), (20, 243000), (50, 203000)], available=101, reserved=0),
        ],
    },
    {
        'id': 123, 'title': 'Sayohat sumkasi “Kadikoy”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=543, size='Universal', color='Bej', sku='BG-03-UNIVERSAL', retail=159000, wholesale=114000, min_qty=5, tiers=[(5, 135000), (20, 114000), (50, 95000)], available=61, reserved=0),
        ],
    },
    {
        'id': 124, 'title': 'Klatch “Uskudar”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=544, size='Universal', color='Bej', sku='BG-04-UNIVERSAL', retail=311000, wholesale=224000, min_qty=5, tiers=[(5, 264000), (20, 224000), (50, 187000)], available=81, reserved=0),
        ],
    },
    {
        'id': 125, 'title': 'Beliga taqiladigan sumka “Taksim”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=545, size='Universal', color='Bej', sku='BG-05-UNIVERSAL', retail=262000, wholesale=189000, min_qty=5, tiers=[(5, 223000), (20, 189000), (50, 157000)], available=157, reserved=0),
        ],
    },
    {
        'id': 126, 'title': 'Noutbuk sumkasi “Karakoy”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=546, size='Universal', color='Jigarrang', sku='BG-06-UNIVERSAL', retail=153000, wholesale=110000, min_qty=5, tiers=[(5, 130000), (20, 110000), (50, 92000)], available=36, reserved=0),
        ],
    },
    {
        'id': 127, 'title': 'Sport sumka “Ortakoy”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=547, size='Universal', color="Ko'k", sku='BG-07-UNIVERSAL', retail=230000, wholesale=166000, min_qty=5, tiers=[(5, 196000), (20, 166000), (50, 138000)], available=140, reserved=0),
        ],
    },
    {
        'id': 128, 'title': 'Bolalar ryukzagi “Besiktas Line”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=548, size='Universal', color='Jigarrang', sku='BG-08-UNIVERSAL', retail=333000, wholesale=240000, min_qty=5, tiers=[(5, 283000), (20, 240000), (50, 200000)], available=136, reserved=0),
        ],
    },
    {
        'id': 129, 'title': 'Kross-badi sumka “Sisli Style”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=549, size='Universal', color="Ko'k", sku='BG-09-UNIVERSAL', retail=363000, wholesale=261000, min_qty=5, tiers=[(5, 309000), (20, 261000), (50, 218000)], available=129, reserved=0),
        ],
    },
    {
        'id': 130, 'title': 'Xarid sumkasi “Nisantasi”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=550, size='Universal', color='Qora', sku='BG-10-UNIVERSAL', retail=412000, wholesale=297000, min_qty=5, tiers=[(5, 350000), (20, 297000), (50, 247000)], available=90, reserved=0),
        ],
    },
    {
        'id': 131, 'title': 'Kosmetichka “Cihangir”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=551, size='Universal', color='Jigarrang', sku='BG-11-UNIVERSAL', retail=223000, wholesale=161000, min_qty=5, tiers=[(5, 190000), (20, 161000), (50, 134000)], available=93, reserved=0),
        ],
    },
    {
        'id': 132, 'title': 'Hamyon “Moda Bag”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=552, size='Universal', color='Bej', sku='BG-12-UNIVERSAL', retail=369000, wholesale=266000, min_qty=5, tiers=[(5, 314000), (20, 266000), (50, 221000)], available=136, reserved=0),
        ],
    },
    {
        'id': 133, 'title': 'Maktab ryukzagi “Eminonu”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=553, size='Universal', color='Bej', sku='BG-13-UNIVERSAL', retail=333000, wholesale=240000, min_qty=5, tiers=[(5, 283000), (20, 240000), (50, 200000)], available=123, reserved=0),
        ],
    },
    {
        'id': 134, 'title': 'Sport ryukzak “Atasehir”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=554, size='Universal', color='Bej', sku='BG-14-UNIVERSAL', retail=479000, wholesale=345000, min_qty=5, tiers=[(5, 407000), (20, 345000), (50, 287000)], available=105, reserved=0),
        ],
    },
    {
        'id': 135, 'title': 'Konvert sumka “Bakirkoy”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=555, size='Universal', color='Bej', sku='BG-15-UNIVERSAL', retail=382000, wholesale=275000, min_qty=5, tiers=[(5, 325000), (20, 275000), (50, 229000)], available=93, reserved=0),
        ],
    },
    {
        'id': 136, 'title': 'Plyaj sumkasi “Maltepe”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=556, size='Universal', color='Qora', sku='BG-16-UNIVERSAL', retail=233000, wholesale=168000, min_qty=5, tiers=[(5, 198000), (20, 168000), (50, 140000)], available=64, reserved=0),
        ],
    },
    {
        'id': 137, 'title': 'Dokument papkasi “Umraniye”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=557, size='Universal', color='Jigarrang', sku='BG-17-UNIVERSAL', retail=254000, wholesale=183000, min_qty=5, tiers=[(5, 216000), (20, 183000), (50, 152000)], available=64, reserved=0),
        ],
    },
    {
        'id': 138, 'title': 'Sayohat chamadoni “Fatih Line”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=558, size='Universal', color="Ko'k", sku='BG-18-UNIVERSAL', retail=221000, wholesale=159000, min_qty=5, tiers=[(5, 188000), (20, 159000), (50, 133000)], available=85, reserved=0),
        ],
    },
    {
        'id': 139, 'title': 'Kichik yelka sumkasi “Bahcelievler”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=559, size='Universal', color='Bej', sku='BG-19-UNIVERSAL', retail=389000, wholesale=280000, min_qty=5, tiers=[(5, 331000), (20, 280000), (50, 233000)], available=40, reserved=0),
        ],
    },
    {
        'id': 140, 'title': 'Fitnes sumka “Levent”', 'category_id': 'sumkalar',
        'origin': 'Turkiya', 'icon': '👜', 'variants': [
            dict(id=560, size='Universal', color='Bej', sku='BG-20-UNIVERSAL', retail=425000, wholesale=306000, min_qty=5, tiers=[(5, 361000), (20, 306000), (50, 255000)], available=73, reserved=0),
        ],
    },
    {
        'id': 141, 'title': 'Kepka “Shanghai Line”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=561, size='Universal', color='Kulrang', sku='HT-01-UNIVERSAL', retail=53000, wholesale=38000, min_qty=5, tiers=[(5, 45000), (20, 38000), (50, 32000)], available=18, reserved=0),
        ],
    },
    {
        'id': 142, 'title': 'Shlyapa “Beijing Classic”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=562, size='Universal', color="Ko'k", sku='HT-02-UNIVERSAL', retail=70000, wholesale=50000, min_qty=5, tiers=[(5, 60000), (20, 50000), (50, 42000)], available=85, reserved=0),
        ],
    },
    {
        'id': 143, 'title': 'Trikotaj shapka “Shenzhen Fresh”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=563, size='Universal', color='Qora', sku='HT-03-UNIVERSAL', retail=37000, wholesale=27000, min_qty=5, tiers=[(5, 31000), (20, 27000), (50, 22000)], available=156, reserved=0),
        ],
    },
    {
        'id': 144, 'title': 'Panama “Canton Cap”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=564, size='Universal', color="Ko'k", sku='HT-04-UNIVERSAL', retail=50000, wholesale=36000, min_qty=5, tiers=[(5, 42000), (20, 36000), (50, 30000)], available=178, reserved=0),
        ],
    },
    {
        'id': 145, 'title': "Do'ppi “Dragon Head”", 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=565, size='Universal', color='Qizil', sku='HT-05-UNIVERSAL', retail=78000, wholesale=56000, min_qty=5, tiers=[(5, 66000), (20, 56000), (50, 47000)], available=41, reserved=0),
        ],
    },
    {
        'id': 146, 'title': "Ro'mol “East Style”", 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=566, size='Universal', color='Kulrang', sku='HT-06-UNIVERSAL', retail=79000, wholesale=57000, min_qty=5, tiers=[(5, 67000), (20, 57000), (50, 47000)], available=135, reserved=0),
        ],
    },
    {
        'id': 147, 'title': 'Bandana “Silk Crown”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=567, size='Universal', color='Kulrang', sku='HT-07-UNIVERSAL', retail=59000, wholesale=42000, min_qty=5, tiers=[(5, 50000), (20, 42000), (50, 35000)], available=62, reserved=0),
        ],
    },
    {
        'id': 148, 'title': 'Beysbolka “Zhejiang Hat”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=568, size='Universal', color='Kulrang', sku='HT-08-UNIVERSAL', retail=83000, wholesale=60000, min_qty=5, tiers=[(5, 71000), (20, 60000), (50, 50000)], available=137, reserved=0),
        ],
    },
    {
        'id': 149, 'title': 'Qishki telpak “Yiwu Cap”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=569, size='Universal', color='Qora', sku='HT-09-UNIVERSAL', retail=41000, wholesale=30000, min_qty=5, tiers=[(5, 35000), (20, 30000), (50, 25000)], available=117, reserved=0),
        ],
    },
    {
        'id': 150, 'title': 'Beret “Guangzhou Head”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=570, size='Universal', color='Qora', sku='HT-10-UNIVERSAL', retail=60000, wholesale=43000, min_qty=5, tiers=[(5, 51000), (20, 43000), (50, 36000)], available=53, reserved=0),
        ],
    },
    {
        'id': 151, 'title': 'Kigiz shlyapa “Fujian Line”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=571, size='Universal', color='Kulrang', sku='HT-11-UNIVERSAL', retail=42000, wholesale=30000, min_qty=5, tiers=[(5, 36000), (20, 30000), (50, 25000)], available=36, reserved=0),
        ],
    },
    {
        'id': 152, 'title': 'Bolalar shapkasi “Hainan Sun”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=572, size='Universal', color='Qora', sku='HT-12-UNIVERSAL', retail=85000, wholesale=61000, min_qty=5, tiers=[(5, 72000), (20, 61000), (50, 51000)], available=157, reserved=0),
        ],
    },
    {
        'id': 153, 'title': 'Plyaj shlyapasi “Sichuan Style”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=573, size='Universal', color="Ko'k", sku='HT-13-UNIVERSAL', retail=73000, wholesale=53000, min_qty=5, tiers=[(5, 62000), (20, 53000), (50, 44000)], available=148, reserved=0),
        ],
    },
    {
        'id': 154, 'title': "Qishki sharf-shapka to'plami “Hunan Cap”", 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=574, size='Universal', color='Qizil', sku='HT-14-UNIVERSAL', retail=54000, wholesale=39000, min_qty=5, tiers=[(5, 46000), (20, 39000), (50, 32000)], available=91, reserved=0),
        ],
    },
    {
        'id': 155, 'title': 'Bolalar kepkasi “Anhui Line”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=575, size='Universal', color='Qizil', sku='HT-15-UNIVERSAL', retail=78000, wholesale=56000, min_qty=5, tiers=[(5, 66000), (20, 56000), (50, 47000)], available=93, reserved=0),
        ],
    },
    {
        'id': 156, 'title': 'Sport bandana “Jiangsu Head”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=576, size='Universal', color='Qora', sku='HT-16-UNIVERSAL', retail=63000, wholesale=45000, min_qty=5, tiers=[(5, 54000), (20, 45000), (50, 38000)], available=171, reserved=0),
        ],
    },
    {
        'id': 157, 'title': 'Trikotaj snud “Hebei Style”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=577, size='Universal', color='Qora', sku='HT-17-UNIVERSAL', retail=83000, wholesale=60000, min_qty=5, tiers=[(5, 71000), (20, 60000), (50, 50000)], available=68, reserved=0),
        ],
    },
    {
        'id': 158, 'title': 'Bolalar panamasi “Shandong Cap”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=578, size='Universal', color='Kulrang', sku='HT-18-UNIVERSAL', retail=66000, wholesale=48000, min_qty=5, tiers=[(5, 56000), (20, 48000), (50, 40000)], available=35, reserved=0),
        ],
    },
    {
        'id': 159, 'title': 'Fetr shlyapa “Fuzhou Line”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=579, size='Universal', color="Ko'k", sku='HT-19-UNIVERSAL', retail=43000, wholesale=31000, min_qty=5, tiers=[(5, 37000), (20, 31000), (50, 26000)], available=156, reserved=0),
        ],
    },
    {
        'id': 160, 'title': 'Trucker kepka “Xiamen Sun”', 'category_id': 'bosh-kiyimlar',
        'origin': 'Xitoy', 'icon': '🧢', 'variants': [
            dict(id=580, size='Universal', color='Qora', sku='HT-20-UNIVERSAL', retail=39000, wholesale=28000, min_qty=5, tiers=[(5, 33000), (20, 28000), (50, 23000)], available=119, reserved=0),
        ],
    },
]