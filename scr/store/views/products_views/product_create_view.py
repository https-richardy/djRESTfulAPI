from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from store.serializers import (ProductSerializer, Product)


class ProductCreate(CreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
