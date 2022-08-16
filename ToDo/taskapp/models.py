from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from usersapp.models import Users


class Project(models.Model):
    title = models.CharField(max_length=60)
    link_to_repository = models.URLField(help_text='Project url', null=True, blank=True)
    users = models.ManyToManyField(Users)
    pass


class Tasks(models.Model):
    projects = models.ManyToManyField(Project)
    text = models.TextField(blank=True, null=True)
    date_create = models.DateField(editable=False)
    date_update = models.DateField(editable=False)
    is_active = models.BooleanField(default=False)



