from rest_framework.generics import RetrieveAPIView
from store.serializers import (ProductSerializer, Product)


class ProductDetail(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
