import django_filters
from store.models import ClothingProduct


class ClothingFilter(django_filters.FilterSet):
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )
    brand = django_filters.CharFilter(
        field_name='brand',
        lookup_expr='icontains'
    )
    size = django_filters.CharFilter(
        field_name='size'
    )
    color = django_filters.CharFilter(
        field_name='color',
        lookup_expr='icontains'
    )

    class Meta:
        model = ClothingProduct
        fields = ('max_price', 'min_price', 'title', 'brand', 'color', 'size')
