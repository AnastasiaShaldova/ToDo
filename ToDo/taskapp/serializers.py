from rest_framework.serializers import ModelSerializer

from .models import Project, Tasks


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TasksModelSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
