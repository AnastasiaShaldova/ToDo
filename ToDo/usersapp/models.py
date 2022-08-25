from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    email = models.EmailField(max_length=160, unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.username} | {self.first_name} | {self.last_name}'






