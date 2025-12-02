from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
from django.utils import timezone

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    depositor_name = models.CharField(max_length=50)     # 입금자명
    bank_name = models.CharField(max_length=100, default="신한은행")
    account_number = models.CharField(max_length=100, default="123-456-7890")  
    amount = models.IntegerField()

    created_at = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order.id}번 주문 결제"
