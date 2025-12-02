from django.db import models
from django.contrib.auth.models import User
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50, default="카카오뱅크")
    account_number = models.CharField(max_length=50, default="123-456-789")
    depositor_name = models.CharField(max_length=50)
    is_confirmed = models.BooleanField(default=False)  # 관리자 확인 여부

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.order.id}"
