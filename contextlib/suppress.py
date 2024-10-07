"""
suppress() - ma'lum xatolarni e'tiborsiz qoldirish uchun kontekst menejeri.

- Qachon ishlatamiz? Ba'zi xatolarni boshqarish kerak bo'lmaganda va ular dastur ishlashiga xalaqit bermasligi kerak bo'lganda.
- Nega bizga kerak? Kodimizni soddalashtirib, keraksiz try-except bloklaridan qutulish uchun.
- Qanchalik tezlashtiradi? Kod hajmini kamaytiradi va o'qishni osonlashtiradi.

"""

# Bad
try:
    os.remove("temp_file.txt")
except FileNotFoundError:
    pass

import os

# Good
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp_file.txt")


# Contextlib modulidan misollar

from contextlib import suppress

from django.core.exceptions import ObjectDoesNotExist


# suppress
def delete_product(product_id):
    with suppress(ObjectDoesNotExist):
        product = Product.objects.get(id=product_id)
        product.delete()
        return True
    return False


# Django view da ishlatish
def delete_product_view(request, product_id):
    if delete_product(product_id):
        messages.success(request, "Mahsulot muvaffaqiyatli o'chirildi")
    else:
        messages.error(request, "Mahsulot topilmadi")
    return redirect("product_list")


# contextmanager dekorator misoli
from contextlib import contextmanager

from django.db import transaction


@contextmanager
def atomic_update(model, pk):
    with transaction.atomic():
        obj = model.objects.select_for_update().get(pk=pk)
        yield obj
        obj.save()


# Django view da ishlatish
def update_product_stock(request, product_id):
    try:
        with atomic_update(Product, product_id) as product:
            new_stock = int(request.POST.get("new_stock", 0))
            product.stock = new_stock
        messages.success(request, "Mahsulot zaxirasi yangilandi")
    except Product.DoesNotExist:
        messages.error(request, "Mahsulot topilmadi")
    return redirect("product_detail", product_id=product_id)
