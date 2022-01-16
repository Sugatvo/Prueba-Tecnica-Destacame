import pytest

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def passenger_data():
    return {
        'username': 'test_passenger',
        'first_name': 'Test',
        'last_name': 'Registration',
        'email': 'test@registration.cl',
        'password': 'password123',
    }


@pytest.fixture
def update_passenger_data():
    return {
        'username': 'update_passenger',
        'first_name': 'Update',
        'last_name': 'Passenger',
        'email': 'update@test.cl',
        'password': 'new_password123'
    }


@pytest.fixture
def partial_update_passenger_data():
    return {
        'first_name': 'Partial',
        'last_name': 'Update',
    }


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db()
def test_get_passenger_list_as_anonymous_user(client):
    url = reverse('passenger-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN),
        ('driver_1', 'password123', status.HTTP_403_FORBIDDEN),
        ('manager', 'password123', status.HTTP_200_OK),
        ('admin', 'password123', status.HTTP_200_OK),
    ]
)
def test_get_passenger_list_as_authenticated_user(
        client, username, password, expected_status):
    login = client.login(username=username, password=password)
    url = reverse('passenger-list')
    response = client.get(url)
    assert login
    assert response.status_code == expected_status


@pytest.mark.django_db()
def test_create_passenger_as_anonymous_user(client, passenger_data):
    url = reverse('passenger-list')
    response = client.post(url, passenger_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(groups__name='Passenger').count() == 3


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status, expected_count",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('driver_1', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('manager', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('admin', 'password123', status.HTTP_201_CREATED, 3),
    ]
)
def test_create_passenger_as_authenticated_user(
        client, passenger_data, username,
        password, expected_status, expected_count):
    login = client.login(username=username, password=password)
    url = reverse('passenger-list')
    response = client.post(url, passenger_data, format='json')
    assert login
    assert response.status_code == expected_status
    assert (
        User.objects.filter(groups__name='Passenger').count() == expected_count
        )


@pytest.mark.django_db()
def test_retrieve_passenger_as_anonymous_user(client):
    url = reverse('passenger-detail', kwargs={'pk': 2})
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ('passenger_1', 'password123', status.HTTP_200_OK),
        ('passenger_2', 'password123', status.HTTP_403_FORBIDDEN),
        ('driver_1', 'password123', status.HTTP_403_FORBIDDEN),
        ('manager', 'password123', status.HTTP_403_FORBIDDEN),
        ('admin', 'password123', status.HTTP_200_OK),
    ]
)
def test_retrieve_passenger_as_authenticated_user(
        client, username, password, expected_status):
    login = client.login(username=username, password=password)
    url = reverse('passenger-detail', kwargs={'pk': 2})
    response = client.get(url)
    assert login
    assert response.status_code == expected_status


@pytest.mark.django_db()
def test_update_passenger_as_anonymous_user(client, update_passenger_data):
    url = reverse('passenger-detail', kwargs={'pk': 2})
    response = client.put(url, update_passenger_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('passenger_2', 'password123'),
        ('driver_1', 'password123'),
        ('manager', 'password123'),
    ]
)
def test_update_passenger_as_authenticated_user_without_permissions(
        client, update_passenger_data, username, password):
    login = client.login(username=username, password=password)
    passenger_1 = User.objects.get(username='passenger_1')
    url = reverse('passenger-detail', kwargs={'pk': passenger_1.id})
    response = client.put(url, update_passenger_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('passenger_1', 'password123'),
        ('admin', 'password123'),
    ]
)
def test_update_passenger_as_authenticated_user_with_permissions(
        client, update_passenger_data, username, password):
    login = client.login(username=username, password=password)
    passenger_1 = User.objects.get(username='passenger_1')
    url = reverse('passenger-detail', kwargs={'pk': passenger_1.id})
    response = client.put(url, update_passenger_data, format='json')
    passenger_1.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert passenger_1.username == 'update_passenger'
    assert passenger_1.first_name == 'Update'
    assert passenger_1.last_name == 'Passenger'
    assert passenger_1.email == 'update@test.cl'


@pytest.mark.django_db()
def test_partial_update_passenger_as_anonymous_user(
        client, partial_update_passenger_data):
    url = reverse('passenger-detail', kwargs={'pk': 2})
    response = client.patch(url, partial_update_passenger_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('passenger_2', 'password123', ),
        ('driver_1', 'password123'),
        ('manager', 'password123'),
    ]
)
def test_partial_update_passenger_as_authenticated_user_without_permissions(
        client, partial_update_passenger_data, username, password):
    login = client.login(username=username, password=password)
    passenger_1 = User.objects.get(username='passenger_1')
    url = reverse('passenger-detail', kwargs={'pk': passenger_1.id})
    response = client.patch(url, partial_update_passenger_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('passenger_1', 'password123'),
        ('admin', 'password123'),
    ]
)
def test_partial_update_passenger_as_authenticated_user_with_permissions(
        client, partial_update_passenger_data, username, password):
    login = client.login(username=username, password=password)
    passenger_1 = User.objects.get(username='passenger_1')
    url = reverse('passenger-detail', kwargs={'pk': passenger_1.id})
    response = client.patch(url, partial_update_passenger_data, format='json')
    passenger_1.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert passenger_1.username == 'passenger_1'
    assert passenger_1.first_name == 'Partial'
    assert passenger_1.last_name == 'Update'
    assert not passenger_1.email


@pytest.mark.django_db()
def test_destroy_passenger_as_anonymous_user(client):
    url = reverse('passenger-detail', kwargs={'pk': 2})
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert User.objects.filter(groups__name='Passenger').count() == 2


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status, expected_count",
    [
        ('passenger_1', 'password123', status.HTTP_204_NO_CONTENT, 1),
        ('passenger_2', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('driver_1', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('manager', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('admin', 'password123', status.HTTP_204_NO_CONTENT, 1),
    ]
)
def test_destroy_passenger_as_authenticated_user(
        client, username, password, expected_status, expected_count):
    login = client.login(username=username, password=password)
    passenger_1 = User.objects.get(username='passenger_1')
    url = reverse('passenger-detail', kwargs={'pk': passenger_1.id})
    response = client.delete(url, format='json')
    assert login
    assert response.status_code == expected_status
    assert (
        User.objects.filter(groups__name='Passenger').count() == expected_count
        )
