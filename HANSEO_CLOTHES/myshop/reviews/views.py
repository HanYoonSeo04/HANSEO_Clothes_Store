from django.shortcuts import redirect, get_object_or_404
from .models import Review
from products.models import Product

def add_review(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)

        Review.objects.create(
            product=product,
            user=request.user,
            rating=request.POST.get("rating"),
            content=request.POST.get("content"),
            image=request.FILES.get("image")
        )

        return redirect("products:detail", product_id)

    return redirect("products:list")
