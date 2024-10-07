# Optimizing Code Performance

## 1. Collections moduli

### Counter()

### defaultdict()

defaultdict() - bu mavjud bo'lmagan kalitlar uchun standart qiymat beradigan lug'at turi.

- **Qachon ishlatamiz?** Lug'atda yo'q kalitlar bilan ishlashda KeyError xatosidan qochish kerak bo'lganda.
- **Nega bizga kerak?** Kodimizni soddalashtirib, xatolardan himoya qiladi.
- **Qanchalik tezlashtiradi?** Har safar kalitning mavjudligini tekshirish o'rniga, avtomatik ravishda standart qiymat qaytaradi.

Misol: Mahsulotlarni kategoriyalarga ajratish.

### namedtuple()

namedtuple() - bu nomlangan maydonlarga ega bo'lgan kortej yaratish imkonini beradi.

- **Qachon ishlatamiz?** Ma'lumotlarni strukturalashtirishda, ayniqsa kichik, o'zgarmas obyektlar uchun.
- **Nega bizga kerak?** Kodni o'qish va tushunish osonroq bo'ladi, xatolar kamayadi.
- **Qanchalik tezlashtiradi?** To'liq klasslardan ko'ra yengil va tezroq, lekin oddiy kortejlardan ko'ra tushunarli.

Misol: Mahsulot ma'lumotlarini saqlash va uzatish.

## 2. Itertools moduli

### combinations()

combinations() - berilgan to'plamdan barcha mumkin bo'lgan kombinatsiyalarni yaratadi.

- **Qachon ishlatamiz?** Barcha mumkin bo'lgan variantlarni ko'rib chiqish kerak bo'lganda.
- **Nega bizga kerak?** Qo'lda hisoblashdan ko'ra ancha samarali va xatosiz.
- **Qanchalik tezlashtiradi?** Murakkab ichma-ich sikllar o'rniga bir qator kod bilan barcha kombinatsiyalarni olish mumkin.

Misol: Mahsulotlar ombori uchun barcha mumkin bo'lgan juftliklarni yaratish.

### groupby()

groupby() - ketma-ketlikni guruhlarga ajratadi.

- **Qachon ishlatamiz?** Ma'lumotlarni biror belgi bo'yicha guruhlash kerak bo'lganda.
- **Nega bizga kerak?** Ma'lumotlarni samarali tahlil qilish va tashkil etish uchun.
- **Qanchalik tezlashtiradi?** Qo'lda guruhlashga nisbatan ancha tez va kamroq xato qilish ehtimoli bor.

Misol: Buyurtmalarni status bo'yicha guruhlash.

## 3. Functools moduli

### lru_cache()

lru_cache() - funksiya natijalarini keshlaydigan dekorator.

- **Qachon ishlatamiz?** Bir xil argumentlar bilan qayta-qayta chaqiriladigan, lekin natijasi kamdan-kam o'zgaradigan funksiyalar uchun.
- **Nega bizga kerak?** Dastur tezligini oshirish va resurslardan samarali foydalanish uchun.
- **Qanchalik tezlashtiradi?** Katta hisoblar uchun funksiya bajarilish vaqtini sezilarli darajada kamaytiradi.

Misol: Mahsulot ma'lumotlarini olish funksiyasini keshlashtirish.

## 4. Contextlib moduli

### suppress()

suppress() - ma'lum xatolarni e'tiborsiz qoldirish uchun kontekst menejeri.

- **Qachon ishlatamiz?** Ba'zi xatolarni boshqarish kerak bo'lmaganda va ular dastur ishlashiga xalaqit bermasligi kerak bo'lganda.
- **Nega bizga kerak?** Kodimizni soddalashtirib, keraksiz try-except bloklaridan qutulish uchun.
- **Qanchalik tezlashtiradi?** Kod hajmini kamaytiradi va o'qishni osonlashtiradi.

Misol: Mavjud bo'lmagan mahsulotni o'chirishga urinish.

### contextmanager dekorator

@contextmanager - o'z kontekst menejerlarimizni yaratish imkonini beruvchi dekorator.

- **Qachon ishlatamiz?** Murakkab resurslarni boshqarish va tozalash kerak bo'lganda.
- **Nega bizga kerak?** Resurslardan foydalanishni avtomatlashtirish va xavfsiz qilish uchun.
- **Qanchalik tezlashtiradi?** Resurslarni ochish va yopish uchun takroriy kodni kamaytiradi, xatolarni kamaytiradi.

Misol: Ma'lumotlar bazasida atomik operatsiyalarni bajarish.

Bu modullar va funksiyalar Python dasturchilariga kodlarini yanada samarali, tushunarli va xatosiz yozishda yordam beradi. Ulardan to'g'ri foydalanish dasturlaringizni sezilarli darajada yaxshilashi mumkin.
