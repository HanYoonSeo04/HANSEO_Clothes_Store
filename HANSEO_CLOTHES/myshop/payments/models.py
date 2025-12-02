from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
from django.utils import timezone

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    depositor_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=False)  # 관리자 확인 여부

    def __str__(self):
        return f"Payment for Order {self.order.id}"
