import json

from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

from django_filters import rest_framework as filters
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.db.models import F
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication
)
from rest_framework import permissions, viewsets, generics, status
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
    ChangePasswordSerializer
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
    def routes_by_city(self, request):
        routes = (
            Route.objects.all()
            .select_related("from_station", "to_station")
            .only("id", "from_station__city", "to_station__city")
            .order_by('from_station__city')
            .values(
                "id",
                from_city=F('from_station__city'),
                to_city=F('to_station__city')
            )
        )
        return Response(routes)

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


def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    if request.user.groups.filter(name='Passenger').exists():
        role = "Passenger"
    elif request.user.groups.filter(name='Manager').exists():
        role = "Manager"
    elif request.user.groups.filter(name='Driver').exists():
        role = "Driver"
    elif request.user.is_superuser:
        role = "Superuser"
    else:
        role = None

    return JsonResponse({
        'role': role,
        'username': request.user.username,
        'id': request.user.id
    })


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse(
            {'detail': 'Please provide username and password.'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not user.check_password(old_password):
                return Response(
                    {'old_password': ['Wrong password.']},
                    status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get('new_password'))
            user.save()
            update_session_auth_hash(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
