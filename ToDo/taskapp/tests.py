from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase, force_authenticate
from mixer.backend.django import mixer

from usersapp.models import Users
from .models import Tasks, Project
from .views import ProjectModelViewSet


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response, 2)


class TestProjects(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/tasks/'
        self.users_dict = {'username': 'wow', 'first_name': 'wow', 'last_name': 'wow', 'email': 'wow@wow.ru'}
        self.users_dict_fake = {'username': 'iriri', 'first_name': 'Ирина', 'last_name': 'Сидорова',
                                'email': 'iriri@iriri.ru'}

        self.format = 'json'
        self.login = 'adkjhm'
        self.password = 'adkjhbm'
        self.admin = Users.objects.create_superuser(self.login, 'jgcv@admin.ru', self.password)
        self.users = Users.objects.create(**self.users_dict)
        self.tasks_dict = {'text': 'Постройка из цельного бруса',
                             'date_create': '2022-08-24T06:41:40.458832Z', 'user': self.users}
        self.tasks_dict_fake = {'text': 'Постройка',
                             'date_create': '2022-09-04T06:41:40.458832Z', 'user': self.users_dict_fake}
        self.tasks = Tasks.objects.create(**self.tasks_dict)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(f'{self.url}{self.tasks.id}/', self.tasks_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.tasks.refresh_from_db()
        self.assertEqual(self.tasks.text, self.tasks_dict_fake.get('text'))
        self.client.logout()

    def test_mixer(self):
        bio = mixer.blend(Tasks, text='DEVELOPER')
        self.client.force_authenticate(user=self.admin)

        response = self.client.put(f'{self.url}{bio.id}/',
                                   self.tasks_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bio.refresh_from_db()
        self.assertEqual(bio.text,
                         self.tasks_dict_fake.get('text'))
        self.assertEqual(bio.author.id,
                         self.tasks_dict_fake.get('user'))
        self.client.logout()

    def tearDown(self) -> None:
        pass
