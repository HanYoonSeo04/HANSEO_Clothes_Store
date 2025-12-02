from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from orders.models import Order
from delivery.models import Delivery

def pay(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # 총 금액 계산
    total = sum(item.get_total() for item in order.items.all())

    if request.method == "POST":
        depositor_name = request.POST.get("depositor_name")

        payment = Payment.objects.create(
            order=order,
            user=request.user,
            depositor_name=depositor_name,
            amount=total
        )

        order.status = "pending"
        order.save()

        return redirect("payments:success", payment.id)

    return render(request, "payments/pay.html", {
        "order": order,
        "total": total,
    })


def success(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    order = payment.order

    order.status = "paid"
    order.save()

    # 배송 정보 생성
    Delivery.objects.create(order=order, status="ready")

    return render(request, "payments/success.html", {
        "payment": payment
    })
