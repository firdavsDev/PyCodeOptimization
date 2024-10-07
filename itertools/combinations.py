"""
combinations(items, r) - berilgan items malumotlar asosida r martalik kambinatsiyalar tuzishda ishlatishiz mumkin.
"""


# Bad
def get_combinations(items, r):
    result = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if r == 2:
                result.append((items[i], items[j]))
            elif r == 3:
                for k in range(j + 1, len(items)):
                    result.append((items[i], items[j], items[k]))
    return result


# Good
from itertools import combinations


def get_combinations(items, r):
    return list(combinations(items, r))


# OutPut: [(1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (4, 5, 6)]


# ################### Django loyihada ###################
def get_product_combinations(request):
    products = Product.objects.all()[:5]  # Misol uchun faqat 5 ta mahsulot olamiz
    product_names = [product.name for product in products]

    # Barcha 2 ta mahsulotdan iborat kombinatsiyalarni yaratish
    product_combos = list(combinations(product_names, 2))

    return render(
        request, "product_combinations.html", {"product_combos": product_combos}
    )
