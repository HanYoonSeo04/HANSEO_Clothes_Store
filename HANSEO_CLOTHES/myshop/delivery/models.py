from django.db import models
from orders.models import Order

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=30, default="배송 준비중")
