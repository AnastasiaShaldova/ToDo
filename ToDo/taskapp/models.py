from django.db import models

from usersapp.models import Users


class Project(models.Model):
    title = models.CharField(max_length=60)
    link_to_repository = models.URLField(help_text='Project url', blank=True)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return self.title


class Tasks(models.Model):
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)






