# flake8: noqa
from .products_views import (
    ProductList, ProductDetail,
    ProductUpdate, ProductDelete,
    ProductListWithFilters, ProductCreate
)


from .books_views import (
    BookList, BookListWithFilters,
    BookDetail, BookCreate,
    BookUpdate
)


from .clothings_views import(
    ClothingList, ClothingDetail,
    ClothingUpdate, ClothingCreate,
    ClothingListWithFilters,
)