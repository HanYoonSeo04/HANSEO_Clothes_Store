from django.shortcuts import render, get_object_or_404
from .models import Product
from reviews.models import Review

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = Review.objects.filter(product=product).order_by("-created_at")
    return render(request, "products/detail.html", {
        "product": product,
        "reviews": reviews,
    })
