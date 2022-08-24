from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilterSet, TaskFilterSet
from .models import Project, Tasks
from .serializers import ProjectHyperlinkedModelSerializer, TasksHyperlinkedModelSerializer


class ProjectLimitOffsetPagination(PageNumberPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilterSet

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class TasksLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TasksModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksHyperlinkedModelSerializer
    pagination_class = TasksLimitOffsetPagination
    filterset_class = TaskFilterSet

    def destroy(self, request, *args, **kwargs):
        try:
            tasks = self.get_object()
            tasks.is_active = True
            tasks.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)
