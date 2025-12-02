from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# 장바구니
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x {self.quantity}"


# 주문
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default="결제 대기중",   # 주문 상태
        choices=[
            ("결제 대기중", "결제 대기중"),
            ("결제 완료", "결제 완료"),
            ("배송 준비중", "배송 준비중"),
            ("배송중", "배송중"),
            ("배송 완료", "배송 완료"),
        ]
    )

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# 주문 상세 (상품 리스트)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order.id} / {self.product.name} ({self.quantity})"
