from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase, force_authenticate
from mixer.backend.django import mixer
from .models import Users
from .views import UsersModelViewSet


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/users/'
        self.users_dict = {'username': 'wow', 'first_name': 'wow', 'last_name': 'wow', 'email': 'wow@wow.ru'}
        self.users_dict_fake = {'username': 'iriri', 'first_name': 'Ирина', 'last_name': 'Сидорова',
                                  'email': 'iriri@iriri.ru'}
        self.format = 'json'
        self.login = 'adkjhm'
        self.password = 'adkjhbm'
        self.admin = Users.objects.create_superuser(self.login, 'jgcv@admin.ru', self.password)
        self.users = Users.objects.create(**self.users_dict)

    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        force_authenticate(request, self.admin)
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.users_dict, format=self.format)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.users_dict, format=self.format)
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_client_detail(self):
        client = APIClient()
        client.force_authenticate(self.admin)
        response = client.get(f'{self.url}{self.users.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_client_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.users.id}/', **self.users_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_client_update_admin(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.put(f'{self.url}{self.users.id}/', self.users_dict_fake, format=self.format)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.users.refresh_from_db()
        self.assertEqual(self.users.username, self.users_dict_fake.get('username'))
        self.assertEqual(self.users.first_name, self.users_dict_fake.get('first_name'))
        self.assertEqual(self.users.last_name, self.users_dict_fake.get('last_name'))
        self.assertEqual(self.users.email, self.users_dict_fake.get('email'))
        client.logout()

    def tearDown(self) -> None:
        pass
