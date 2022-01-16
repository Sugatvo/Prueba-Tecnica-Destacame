import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from bus_backend.models import Station, Route


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
def algarrobo_station():
    return Station.objects.create(
        name='Terminal de Algarrobo',
        street_address='John Doe 8752',
        city='Algarrobo'
    )


@pytest.fixture
def route(santiago_station, coquimbo_station):
    return Route.objects.create(
        from_station=santiago_station,
        to_station=coquimbo_station
    )


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db()
def test_get_route_list_as_anonymous_user(client):
    url = reverse('route-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_get_route_list_as_authenticated_user(client, username):
    login = client.login(username=username, password='password123')
    url = reverse('route-list')
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_create_route_as_anonymous_user(
        client, santiago_station, coquimbo_station):
    url = reverse('route-list')
    route_data = {
        'from_station': santiago_station.id,
        'to_station': coquimbo_station.id
    }
    response = client.post(url, route_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Route.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_create_route_as_authenticated_user_without_permissions(
        client, username, santiago_station, coquimbo_station):
    login = client.login(username=username, password='password123')
    url = reverse('route-list')
    route_data = {
        'from_station': santiago_station.id,
        'to_station': coquimbo_station.id
    }
    response = client.post(url, route_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Route.objects.count() == 0


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_create_route_as_authenticated_user_with_permissions(
        client, username, santiago_station, coquimbo_station):
    login = client.login(username=username, password='password123')
    url = reverse('route-list')
    route_data = {
        'from_station': santiago_station.id,
        'to_station': coquimbo_station.id
    }
    response = client.post(url, route_data, format='json')
    assert login
    assert response.status_code == status.HTTP_201_CREATED
    assert Route.objects.count() == 1


@pytest.mark.django_db()
def test_retrieve_route_as_anonymous_user(client, route):
    url = reverse('route-detail', kwargs={'pk': route.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username", ['passenger_1', 'driver_1', 'manager', 'admin']
)
def test_retrieve_route_as_authenticated_user(
        client, username, route):
    login = client.login(username=username, password='password123')
    url = reverse('route-detail', kwargs={'pk': route.id})
    response = client.get(url)
    assert login
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db()
def test_update_route_as_anonymous_user(
        client, santiago_station, coquimbo_station, route):
    url = reverse('route-detail', kwargs={'pk': route.id})
    update_data = {
        'from_station': coquimbo_station.id,
        'to_station': santiago_station.id
    }
    response = client.put(url, update_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_update_route_as_authenticated_user_without_permissions(
        client, username, santiago_station, coquimbo_station, route):
    login = client.login(username=username, password='password123')
    url = reverse('route-detail', kwargs={'pk': route.id})
    update_data = {
        'from_station': coquimbo_station.id,
        'to_station': santiago_station.id
    }
    response = client.put(url, update_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_update_route_as_authenticated_user_with_permissions(
        client, username, santiago_station, coquimbo_station, route):
    login = client.login(username=username, password='password123')
    url = reverse('route-detail', kwargs={'pk': route.id})
    update_data = {
        'from_station': coquimbo_station.id,
        'to_station': santiago_station.id
    }
    response = client.put(url, update_data, format='json')
    route.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert route.from_station == coquimbo_station
    assert route.to_station == santiago_station


@pytest.mark.django_db()
def test_partial_update_route_as_anonymous_user(
        client, route, algarrobo_station):
    url = reverse('route-detail', kwargs={'pk': route.id})
    partial_update_data = {
        'to_station': algarrobo_station.id
    }
    response = client.patch(url, partial_update_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['passenger_1', 'driver_1'])
def test_partial_update_route_as_authenticated_user_without_permissions(
        client, username, route, algarrobo_station):
    login = client.login(username=username, password='password123')
    url = reverse('route-detail', kwargs={'pk': route.id})
    partial_update_data = {
        'to_station': algarrobo_station.id
    }
    response = client.patch(url, partial_update_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize("username", ['manager', 'admin'])
def test_partial_update_route_as_authenticated_user_with_permissions(
        client, username, route, algarrobo_station, santiago_station):
    login = client.login(username=username, password='password123')
    url = reverse('route-detail', kwargs={'pk': route.id})
    partial_update_data = {
        'to_station': algarrobo_station.id
    }
    response = client.patch(url, partial_update_data, format='json')
    route.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert route.from_station == santiago_station
    assert route.to_station == algarrobo_station


@pytest.mark.django_db()
def test_destroy_route_as_anonymous_user(client, route):
    url = reverse('route-detail', kwargs={'pk': route.id})
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Route.objects.count() == 1


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
def test_destroy_route_as_authenticated_user(
        client, username, expected_status, expected_count, route):
    login = client.login(username=username, password='password123')
    url = reverse('route-detail', kwargs={'pk': route.id})
    response = client.delete(url, format='json')
    assert login
    assert response.status_code == expected_status
    assert Route.objects.count() == expected_count
