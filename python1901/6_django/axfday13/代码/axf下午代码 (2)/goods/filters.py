
import django_filters

from goods.models import Goods


class GoodFilter(django_filters.rest_framework.FilterSet):
    # typeid  childcid  order_rule
    typeid = django_filters.CharFilter('categoryid')
    childcid = django_filters.CharFilter(method='filter_child')
    order_rule = django_filters.CharFilter(method='filter_rule')

    class Meta:
        model = Goods
        fields = ['categoryid']

    def filter_child(self, queryset, name, value):
        if value == '0':
            return queryset
        else:
            return queryset.filter(childcid=value)

    def filter_rule(self, queryset, name, value):
        if value == '0':
            return queryset
        elif value == '1':
            return queryset.order_by('marketprice')
        elif value == '2':
            return queryset.order_by('-marketprice')
        elif value == '3':
            return queryset.order_by('productnum')
        else:
            return queryset.order_by('-productnum')
