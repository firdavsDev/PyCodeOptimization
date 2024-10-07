"""
functools.lru_cache(): ko'p marotaba run bo'layotgan funksiyangiz uchun juda foydali bo'lad oladi.  
funksiyadan qaytayotgan natija kashlanish orqali biroz saqlanib turiladi
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
