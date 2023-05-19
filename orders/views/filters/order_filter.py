import django_filters
from django.db import models
from django.forms import forms


from orders.models.order import Order


# class OrderFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Order
#         fields = {
#             'supplier': ['contains'],
#             'product_name': ['contains'], 'quantity': ['lt', 'gt'],
#             'unit_price': ['lt', 'gt'], 'cost_price': ['lt', 'gt'],
#             'date_added': ['exact', 'contains'],
#             'is_fulfilled': ['exact'], 'date_fulfilled': ['exact', 'contains'],
#             'other_info': ['contains'], 'date_updated': ['exact', 'contains']
#         }


class OrderFilter(django_filters.FilterSet):
    supplier = django_filters.AllValuesFilter()

    class Meta:
        model = Order
        fields = ['supplier']