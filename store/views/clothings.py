from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    UpdateAPIView, CreateAPIView
)
import django_filters
from store.utils import (CustomPagination, ClothingFilter)
from store.serializers import (ClothingSerializer, ClothingProduct)


class ClothingList(ListAPIView):
    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
    pagination_class = CustomPagination


class ClothingListWithFilters(ListAPIView):
    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
    pagination_class = CustomPagination
    filterset_class = ClothingFilter
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]


class ClothingDetail(RetrieveAPIView):
    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()


class ClothingCreate(CreateAPIView):
    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()


class ClothingUpdate(UpdateAPIView):
    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
