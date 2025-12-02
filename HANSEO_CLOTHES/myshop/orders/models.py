from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("cart", "장바구니"),
            ("pending", "결제 대기"),
            ("paid", "결제 완료"),
            ("shipping", "배송중"),
            ("done", "배송 완료"),
        ],
        default="cart"
    )

    def __str__(self):
        return f"{self.user.username}의 주문({self.id})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.product.price * self.quantity
