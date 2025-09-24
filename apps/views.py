from django.shortcuts import render

from apps.models import Product


def product_list_page(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'apps/product-list.html', context)


def product_detail_page(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product": product,
    }
    return render(request, 'apps/product-detail.html', context)
