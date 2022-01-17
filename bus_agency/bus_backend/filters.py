from django_filters import rest_framework as filters
from bus_backend.models import Trip


class TripFilter(filters.FilterSet):
    departure_date = filters.DateTimeFilter(
        field_name='departure_time',
        lookup_expr='gte'
    )
    arrival_date = filters.DateTimeFilter(
        field_name='departure_time',
        lookup_expr='lte'
    )

    class Meta:
        model = Trip
        fields = ('departure_date', 'arrival_date')
