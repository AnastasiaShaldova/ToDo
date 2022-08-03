from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=160, unique=True)
