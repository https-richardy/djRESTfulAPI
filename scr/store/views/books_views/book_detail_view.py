from rest_framework.generics import RetrieveAPIView
from store.serializers import (BookSerializer, BookProduct)


class BookDetail(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
