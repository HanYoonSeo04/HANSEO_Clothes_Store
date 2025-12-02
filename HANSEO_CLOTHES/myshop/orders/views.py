from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, CartItem
from payments.models import Payment

@login_required
def checkout(request):
    # 주소 없으면 주소 페이지로 이동
    if not request.user.profile.address:
        return redirect("/accounts/edit?error=need_address")

    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect("/orders/cart/")

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total": total,
        "address": request.user.profile.address
    })


@login_required
def make_payment(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect("/orders/cart/")

    order = Order.objects.create(
        user=request.user,
        total_price=sum(item.product.price * item.quantity for item in cart_items),
        status="입금대기"
    )

    Payment.objects.create(
        order=order,
        user=request.user,
        depositor_name=request.POST.get("depositor_name")
    )

    cart_items.delete()

    return render(request, "orders/payment_complete.html", {"order": order})
