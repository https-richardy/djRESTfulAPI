from rest_framework.serializers import ModelSerializer
from store.models import Product
from store.serializers import CategorySerializer


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
