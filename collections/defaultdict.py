"""
defaultdict - o'z nomi bilan kurishiz mumkin default holatda value berib ketishda ishlatishimiz mumkin
"""

# bad
word_list = ["apple", "banana", "apple", "cherry", "banana", "date"]
word_count = {}
for word in word_list:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1


# Good
from collections import defaultdict

word_list = ["apple", "banana", "apple", "cherry", "banana", "date"]
word_count = defaultdict(int)

word_count = {}
for word in word_list:
    word_count[word] += 1

# Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 2, 'cherry': 1, 'date': 1})


################### Django loyihada ###################
from collections import defaultdict


def order_summary(request):
    # Bad
    product_totals = {}
    for order in Order.objects.all():
        for item in order.items.all():
            if item.product.name not in product_totals:
                product_totals[item.product.name] = 0
            product_totals[item.product.name] += item.quantity

    # Good
    product_totals = defaultdict(int)
    for order in Order.objects.all():
        for item in order.items.all():
            product_totals[item.product.name] += item.quantity

    return render(
        request, "order_summary.html", {"product_totals": dict(product_totals)}
    )
