from rest_framework.generics import RetrieveAPIView

from ...serializers import ProductSerializer
from ...models import Product

class ProductDetailsView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
