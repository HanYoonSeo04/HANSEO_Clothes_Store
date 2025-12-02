from django.db import models
from django.contrib.auth.models import User

class Qna(models.Model):
    CATEGORY = [
        ("product", "상품 문의"),
        ("order", "주문/결제 문의"),
        ("delivery", "배송 문의"),
        ("etc", "기타 문의"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY)
    content = models.TextField()
    image = models.ImageField(upload_to="qna/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    reply = models.TextField(null=True, blank=True)  
    replied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
