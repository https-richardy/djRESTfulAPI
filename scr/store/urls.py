from django.urls import path
from .views.product_views import (
    ListProductView,
    ListProductsWithFiltersView,
    CreateProductView,
    ProductDetailsView,
    UpdateProductView,
    DeleteProductView,
)

urlpatterns = [
    path('products/', ListProductView.as_view(), name='products-list'),
    path('products/search/', ListProductsWithFiltersView.as_view(), name='product-search'),  # noqa: E501
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product-detail'),
    path('products/', CreateProductView.as_view(), name='product-create'),
    path('products/<int:pk>/', UpdateProductView.as_view(), name='product-update'),  # noqa: E501
    path('products/<int:pk>/', DeleteProductView.as_view(), name='product-delete')  # noqa: E501
]
