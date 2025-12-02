from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review

@login_required
def create_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            content=content,
            image=image
        )
        return redirect("/products/" + str(product_id))

    return render(request, "reviews/create.html", {"product": product})
