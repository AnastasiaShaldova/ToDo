from mixer.backend.django import mixer
from django.core.management.base import BaseCommand

from taskapp.models import Project, Tasks


class Command(BaseCommand):
    help = 'Создание проекта и записок'

    def handle(self, *args, **options):
        for i in range(5):
            mixer.blend(Project)
            mixer.blend(Tasks)
        print('Выполнено')

