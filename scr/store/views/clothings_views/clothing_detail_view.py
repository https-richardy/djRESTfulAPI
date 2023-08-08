from rest_framework.generics import RetrieveAPIView
from store.serializers import (ClothingSerializer, ClothingProduct)


class ClothingDetail(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
