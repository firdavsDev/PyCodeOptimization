"""
functools.lru_cache(): ko'p marotaba run bo'layotgan funksiyangiz uchun juda foydali bo'lad oladi.  
funksiyadan qaytayotgan natija kashlanish orqali biroz saqlanib turiladi

- Qachon ishlatamiz? Bir xil argumentlar bilan qayta-qayta chaqiriladigan, lekin natijasi kamdan-kam o'zgaradigan funksiyalar uchun.
- Nega bizga kerak? Dastur tezligini oshirish va resurslardan samarali foydalanish uchun.
- Qanchalik tezlashtiradi? Katta hisoblar uchun funksiya bajarilish vaqtini sezilarli darajada kamaytiradi.

"""


# Bad
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Good
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Functools modulidan misollar

from functools import lru_cache

from django.core.cache import cache


# lru_cache()
@lru_cache(maxsize=100)
def get_product_details(product_id):
    # Bu funksiya tez-tez chaqiriladigan, lekin kam o'zgaradigan ma'lumotlar uchun
    try:
        product = Product.objects.get(id=product_id)
        return {
            "name": product.name,
            "price": product.price,
            "description": product.description,
        }
    except Product.DoesNotExist:
        return None


# Django view da ishlatish
def product_view(request, product_id):
    product_details = get_product_details(product_id)
    if product_details:
        return render(request, "product_details.html", {"product": product_details})
    else:
        return HttpResponse("Mahsulot topilmadi", status=404)
