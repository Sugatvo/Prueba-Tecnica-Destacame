from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class Station(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=28)


class Route(models.Model):
    from_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="from_station")

    to_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="to_station")


class Bus(models.Model):
    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    type = models.CharField(
        max_length=255,
        default="Modelo FSO 1701 con retardador incorporado")
    manufacturer = models.CharField(max_length=255, default="Yutong")


class Seat(models.Model):
    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        related_name='seats')
    sequence_number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        unique_together = ('bus', 'sequence_number',)


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()


class Ticket(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passenger = models.ForeignKey(
        User,
        related_name='tickets',
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ('trip', 'seat',)
