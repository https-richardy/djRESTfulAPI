import django_filters
from store.models import BookProduct


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )
    author = django_filters.CharFilter(
        field_name='author',
        lookup_expr='icontains'
    )
    genre = django_filters.CharFilter(
        field_name='genre'
    )
    language = django_filters.CharFilter(
        field_name='language'
    )

    class Meta:
        model = BookProduct
        fields = ('min_price', 'max_price', 'title', 'genre', 'author', 'language')  # noqa