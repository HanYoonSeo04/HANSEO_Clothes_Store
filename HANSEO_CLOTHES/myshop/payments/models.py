from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    paid_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    method = models.CharField(max_length=30)
