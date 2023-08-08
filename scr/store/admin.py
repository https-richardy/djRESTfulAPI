from django.contrib import admin

from store.models import (
    Product, BookProduct,
    Category, ClothingProduct,
    EletronicProduct
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock')
    list_filter = ('category', 'price')
    search_fields = ('id', 'title', 'category__title')


@admin.register(BookProduct)
class BookProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'stock')
    list_filter = ('category', 'genre')
    search_fields = ('id', 'title', 'author', 'cateogry__title', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(ClothingProduct)
class ClothingProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'stock')
    list_filter = ('title', 'size', 'category', )
    search_fields = ('title', 'brand', 'category', 'category__title')


@admin.register(EletronicProduct)
class EletronicProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('title', 'brand', 'category__title')
