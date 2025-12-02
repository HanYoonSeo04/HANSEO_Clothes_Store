from django.shortcuts import render, redirect
from .models import CartItem, Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required


# 장바구니 보기
@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'orders/cart.html', {"items": items})


# 장바구니 담기
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("orders:cart")


# 장바구니 상품 삭제
@login_required
def remove_from_cart(request, item_id):
    CartItem.objects.get(id=item_id).delete()
    return redirect("orders:cart")

# 주문 생성
@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("orders:cart")

    # 주문 생성
    order = Order.objects.create(user=request.user)

    # 각 CartItem → OrderItem 으로 이동
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    # 장바구니 비우기
    cart_items.delete()

    return redirect("orders:order_complete", order_id=order.id)


# 주문 완료 페이지
@login_required
def order_complete(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    return render(request, "orders/order_complete.html", {
        "order": order,
        "order_items": order_items
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {"orders": orders})

@login_required
def checkout(request):
    if not request.user.profile.address:
        return redirect("/accounts/edit/?error=need_address")

    cart_items = CartItem.objects.filter(user=request.user)

    return render(request, "orders/checkout.html", {"cart_items": cart_items})
