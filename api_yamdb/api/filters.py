from django_filters import FilterSet
from django_filters.filters import CharFilter, NumberFilter

from reviews.models import Title


class TitleFilter(FilterSet):
    category = CharFilter(
        field_name='category__slug',
        lookup_expr='icontains'
    )
    genre = CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )
    name = CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )
    year = NumberFilter(
        field_name='year',
        lookup_expr='exact'
    )

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year')
