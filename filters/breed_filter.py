from django_filters import rest_framework as filters

from cats.models.cats import Cat


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CatFilter(filters.FilterSet):
    """Класс фильтрует котов по породе"""
    breed = CharFilterInFilter(field_name='breed__name', lookup_expr='in')

    class Meta:
        model = Cat
        fields = ['breed']