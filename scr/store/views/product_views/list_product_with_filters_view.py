from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from ...utils import (CustomPagination, ProductFilter)
from ...serializers import ProductSerializer
from ...models import Product

class ListProductsWithFiltersView(ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    pagination_class = CustomPagination
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend
    ]
