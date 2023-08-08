from rest_framework.serializers import ModelSerializer
from store.serializers import CategorySerializer
from store.models import EletronicProduct


class EletronicSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = EletronicProduct
        fields = '__all__'
