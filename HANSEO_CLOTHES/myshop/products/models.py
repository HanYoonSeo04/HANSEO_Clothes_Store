from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('top', '상의'),
        ('bottom', '하의'),
        ('acc', '악세사리'),
        ('shoe', '신발'),
    ]

    SUBCATEGORY_CHOICES = [
        ('coat', '코트'),
        ('jacket', '자켓'),
        ('padding', '패딩'),
        ('mtm', '맨투맨'),
        ('hoodie', '후드티'),
        ('jeans', '청바지'),
        ('slacks', '슬랙스'),
        ('jogger', '조거팬츠'),
        ('shorts', '반바지'),
        ('hat', '모자'),
        ('bag', '가방'),
        ('belt', '벨트'),
        ('tie', '넥타이'),
        ('sneakers', '운동화'),
        ('boots', '부츠'),
        ('sandals', '샌들'),
        ('loafers', '로퍼'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="products/")

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='top')
    subcategory = models.CharField(max_length=20, choices=SUBCATEGORY_CHOICES, default='coat')

    def __str__(self):
        return self.name
