from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

from bus_backend.models import (
    Station,
    Route,
    Bus,
    Seat,
    Ticket,
    Trip
)

from bus_backend.serializers import (
    PassengerSerializer,
    StationSerializer,
    RouteSerializer,
    BusSerializer,
    SeatSerializer,
    TripSerializer,
    TicketSerializer,
)

from bus_backend.permissions import (
    IsOwnerOrReadOnly,
    IsOwnerOrAdmin,
    IsManager,
    IsDriver,
    IsPassenger
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'passenger': reverse('passenger-list', request=request, format=format),
        'stations': reverse('station-list', request=request, format=format),
        'routes': reverse('route-list', request=request, format=format),
        'buses': reverse('bus-list', request=request, format=format),
        'seats': reverse('seat-list', request=request, format=format),
        'trips': reverse('trip-list', request=request, format=format),
        'tickets': reverse('ticket-list', request=request, format=format)
    })


class PassengerList(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Passenger')
    serializer_class = PassengerSerializer
    permission_classes = [permissions.AllowAny]


class PassengerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Passenger')
    serializer_class = PassengerSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrAdmin
        ]


class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class BusList(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class BusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class SeatList(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class SeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsManager
        ]


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def perform_create(self, serializer):
        serializer.save(passenger=self.request.user)


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]
