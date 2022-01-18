from django.contrib.auth.models import User

from django_filters import rest_framework as filters
from django.db.models import F

from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication
)
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from bus_backend.models import (
    Station,
    Route,
    Bus,
    Ticket,
    Trip
)
from bus_backend.permissions import (
    PassengerPermissions,
    DriverPermissions,
    StationPermissions,
    RoutePermissions,
    BusPermissions,
    TicketPermissions,
    TripPermissions
)
from bus_backend.serializers import (
    PassengerSerializer,
    DriverSerializer,
    StationSerializer,
    RouteSerializer,
    BusSerializer,
    TripSerializer,
    TicketSerializer,
)

from bus_backend.filters import TripFilter


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='Passenger')
    serializer_class = PassengerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [PassengerPermissions]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='Driver')
    serializer_class = DriverSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        DriverPermissions
    ]


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        StationPermissions
    ]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        RoutePermissions,
    ]

    @action(detail=False)
    def departure_cities(self, request):
        """
        Get all the departure cities available from routes
        """
        cities = (
            Route.objects.all()
            .select_related("from_station")
            .distinct("from_station")
            .only("from_station", "from_station__city")
            .values("from_station", city=F('from_station__city'))
        )
        return Response(cities)

    @action(detail=False)
    def arrival_cities(self, request):
        """
        Gets all the arrival cities available from the departure city.
        """
        from_station = request.query_params.get('from_station')
        cities = (
            Route.objects.filter(from_station=from_station)
            .select_related("to_station")
            .distinct("to_station")
            .only("to_station", "to_station__city")
            .values("to_station", city=F('to_station__city'))
        )
        return Response(cities)


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        BusPermissions
    ]


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        TripPermissions
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TripFilter


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        TicketPermissions
    ]

    def perform_create(self, serializer):
        serializer.save(passenger=self.request.user)
