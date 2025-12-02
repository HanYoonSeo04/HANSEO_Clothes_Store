from accounts.forms import ProfileForm
from accounts.models import Profile
from django.shortcuts import render, redirect
from .models import Order

def checkout(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    # 📌 Profile 자동 생성 (가장 중요)
    profile, created = Profile.objects.get_or_create(user=request.user)

    # 장바구니(order) 가져오기
    order = Order.objects.filter(user=request.user, status="cart").first()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            order.status = "pending"
            order.save()
            return redirect("payments:pay", order.id)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "orders/checkout.html", {
        "form": form,
        "order": order,
    })
