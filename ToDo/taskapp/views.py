from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilterSet, TaskFilterSet
from .models import Project, Tasks
from .serializers import ProjectSerializers, TasksSerializers, ProjectCastomSerializers, TasksCastomSerializers


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilterSet

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return ProjectSerializers
        return ProjectCastomSerializers


class TasksLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TasksModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
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

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return TasksSerializers
        return TasksCastomSerializers
