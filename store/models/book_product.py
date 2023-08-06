from django.db import models
from store.models import Product


class BookProduct(Product):
    GENRE_CHOICES = (
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('romance', 'Romance'),
        ('mystery_thriller', 'Mystery & Thriller'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        ('biography', 'Biography'),
        ('self_help', 'Self-Help'),
        ('history', 'History'),
        ('travel', 'Travel'),
        ('cooking', 'Cooking'),
        ('poetry', 'Poetry'),
        ('graphic_novels', 'Graphic Novels'),
        ('children', 'Children'),
        ('young_adult', 'Young Adult'),
        ('classic', 'Classic'),
        ('horror', 'Horror'),
    )
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, null=True)
