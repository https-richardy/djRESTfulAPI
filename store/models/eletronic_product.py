from django.db import models
from store.models import Product


class EletronicProduct(Product):
    brand = models.CharField(max_length=50)
