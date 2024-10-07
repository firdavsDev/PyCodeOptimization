"""
namedtuple() -  classlardan ko'ra ko'proq memory efficient hisoblanadi bunda faqat read malumotlar tezroq ishlaydi.

- Qachon ishlatamiz? Ma'lumotlarni strukturalashtirishda, ayniqsa kichik, o'zgarmas obyektlar uchun.
- Nega bizga kerak? Kodni o'qish va tushunish osonroq bo'ladi, xatolar kamayadi.
- Qanchalik tezlashtiradi? To'liq klasslardan ko'ra yengil va tezroq, lekin oddiy kortejlardan ko'ra tushunarli.
"""

from collections import namedtuple

# Create a namedtuple called 'Car' with fields 'make', 'model', and 'year'
Car = namedtuple("Car", ["make", "model", "year"])

# Create an instance of the Car namedtuple
my_car = Car(make="Toyota", model="Corolla", year=2020)

# Access fields by name
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)  # Output: 2020

# You can still access fields by index if you prefer
print(my_car[0])  # Output: Toyota

# Namedtuples are immutable, so this will raise an error:
# my_car.year = 2021 # Uncommenting this will cause AttributeError


################### Django loyihada ###################
from django.db import models

ProductInfo = namedtuple("ProductInfo", ["name", "price", "stock"])


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def get_product_info(self):
        return ProductInfo(self.name, self.price, self.stock)


# Foydalanish:
product = Product.objects.first()
info = product.get_product_info()
print(f"Mahsulot: {info.name}, Narxi: {info.price}, Omborda: {info.stock}")
