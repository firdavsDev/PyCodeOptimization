# partial() funksiyasi misoli
from functools import partial

from django.core.paginator import Paginator


def custom_paginate(queryset, page_number, per_page=10):
    paginator = Paginator(queryset, per_page)
    return paginator.get_page(page_number)


# 20 ta element bilan sahifalash funksiyasini yaratish
paginate_20 = partial(custom_paginate, per_page=20)


# View da ishlatish
def product_list_view(request):
    products = Product.objects.all()
    page_number = request.GET.get("page")
    paginated_products = paginate_20(products, page_number)
    return render(request, "product_list.html", {"products": paginated_products})
