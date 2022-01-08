from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

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

class BusOnRoute(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()

class Passenger(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$', message="Phone number must be entered in the format: '+99999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    rut = models.CharField(max_length=10) # Formato: 00000000-0

class Ticket(models.Model):
    bus_on_route = models.ForeignKey(BusOnRoute, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE) 