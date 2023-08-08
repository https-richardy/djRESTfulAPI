from rest_framework.generics import ListAPIView
import django_filters

from store.utils import (CustomPagination, BookFilter)
from store.serializers import (BookSerializer, BookProduct)


class BookListWithFilters(ListAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()

    pagination_class = CustomPagination

    filterset_class = BookFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
    search_field = ('title', 'author', 'genre')
