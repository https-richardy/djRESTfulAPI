from rest_framework.generics import (
    CreateAPIView, ListAPIView,
    UpdateAPIView, RetrieveAPIView
)

import django_filters
from store.utils import (CustomPagination, BookFilter)
from store.serializers import (BookSerializer, BookProduct)


class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
    pagination_class = CustomPagination


class BookListWithFilters(ListAPIView):
    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
    pagination_class = CustomPagination
    filterset_class = BookFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
    ordering_fields = ('price', 'title')
    search_field = ('title', 'author', 'genre')


class BookDetail(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()


class BookCreate(CreateAPIView):
    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()


class BookUpdate(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
