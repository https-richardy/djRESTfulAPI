from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from store.serializers import (ClothingSerializer, ClothingProduct)


class ClothingUpdate(UpdateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
