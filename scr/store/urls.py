from django.urls import path
from .views import (
    ProductCreate,
    ProductList,
    ProductDetail,
    ProductUpdate,
    ProductDelete,
    ProductListWithFilters,
)

urlpatterns = [
    path('products/', ProductList.as_view(), name='products-list'),
    path('products/search/', ProductListWithFilters.as_view(), name='product-search'),  # noqa: E501
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product/create/', ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product-update'),  # noqa: E501
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product-delete')  # noqa: E501
]
