import pytest

from django.contrib.auth.models import User
from django.db import transaction
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APIClient

from bus_backend.models import Bus, Seat


@pytest.fixture
def bus_data():
    return {
        'driver': 5,
        'wifi': True,
        'usb': True,
        'extra_leg_room': True,
        'entertainment': False
    }


@pytest.fixture
def update_data():
    return {
        'driver': '6',
        'wifi': False,
        'usb': False,
        'extra_leg_room': False,
        'entertainment': False
    }


@pytest.fixture
def partial_update_data():
    return {
        'driver': '6',
        'wifi': False
    }


@pytest.fixture
def unassigned_bus():
    bus = Bus.objects.create()
    with transaction.atomic():
        for i in range(10):
            Seat.objects.create(bus=bus, sequence_number=i+1)
    return bus


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db()
def test_get_bus_list_as_anonymous_user(client):
    url = reverse('bus-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_get_bus_list_as_authenticated_user(client, username):
    login = client.login(username=username, password='password123')
    url = reverse('bus-list')
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_create_bus_as_anonymous_user(client, bus_data):
    url = reverse('bus-list')
    response = client.post(url, bus_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Bus.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_create_bus_as_authenticated_user_without_permissions(
        client, bus_data, username):
    login = client.login(username=username, password='password123')
    url = reverse('bus-list')
    response = client.post(url, bus_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Bus.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_create_bus_as_authenticated_user_with_permissions(
        client, bus_data, username):
    login = client.login(username=username, password='password123')
    url = reverse('bus-list')
    response = client.post(url, bus_data, format='json')
    bus = Bus.objects.first()
    assert login
    assert response.status_code == status.HTTP_201_CREATED
    assert Bus.objects.count() == 1
    assert Seat.objects.count() == 10
    assert bus.wifi
    assert bus.usb
    assert bus.extra_leg_room
    assert not bus.entertainment


@pytest.mark.django_db()
def test_retrieve_bus_as_anonymous_user(client, unassigned_bus):
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_retrieve_bus_as_authenticated_user(client, username, unassigned_bus):
    login = client.login(username=username, password='password123')
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_update_bus_as_anonymous_user(client, unassigned_bus, update_data):
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.put(url, update_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_update_bus_as_authenticated_user_without_permissions(
        client, username, unassigned_bus, update_data):
    login = client.login(username=username, password='password123')
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.put(url, update_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_update_bus_as_authenticated_user_with_permissions(
        client, username, unassigned_bus, update_data):
    login = client.login(username=username, password='password123')
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    driver_2 = User.objects.get(username='driver_2')
    response = client.put(url, update_data, format='json')
    unassigned_bus.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert unassigned_bus.driver == driver_2
    assert not unassigned_bus.wifi
    assert not unassigned_bus.usb
    assert not unassigned_bus.extra_leg_room
    assert not unassigned_bus.entertainment


@pytest.mark.django_db()
def test_partial_update_bus_as_anonymous_user(
        client, unassigned_bus, partial_update_data):
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.patch(url, partial_update_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_partial_update_bus_as_authenticated_user_without_permissions(
        client, username, unassigned_bus, partial_update_data):
    login = client.login(username=username, password='password123')
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.patch(url, partial_update_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_partial_update_bus_as_authenticated_user_with_permissions(
        client, username, unassigned_bus, partial_update_data):
    login = client.login(username=username, password='password123')
    driver_2 = User.objects.get(username='driver_2')
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.patch(url, partial_update_data, format='json')
    unassigned_bus.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert unassigned_bus.driver == driver_2
    assert not unassigned_bus.wifi
    assert unassigned_bus.usb
    assert unassigned_bus.extra_leg_room
    assert unassigned_bus.entertainment


@pytest.mark.django_db()
def test_destroy_bus_as_anonymous_user(client, unassigned_bus):
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Bus.objects.count() == 1


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
def test_destroy_bus_as_authenticated_user(
        client, username, expected_status, expected_count, unassigned_bus):
    login = client.login(username=username, password='password123')
    url = reverse('bus-detail', kwargs={'pk': unassigned_bus.id})
    response = client.delete(url, format='json')
    assert login
    assert response.status_code == expected_status
    assert Bus.objects.count() == expected_count
