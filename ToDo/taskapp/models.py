from django.db import models

from usersapp.models import Users


class Project(models.Model):
    title = models.CharField(max_length=60)
    link_to_repository = models.URLField
    users = models.OneToOneField(Users, on_delete=models.CASCADE)
    pass


class Tasks(models.Model):
    projects = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

