"""

- Qachon ishlatamiz? Ma'lumotlarni biror belgi bo'yicha guruhlash kerak bo'lganda.
- Nega bizga kerak? Ma'lumotlarni samarali tahlil qilish va tashkil etish uchun.
- Qanchalik tezlashtiradi? Qo'lda guruhlashga nisbatan ancha tez va kamroq xato qilish ehtimoli bor.

"""

# Bad
data = [("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)]
grouped = {}
for key, value in data:
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(value)

# Good
from itertools import groupby
from operator import itemgetter

data = [("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)]
sorted_data = sorted(data, key=itemgetter(0))
grouped = {
    k: list(map(itemgetter(1), v)) for k, v in groupby(sorted_data, key=itemgetter(0))
}


def group_orders_by_status(request):
    orders = Order.objects.all().order_by("status")

    grouped_orders = []
    for status, orders_group in groupby(orders, key=lambda x: x.status):
        grouped_orders.append({"status": status, "orders": list(orders_group)})

    return render(request, "grouped_orders.html", {"grouped_orders": grouped_orders})
