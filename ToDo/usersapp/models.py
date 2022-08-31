from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    email = models.EmailField(max_length=160, unique=True)









