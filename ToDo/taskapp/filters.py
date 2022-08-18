from django_filters import rest_framework as filters

from .models import Project, Tasks


class ProjectFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class ToDoFilterSet(filters.FilterSet):
    create = filters.DateFromToRangeFilter()
    project = filters.ModelChoiceFilter(queryset=Project.object.all())

    class Meta:
        model = Tasks
        fields = ['projects', 'date_create']


