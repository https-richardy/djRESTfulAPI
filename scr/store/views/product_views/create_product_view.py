from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from ...serializers import ProductSerializer
from ...models import Product

class CreateProductView(CreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
