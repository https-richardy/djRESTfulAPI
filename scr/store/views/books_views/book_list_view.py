from rest_framework.generics import ListAPIView
from store.utils import CustomPagination
from store.serializers import (BookSerializer, BookProduct)


class BookList(ListAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
    pagination_class = CustomPagination
