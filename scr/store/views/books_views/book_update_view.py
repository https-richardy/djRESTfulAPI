from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from store.serializers import (BookSerializer, BookProduct)


class BookUpdate(UpdateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
