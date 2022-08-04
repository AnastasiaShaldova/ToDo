from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from usersapp.models import Users


class Command(BaseCommand):
    help = 'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых пользователей')
        parser.add_argument('-a', '--admin', action='store_true', help='Создание учетной записи администратора')

    def handle(self, *args, **options):
        total = options['total']
        admin = options['admin']

        for i in range(total):
            username = get_random_string(length=10)
            email = get_random_string(length=15)
            if admin:
                Users.objects.create_superuser(
                    username=username,
                    email=email,
                    password='123'
                )
            else:
                Users.objects.create_user(
                    username=username,
                    email=email,
                    password='123'
                )
