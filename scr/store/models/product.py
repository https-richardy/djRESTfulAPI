from django.db import models
from store.models import Category


class Product(models.Model):
    title = models.CharField(max_length=120)
    cover = models.ImageField(upload_to='imgs/products/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
