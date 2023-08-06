from rest_framework.serializers import ModelSerializer
from store.serializers import CategorySerializer
from store.models import ClothingProduct


class ClothingSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ClothingProduct
        fields = '__all__'
