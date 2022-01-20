import pytest

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def driver_data():
    return {
        'username': 'driver_passenger',
        'first_name': 'Driver',
        'last_name': 'Registration',
        'email': 'test@registration.cl',
        'password': 'password123',
    }


@pytest.fixture
def update_driver_data():
    return {
        'username': 'update_driver',
        'first_name': 'Update',
        'last_name': 'Driver',
        'email': 'update@test.cl',
        'password': 'new_password123'
    }


@pytest.fixture
def partial_update_driver_data():
    return {
        'first_name': 'Partial',
        'last_name': 'Update',
    }


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db()
def test_get_driver_list_as_anonymous_user(client):
    url = reverse('driver-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN),
        ('driver_1', 'password123', status.HTTP_200_OK),
        ('manager', 'password123', status.HTTP_200_OK),
        ('admin', 'password123', status.HTTP_200_OK),
    ]
)
def test_get_driver_list_as_authenticated_user(
        client, username, password, expected_status):
    login = client.login(username=username, password=password)
    url = reverse('driver-list')
    response = client.get(url)
    assert login
    assert response.status_code == expected_status


@pytest.mark.django_db()
def test_create_driver_as_anonymous_user(client, driver_data):
    url = reverse('driver-list')
    response = client.post(url, driver_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert User.objects.filter(groups__name='Driver').count() == 2


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status, expected_count",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('driver_1', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('manager', 'password123', status.HTTP_201_CREATED, 3),
        ('admin', 'password123', status.HTTP_201_CREATED, 3),
    ]
)
def test_create_driver_as_authenticated_user(
        client, driver_data, username,
        password, expected_status, expected_count):
    login = client.login(username=username, password=password)
    url = reverse('driver-list')
    response = client.post(url, driver_data, format='json')
    assert login
    assert response.status_code == expected_status
    assert User.objects.filter(groups__name='Driver').count() == expected_count


@pytest.mark.django_db()
def test_retrieve_driver_as_anonymous_user(client):
    url = reverse('driver-detail', kwargs={'pk': 5})
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN),
        ('driver_1', 'password123', status.HTTP_200_OK),
        ('driver_2', 'password123', status.HTTP_403_FORBIDDEN),
        ('manager', 'password123', status.HTTP_200_OK),
        ('admin', 'password123', status.HTTP_200_OK),
    ]
)
def test_retrieve_driver_as_authenticated_user(
        client, username, password, expected_status):
    login = client.login(username=username, password=password)
    url = reverse('driver-detail', kwargs={'pk': 5})
    response = client.get(url)
    assert login
    assert response.status_code == expected_status


@pytest.mark.django_db()
def test_update_driver_as_anonymous_user(client, update_driver_data):
    url = reverse('driver-detail', kwargs={'pk': 5})
    response = client.put(url, update_driver_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('passenger_1', 'password123'),
        ('driver_2', 'password123'),
    ]
)
def test_update_driver_as_authenticated_user_without_permissions(
        client, update_driver_data, username, password):
    login = client.login(username=username, password=password)
    driver_1 = User.objects.get(username='driver_1')
    url = reverse('driver-detail', kwargs={'pk': driver_1.id})
    response = client.put(url, update_driver_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('driver_1', 'password123'),
        ('admin', 'password123'),
        ('manager', 'password123'),
    ]
)
def test_update_driver_as_authenticated_user_with_permissions(
        client, update_driver_data, username, password):
    login = client.login(username=username, password=password)
    driver_1 = User.objects.get(username='driver_1')
    url = reverse('driver-detail', kwargs={'pk': driver_1.id})
    response = client.put(url, update_driver_data, format='json')
    driver_1.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert driver_1.username == 'update_driver'
    assert driver_1.first_name == 'Update'
    assert driver_1.last_name == 'Driver'
    assert driver_1.email == 'update@test.cl'


@pytest.mark.django_db()
def test_partial_update_driver_as_anonymous_user(
        client, partial_update_driver_data):
    url = reverse('driver-detail', kwargs={'pk': 5})
    response = client.patch(url, partial_update_driver_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('passenger_2', 'password123'),
        ('driver_2', 'password123'),
    ]
)
def test_partial_update_driver_as_authenticated_user_without_permissions(
        client, partial_update_driver_data, username, password):
    login = client.login(username=username, password=password)
    driver_1 = User.objects.get(username='driver_1')
    url = reverse('driver-detail', kwargs={'pk': driver_1.id})
    response = client.patch(url, partial_update_driver_data, format='json')
    assert login
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password",
    [
        ('driver_1', 'password123'),
        ('admin', 'password123'),
        ('manager', 'password123'),
    ]
)
def test_partial_update_driver_as_authenticated_user_with_permissions(
        client, partial_update_driver_data, username, password):
    login = client.login(username=username, password=password)
    driver_1 = User.objects.get(username='driver_1')
    url = reverse('driver-detail', kwargs={'pk': driver_1.id})
    response = client.patch(url, partial_update_driver_data, format='json')
    driver_1.refresh_from_db()
    assert login
    assert response.status_code == status.HTTP_200_OK
    assert driver_1.username == 'driver_1'
    assert driver_1.first_name == 'Partial'
    assert driver_1.last_name == 'Update'
    assert driver_1.email == 'driver_1@test.cl'


@pytest.mark.django_db()
def test_destroy_driver_as_anonymous_user(client):
    url = reverse('driver-detail', kwargs={'pk': 5})
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert User.objects.filter(groups__name='Driver').count() == 2


@pytest.mark.django_db()
@pytest.mark.parametrize(
    "username, password, expected_status, expected_count",
    [
        ('passenger_1', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('driver_1', 'password123', status.HTTP_204_NO_CONTENT, 1),
        ('driver_2', 'password123', status.HTTP_403_FORBIDDEN, 2),
        ('manager', 'password123', status.HTTP_204_NO_CONTENT, 1),
        ('admin', 'password123', status.HTTP_204_NO_CONTENT, 1),
    ]
)
def test_destroy_driver_as_authenticated_user(
        client, username, password, expected_status, expected_count):
    login = client.login(username=username, password=password)
    driver_1 = User.objects.get(username='driver_1')
    url = reverse('driver-detail', kwargs={'pk': driver_1.id})
    response = client.delete(url, format='json')
    assert login
    assert response.status_code == expected_status
    assert (
        User.objects.filter(groups__name='Driver').count() == expected_count
        )
