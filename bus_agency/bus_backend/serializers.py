from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from django.db.models import fields
from rest_framework import serializers
from bus_backend.models import (
    Station,
    Route,
    Bus,
    Seat,
    Trip,
    Ticket,
)


class PassengerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    tickets = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'tickets',
            'password'
            ]

    def create(self, validated_data):
        user = super(PassengerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        passenger_group = Group.objects.get(name='Passenger')
        passenger_group.user_set.add(user)
        return user


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    content_type = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=ContentType.objects.all(),
        )

    class Meta:
        model = Permission
        fields = [
            'url',
            'name',
            'content_type',
            'codename',
            ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        )

    class Meta:
        model = Group
        fields = ['url', 'name', 'permissions']


class BusSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=User.objects.all(),
        required=False
        )

    class Meta:
        model = Bus
        fields = ['id', 'driver', 'type', 'manufacturer']


class SeatSerializer(serializers.ModelSerializer):
    bus = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Bus.objects.all(),
        )

    class Meta:
        model = Seat
        fields = ['id', 'bus', 'sequence_number']


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'street_address', 'city']


class RouteSerializer(serializers.ModelSerializer):
    from_station = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Station.objects.all(),
        )
    to_station = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Station.objects.all(),
        )

    class Meta:
        model = Route
        fields = ['id', 'from_station', 'to_station']


class TripSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Route.objects.all(),
        )
    bus = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Bus.objects.all(),
        )

    class Meta:
        model = Trip
        fields = ['id', 'route', 'bus', 'departure_time']


class TicketSerializer(serializers.ModelSerializer):
    trip = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Trip.objects.all(),
        )
    seat = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Seat.objects.all(),
        )

    passenger = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True
        )

    class Meta:
        model = Ticket
        fields = ['trip', 'seat', 'passenger']
