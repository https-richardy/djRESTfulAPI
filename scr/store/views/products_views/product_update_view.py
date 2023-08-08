from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from store.serializers import (ProductSerializer, Product)


class ProductUpdate(UpdateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
