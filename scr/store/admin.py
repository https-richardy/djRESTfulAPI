from django.contrib import admin
from .models import (
    Product,
    Category,
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock')
    list_filter = ('category', 'price')
    search_fields = ('id', 'title', 'category__title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )