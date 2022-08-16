from rest_framework.viewsets import ModelViewSet

from .models import Project, Tasks
from .serializers import ProjectHyperlinkedModelSerializer, TasksHyperlinkedModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class TasksModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksHyperlinkedModelSerializer



