import django_filters
from django_filters import DateFilter
from django.contrib.auth.models import User

from .models import *
#filter Search Submissions
class HealthFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_joined", lookup_expr='gte')
    end_date = DateFilter(field_name="date_joined", lookup_expr='lte')
    class Meta:
        model = Health
        fields = ['name', 'email' ]
        exlude = ['name', 'email', 'date_joined']


class UserFilter(django_filters.FilterSet):
    start_dateU = DateFilter(field_name="last_login", lookup_expr='gte')
    end_dateU = DateFilter(field_name="last_login", lookup_expr='lte')
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        exlude = ['username', 'email', 'last_login']