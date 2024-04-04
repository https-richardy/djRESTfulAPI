from rest_framework.generics import ListAPIView

from ...utils import CustomPagination
from ...serializers import ProductSerializer
from ...models import Product

class ListProductView(ListAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
