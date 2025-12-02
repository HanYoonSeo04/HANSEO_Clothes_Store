from django.db import models
from orders.models import Order

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ("ready", "배송 준비중"),
            ("shipping", "배송중"),
            ("done", "배송 완료"),
        ],
        default="ready"
    )

    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.order.id}번 배송 상태: {self.status}"
