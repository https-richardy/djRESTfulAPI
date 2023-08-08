from rest_framework.generics import ListAPIView
from store.serializers import (ClothingSerializer, ClothingProduct)
from store.utils import CustomPagination


class ClothingList(ListAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
    pagination_class = CustomPagination
