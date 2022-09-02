from rest_framework.relations import StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, Tasks


class ProjectHyperlinkedModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TasksHyperlinkedModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Tasks
        fields = '__all__'
