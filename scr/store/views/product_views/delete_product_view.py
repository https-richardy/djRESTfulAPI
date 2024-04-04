from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from ...serializers import ProductSerializer
from ...models import Product

class DeleteProductView(DestroyAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = ProductSerializer()
    queryset = Product.objects.all()
