from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class PassengerViewSetTests(APITestCase):
    fixtures = [
        'users.json',
        'permissions.json',
        'groups.json',
        ]

    def test_get_passenger_list_as_anonymous_user(self):
        url = reverse('passenger-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_passenger_list_as_passenger_user(self):
        login = self.client.login(
            username='passenger_1',
            password='password123'
            )
        url = reverse('passenger-list')
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_passenger_list_as_driver_user(self):
        login = self.client.login(username='driver', password='password123')
        url = reverse('passenger-list')
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_passenger_list_as_manager_user(self):
        login = self.client.login(username='manager', password='password123')
        url = reverse('passenger-list')
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_passenger_list_as_admin_user(self):
        login = self.client.login(username='admin', password='password123')
        url = reverse('passenger-list')
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_passenger_as_anonymous_user(self):
        url = reverse('passenger-list')
        data = {
            'username': 'test_passenger',
            'first_name': 'Test',
            'last_name': 'Registration',
            'email': 'test@registration.cl',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 6)

    def test_create_passenger_as_passenger_user(self):
        login = self.client.login(
            username='passenger_1',
            password='password123'
            )
        url = reverse('passenger-list')
        data = {
            'username': 'test_passenger',
            'first_name': 'Test',
            'last_name': 'Registration',
            'email': 'test@registration.cl',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 5)

    def test_create_passenger_as_driver_user(self):
        login = self.client.login(username='driver', password='password123')
        url = reverse('passenger-list')
        data = {
            'username': 'test_passenger',
            'first_name': 'Test',
            'last_name': 'Registration',
            'email': 'test@registration.cl',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 5)

    def test_create_passenger_as_manager_user(self):
        login = self.client.login(username='manager', password='password123')
        url = reverse('passenger-list')
        data = {
            'username': 'test_passenger',
            'first_name': 'Test',
            'last_name': 'Registration',
            'email': 'test@registration.cl',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 5)

    def test_create_passenger_as_admin_user(self):
        login = self.client.login(username='admin', password='password123')
        url = reverse('passenger-list')
        data = {
            'username': 'test_passenger',
            'first_name': 'Test',
            'last_name': 'Registration',
            'email': 'test@registration.cl',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 6)

    def test_retrieve_passenger_as_anonymous_user(self):
        url = reverse('passenger-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_passenger_as_account_owner(self):
        login = self.client.login(
            username='passenger_1',
            password='password123'
            )
        url = reverse('passenger-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_passenger_as_another_passenger(self):
        login = self.client.login(
            username='passenger_2',
            password='password123'
            )
        url = reverse('passenger-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_passenger_as_driver_user(self):
        login = self.client.login(username='driver', password='password123')
        url = reverse('passenger-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_passenger_as_manager_user(self):
        login = self.client.login(username='manager', password='password123')
        url = reverse('passenger-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_passenger_as_admin_user(self):
        login = self.client.login(username='admin', password='password123')
        url = reverse('passenger-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertTrue(login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
