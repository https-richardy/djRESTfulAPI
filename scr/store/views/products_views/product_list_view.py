from rest_framework.generics import ListAPIView

from store.utils import CustomPagination
from store.serializers import (ProductSerializer, Product)


class ProductList(ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
