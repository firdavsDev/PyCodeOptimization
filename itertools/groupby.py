def group_orders_by_status(request):
    orders = Order.objects.all().order_by("status")

    grouped_orders = []
    for status, orders_group in groupby(orders, key=lambda x: x.status):
        grouped_orders.append({"status": status, "orders": list(orders_group)})

    return render(request, "grouped_orders.html", {"grouped_orders": grouped_orders})
