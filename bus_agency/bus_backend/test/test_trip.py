import pytest

from django.urls import reverse
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from datetime import date

from rest_framework import status
from rest_framework.test import APIClient

from bus_backend.models import Bus, Seat, Station, Route, Trip


@pytest.fixture
def bus_1():
    bus = Bus.objects.create()
    with transaction.atomic():
        for i in range(10):
            Seat.objects.create(bus=bus, sequence_number=i+1)
    return bus


@pytest.fixture
def bus_2():
    bus = Bus.objects.create()
    with transaction.atomic():
        for i in range(10):
            Seat.objects.create(bus=bus, sequence_number=i+1)
    return bus


@pytest.fixture
def santiago_station():
    return Station.objects.create(
        name='Terminal de Santiago',
        street_address='John Doe 8752',
        city='Santiago'
    )


@pytest.fixture
def coquimbo_station():
    return Station.objects.create(
        name='Terminal de Coquimbo',
        street_address='John Doe 8752',
        city='Coquimbo'
    )


@pytest.fixture
def route_1(santiago_station, coquimbo_station):
    return Route.objects.create(
        from_station=santiago_station,
        to_station=coquimbo_station
    )


@pytest.fixture
def route_2(santiago_station, coquimbo_station):
    return Route.objects.create(
        from_station=coquimbo_station,
        to_station=santiago_station
    )


@pytest.fixture
def aware_date_1():
    today = date.today()
    time = '09:00:00'
    datetime_str = today.strftime("%Y-%m-%d") + " " + time
    unaware_date = parse_datetime(datetime_str)
    aware_date = timezone.make_aware(
        unaware_date,
        timezone.get_current_timezone()
    )
    return aware_date


@pytest.fixture
def aware_date_2():
    today = date.today()
    time = '12:00:00'
    datetime_str = today.strftime("%Y-%m-%d") + " " + time
    unaware_date = parse_datetime(datetime_str)
    aware_date = timezone.make_aware(
        unaware_date,
        timezone.get_current_timezone()
    )
    return aware_date


@pytest.fixture
def trip_data(bus_1, route_1, aware_date_1):
    return {
        'bus': bus_1.id,
        'route': route_1.id,
        'departure_time': aware_date_1
    }


@pytest.fixture
def update_data(bus_2, route_2, aware_date_2):
    return {
        'bus': bus_2.id,
        'route': route_2.id,
        'departure_time': aware_date_2
    }


@pytest.fixture
def trip_1(route_1, bus_1, aware_date_1):
    return Trip.objects.create(
        route=route_1,
        bus=bus_1,
        departure_time=aware_date_1
    )


@pytest.fixture
def trip_2(route_2, bus_2, aware_date_2):
    return Trip.objects.create(
        route=route_2,
        bus=bus_2,
        departure_time=aware_date_2
    )


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db()
def test_get_trip_list_as_anonymous_user(client):
    url = reverse('trip-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_get_trip_list_as_authenticated_user(client, username):
    login = client.login(username=username, password='password123')
    url = reverse('trip-list')
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_create_trip_as_anonymous_user(client, trip_data):
    url = reverse('trip-list')
    response = client.post(url, trip_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Trip.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_create_trip_as_authenticated_user_without_permissions(
        client, username, trip_data):
    login = client.login(username=username, password='password123')
    url = reverse('trip-list')
    response = client.post(url, trip_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Trip.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_create_trip_as_authenticated_user_with_permissions(
        client, username, trip_data):
    login = client.login(username=username, password='password123')
    url = reverse('trip-list')
    response = client.post(url, trip_data, format='json')
    assert login
    assert response.status_code == status.HTTP_201_CREATED
    assert Trip.objects.count() == 1


@pytest.mark.django_db()
def test_retrieve_trip_as_anonymous_user(client, trip_1):
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_retrieve_trip_as_authenticated_user(client, username, trip_1):
    login = client.login(username=username, password='password123')
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_update_trip_as_anonymous_user(
        client, trip_1, update_data):
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.put(url, update_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_update_trip_as_authenticated_user_without_permissions(
        client, username, trip_1, update_data):
    login = client.login(username=username, password='password123')
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.put(url, update_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_update_trip_as_authenticated_user_with_permissions(
        client, username, trip_1, update_data, route_2, bus_2, aware_date_2):
    login = client.login(username=username, password='password123')
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.put(url, update_data, format='json')
    trip_1.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert trip_1.bus == bus_2
    assert trip_1.route == route_2
    assert trip_1.departure_time == aware_date_2


@pytest.mark.django_db()
def test_partial_update_trip_as_anonymous_user(
        client, trip_1, aware_date_2):
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    partial_update_data = {'departure_time': aware_date_2}
    response = client.patch(url, partial_update_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_partial_update_trip_as_authenticated_user_without_permissions(
        client, username, trip_1, aware_date_2):
    login = client.login(username=username, password='password123')
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    partial_update_data = {'departure_time': aware_date_2}
    response = client.patch(url, partial_update_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_partial_update_trip_as_authenticated_user_with_permissions(
        client, username, trip_1, bus_1, route_1, aware_date_2):
    login = client.login(username=username, password='password123')
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    partial_update_data = {'departure_time': aware_date_2}
    response = client.patch(url, partial_update_data, format='json')
    trip_1.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert trip_1.bus == bus_1
    assert trip_1.route == route_1
    assert trip_1.departure_time == aware_date_2


@pytest.mark.django_db()
def test_destroy_trip_as_anonymous_user(client, trip_1):
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Trip.objects.count() == 1


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, expected_status, expected_count",
    [
        ('passenger_1', status.HTTP_403_FORBIDDEN, 1),
        ('driver_1', status.HTTP_403_FORBIDDEN, 1),
        ('manager', status.HTTP_204_NO_CONTENT, 0),
        ('admin', status.HTTP_204_NO_CONTENT, 0),
    ]
)
def test_destroy_trip_as_authenticated_user(
        client, username, expected_status, expected_count, trip_1):
    login = client.login(username=username, password='password123')
    url = reverse('trip-detail', kwargs={'pk': trip_1.id})
    response = client.delete(url, format='json')
    assert login
    assert response.status_code == expected_status
    assert Trip.objects.count() == expected_count
