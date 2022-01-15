from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)

from bus_backend.models import (
    Station,
    Route,
    Bus,
    Ticket,
    Trip
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

from bus_backend.permissions import (
    PassengerPermissions,
    DriverPermissions,
    StationPermissions,
    RoutePermissions,
    BusPermissions,
    TicketPermissions,
    TripPermissions
)


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
