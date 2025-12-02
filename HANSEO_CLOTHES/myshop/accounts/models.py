from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    receiver_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    detail_address = models.CharField(max_length=255, blank=True)

    is_default = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Profile"
