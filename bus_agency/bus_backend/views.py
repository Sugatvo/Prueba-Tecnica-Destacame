from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions

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
    IsAnonymousOrAdmin,
    IsOwnerOrReadOnly,
    IsAccountOwnerOrAdmin,
    IsManagerOrReadOnly,
    IsManagerOrAdmin,
    IsManager,
    IsDriver,
    IsPassenger
)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='Passenger')
    serializer_class = PassengerSerializer

    def get_permissions(self):
        # Only authenticated users can view all the passengers
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        # Only anonymous users can register as passengers.
        elif self.action == 'create':
            permission_classes = [IsAnonymousOrAdmin]
        # Only owner or superuser can retrieve, update,
        # partial_update or destroy the passanger account
        else:
            permission_classes = [IsAccountOwnerOrAdmin]
        return [permission() for permission in permission_classes]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='Driver')
    serializer_class = DriverSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsManagerOrAdmin
    ]


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManagerOrReadOnly
        ]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManagerOrReadOnly
        ]


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManagerOrReadOnly
        ]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def perform_create(self, serializer):
        serializer.save(passenger=self.request.user)
