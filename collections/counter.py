"""

Counter() - bu elementlarni sanash uchun mo'ljallangan maxsus lug'at turi.

- Qachon ishlatamiz? Ro'yxatdagi elementlarni sanash kerak bo'lganda.
- Nega bizga kerak? Elementlarni samarali sanash va eng ko'p uchraydigan elementlarni topish uchun.
- Qanchalik tezlashtiradi? Oddiy lug'at bilan qo'lda sanashga nisbatan ancha tezroq va kamroq kod talab qiladi.


More: https://github.com/firdavsDev/advanced-python/blob/main/data_structures/collections/Counter.py
"""

from collections import Counter

# Bad
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(word_count)

# Good
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "date"]
word_count = Counter(words)
print(word_count.most_common(2))


# Output: Counter({'apple': 2, 'banana': 2, 'cherry': 1, 'date': 1})


################### Django loyihada ###################


def product_stats(request):
    # Bad
    categories = {}
    for product in Product.objects.all():
        if product.category in categories:
            categories[product.category] += 1
        else:
            categories[product.category] = 1

    # Good
    categories = Counter(product.category for product in Product.objects.all())
    return render(request, "product_stats.html", {"categories": categories})
