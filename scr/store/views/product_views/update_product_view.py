from rest_framework.generics import UpdateAPIView
from rest_framework import permissions

from ...serializers import ProductSerializer
from ...models import Product

class UpdateProductView(UpdateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
