import django_filters
from .models import *

class Orderfilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['product', 'status']
        
class Orderfilter2(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['product','customer', 'status']