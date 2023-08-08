from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('clothing', 'Clothing'),
        ('eletronics', 'Eletronics'),
        ('books', 'Books'),
        ('shoes', 'Shoes'),
        ('toy_games', 'Toy & Games'),
        ('beauty_personal', 'Beauty & Personal'),
        ('jewelry_accessories', "Jewelry & Accessories")
    )
    title = models.CharField(max_length=25, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
