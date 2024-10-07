"""
Importlarda (Do Not Use * Operation) aynan sizga qaysi funksiya kerak bo'lsa ushani chaqirib ishlating, butun bir boshli module'ni emas
negaki siznig yozgan .(nuqta) birinchi bo'lib __getattribute()__ yoki __getattr()__ metodlarni chaqiradi, bular esa metodlarni nomlarini dict'larni qaytarib beradi bu degani esa .(nuqta) operatsiya ko'proq vaqt oladi degani
"""

# bad
import math

from some_module import *

math.sqrt(64)  # here u use .

# good
from math import sqrt

sqrt(64)
