from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)


class Driver(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)


class Administrator(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)


class Station(models.Model):
    street_address = models.CharField()
    city = models.CharField(max_length=28)


class Route(models.Model):
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE)


class Bus(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL)


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    sequence_number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        unique_together = ('bus', 'sequence_number',)


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()


class Passenger(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    phone_regex = RegexValidator(
        regex=r'^(\+?56)?(\s?)(9)(\s?)\d{4}(\s?)\d{4}',
        message="Número de télefono invalido.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    rut_regex = RegexValidator(
        regex=r'^d{8}-\d{1}$',
        message="Ingrese RUT sin puntos y con guión.")
    rut = models.CharField(max_length=10)  # Formato: 00000000-0
    email = models.EmailField()


class Ticket(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
