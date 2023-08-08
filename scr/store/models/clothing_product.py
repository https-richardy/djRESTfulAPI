from django.db import models
from store.models import Product


class ClothingProduct(Product):
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=35, null=True, blank=True)
