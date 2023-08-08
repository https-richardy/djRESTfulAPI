from rest_framework.generics import DestroyAPIView
from rest_framework import permissions
from store.serializers import (ProductSerializer, Product)


class ProductDelete(DestroyAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = ProductSerializer()
    queryset = Product.objects.all()
