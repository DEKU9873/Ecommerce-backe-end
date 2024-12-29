import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['title', 'brand', 'category', 'price', 'keyword']