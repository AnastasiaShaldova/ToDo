from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, Tasks


class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TasksSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = '__all__'


class ProjectCastomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = 'title', 'users'


class TasksCastomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = 'text', 'date_create'
