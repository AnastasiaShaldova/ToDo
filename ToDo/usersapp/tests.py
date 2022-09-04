from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase, force_authenticate
from mixer.backend.django import mixer
from .models import Users
from .views import UsersModelViewSet


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/users/'
        self.users = {'username': 'wow', 'first_name': 'wow', 'last_name': 'wow', 'email': 'wow@wow.ru'}
        self.users_dict_fake = {'username': 'iriri', 'first_name': 'Ирина', 'last_name': 'Сидорова',
                                  'email': 'iriri@iriri.ru'}
        self.format = 'json'
        self.login = 'adm'
        self.password = '123'
        self.admin = Users.objects.create_superuser(self.login, 'adm@adm.ru', self.password)

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
        request = factory.post(self.url, self.users, format=self.format)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.users, format=self.format)
        force_authenticate(request, self.admin)
        view = UsersModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tearDown(self) -> None:
        pass
