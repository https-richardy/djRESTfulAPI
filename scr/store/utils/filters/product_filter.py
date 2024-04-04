import django_filters
from ...models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )
    category = django_filters.CharFilter(
        field_name='category__title',
    )

    class Meta:
        model = Product
        fields = ('min_price', 'max_price', 'title', 'category')
