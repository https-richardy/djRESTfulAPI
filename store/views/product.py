from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    CreateAPIView
)

import django_filters
from store.utils import (CustomPagination, ProductFilter)
from store.serializers import (ProductSerializer, Product)


class ProductList(ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination


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


class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdate(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDelete(DestroyAPIView):
    serializer_class = ProductSerializer()
    queryset = Product.objects.all()
