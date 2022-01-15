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
        ('driver', 'password123', status.HTTP_403_FORBIDDEN),
        ('manager', 'password123', status.HTTP_200_OK),
        ('admin', 'password123', status.HTTP_200_OK),
    ]
)
def test_get_passenger_list_as_authenticated_user(client, username, password, expected_status):
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
    assert User.objects.count() == 6


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status, expected_count",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN, 5),
        ('driver', 'password123', status.HTTP_403_FORBIDDEN, 5),
        ('manager', 'password123', status.HTTP_403_FORBIDDEN, 5),
        ('admin', 'password123', status.HTTP_201_CREATED, 6),
    ]
)
def test_create_passenger_as_authenticated_user(client, passenger_data, username, password, expected_status, expected_count):
    login = client.login(username=username, password=password)
    url = reverse('passenger-list')
    response = client.post(url, passenger_data, format='json')
    assert login
    assert response.status_code == expected_status
    assert User.objects.count() == expected_count


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
        ('driver', 'password123', status.HTTP_403_FORBIDDEN),
        ('manager', 'password123', status.HTTP_403_FORBIDDEN),
        ('admin', 'password123', status.HTTP_200_OK),
    ]
)
def test_retrieve_passenger_as_authenticated_user(client, username, password, expected_status):
    login = client.login(username=username, password=password)
    url = reverse('passenger-detail', kwargs={'pk': 2})
    response = client.get(url)
    assert login
    assert response.status_code == expected_status
