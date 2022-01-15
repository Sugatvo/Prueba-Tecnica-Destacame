from django.contrib.auth.models import Group, User

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
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'tickets', 'password']
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True},
                        'email': {'required': True}}

    def create(self, validated_data):
        user = super(PassengerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        passenger_group = Group.objects.get(name='Passenger')
        passenger_group.user_set.add(user)
        return user


class DriverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']

    def create(self, validated_data):
        user = super(DriverSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        passenger_group = Group.objects.get(name='Driver')
        passenger_group.user_set.add(user)
        return user


class BusSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=User.objects.filter(groups__name='Driver'),
        required=False,
    )
    seats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Bus
        fields = ['id', 'driver', 'type', 'manufacturer', 'seats']


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

    passenger = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'trip', 'seat', 'passenger']
