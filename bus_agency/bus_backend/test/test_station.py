import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from bus_backend.models import Station


@pytest.fixture
def station_data():
    return {
        "name": "Terminal de test",
        "street_address": "test 1234",
        "city": "Testing"
    }


@pytest.fixture
def partial_station_data():
    return {"name": "Terminal de test"}


@pytest.fixture
def station():
    return Station.objects.create(
        name='Terminal de John Doe',
        street_address='John Doe 8752',
        city='John Doe City'
    )


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db()
def test_get_station_list_as_anonymous_user(client):
    url = reverse('station-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_get_station_list_as_authenticated_user(client, username,):
    login = client.login(username=username, password='password123')
    url = reverse('station-list')
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_create_station_as_anonymous_user(client, station_data):
    url = reverse('station-list')
    response = client.post(url, station_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Station.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, expected_status, expected_count",
    [
        ('passenger_1', status.HTTP_403_FORBIDDEN, 0),
        ('driver_1', status.HTTP_403_FORBIDDEN, 0),
        ('manager', status.HTTP_201_CREATED, 1),
        ('admin', status.HTTP_201_CREATED, 1),
    ]
)
def test_create_station_as_authenticated_user(
        client, station_data, username, expected_status, expected_count):
    login = client.login(username=username, password='password123')
    url = reverse('station-list')
    response = client.post(url, station_data, format='json')
    assert login
    assert response.status_code == expected_status
    assert Station.objects.count() == expected_count


@pytest.mark.django_db()
def test_retrieve_station_as_anonymous_user(client, station):
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_retrieve_station_as_authenticated_user(client, username, station):
    login = client.login(username=username, password='password123')
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_update_station_as_anonymous_user(client, station_data, station):
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.put(url, station_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_update_station_as_authenticated_user_without_permissions(
        client, station_data, username, station):
    login = client.login(username=username, password='password123')
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.put(url, station_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_update_station_as_authenticated_user_with_permissions(
        client, station_data, username, station):
    login = client.login(username=username, password='password123')
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.put(url, station_data, format='json')
    station.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert station.name == 'Terminal de test'
    assert station.street_address == 'test 1234'
    assert station.city == 'Testing'


@pytest.mark.django_db()
def test_partial_update_station_as_anonymous_user(
        client, partial_station_data, station):
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.patch(url, partial_station_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_partial_update_station_as_authenticated_user_without_permissions(
        client, partial_station_data, username, station):
    login = client.login(username=username, password='password123')
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.patch(url, partial_station_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_partial_update_station_as_authenticated_user_with_permissions(
        client, partial_station_data, username, station):
    login = client.login(username=username, password='password123')
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.patch(url, partial_station_data, format='json')
    station.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert station.name == 'Terminal de test'
    assert station.street_address == 'John Doe 8752'
    assert station.city == 'John Doe City'


@pytest.mark.django_db()
def test_destroy_station_as_anonymous_user(client, station):
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Station.objects.count() == 1


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
def test_destroy_station_as_authenticated_user(
        client, username, expected_status, expected_count, station):
    login = client.login(username=username, password='password123')
    url = reverse('station-detail', kwargs={'pk': station.id})
    response = client.delete(url, format='json')
    assert login
    assert response.status_code == expected_status
    assert Station.objects.count() == expected_count
