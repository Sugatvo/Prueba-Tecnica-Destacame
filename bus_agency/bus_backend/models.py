from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=28)


class Route(models.Model):
    from_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="from_station"
    )
    to_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="to_station"
    )

    class Meta:
        unique_together = ('from_station', 'to_station')


class Bus(models.Model):
    driver = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        unique=True
    )
    wifi = models.BooleanField(null=False, blank=False, default=True)
    usb = models.BooleanField(null=False, blank=False, default=True)
    extra_leg_room = models.BooleanField(null=False, blank=False, default=True)
    entertainment = models.BooleanField(null=False, blank=False, default=True)


class Seat(models.Model):
    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        related_name='seats'
    )
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
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('trip', 'seat',)
