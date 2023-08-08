from rest_framework.generics import ListAPIView

import django_filters
from store.utils import (CustomPagination, ProductFilter)
from store.serializers import (ProductSerializer, Product)


class ProductListWithFilters(ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    pagination_class = CustomPagination
    filterset_class = ProductFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
