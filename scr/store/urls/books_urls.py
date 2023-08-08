from django.urls import path
from store.views import (
    BookList, BookListWithFilters,
    BookDetail, BookCreate,
    BookUpdate,
)

urlpatterns = [
    path('books/', BookList.as_view(), name='books-list'),
    path('books/search/', BookListWithFilters.as_view(), name='books-search'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
]
