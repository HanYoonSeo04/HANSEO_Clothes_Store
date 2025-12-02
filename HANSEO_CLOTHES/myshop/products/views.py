from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    category = request.GET.get("category")
    sub = request.GET.get("sub")

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)
    if sub:
        products = products.filter(subcategory=sub)

    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {"product": product})
