from typing import Sequence

from .product_views import (
    CreateProductView,
    DeleteProductView,
    ListProductView,
    ListProductsWithFiltersView,
    ProductDetailsView,
    UpdateProductView
)

__all__: Sequence[str] = [
    "CreateProductView",
    "DeleteProductView",
    "ListProductView",
    "ListProductsWithFiltersView",
    "ProductDetailsView",
    "UpdateProductView"
]