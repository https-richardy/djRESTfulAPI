from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from store.serializers import (ClothingProduct, ClothingSerializer)


class ClothingCreate(CreateAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]

    serializer_class = ClothingSerializer
    queryset = ClothingProduct.objects.all()
