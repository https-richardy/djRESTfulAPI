from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from store.serializers import (BookSerializer, BookProduct)


class BookCreate(CreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = BookSerializer
    queryset = BookProduct.objects.all()
