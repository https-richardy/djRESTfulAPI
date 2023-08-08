from rest_framework.generics import ListAPIView
import django_filters
from store.utils import (CustomPagination, ClothingFilter)
from store.serializers import (ClothingSerializer, ClothingProduct)


class ClothingListWithFilters(ListAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
    pagination_class = CustomPagination

    filterset_class = ClothingFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
