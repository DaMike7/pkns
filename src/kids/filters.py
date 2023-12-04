import django_filters as df
from base.models import *

class KidFilter(df.FilterSet):
    class Meta:
        model = Kid
        fields = ['full_name']

class PaymentFilter(df.FilterSet):
    class Meta:
        model = Payment
        fields = ['paid_on']