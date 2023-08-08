from rest_framework.serializers import ModelSerializer
from store.models import BookProduct
from store.serializers import CategorySerializer


class BookSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = BookProduct
        fields = '__all__'
