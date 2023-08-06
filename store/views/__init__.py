# flake8: noqa
from .product import (
    ProductList, ProductDetail,
    ProductUpdate, ProductDelete,
    ProductListWithFilters, ProductCreate
)


from .books import (
    BookList, BookListWithFilters,
    BookDetail, BookCreate,
    BookUpdate
)


from .clothings import(
    ClothingList, ClothingDetail,
    ClothingUpdate, ClothingCreate,
    ClothingListWithFilters,
)