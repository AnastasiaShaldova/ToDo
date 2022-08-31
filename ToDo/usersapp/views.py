from rest_framework import mixins, viewsets
from rest_framework.permissions import BasePermission

from .models import Users
from .serializers import UsersModelSerializer

#
# class SuperUserOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_staff


class UsersModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer
    # permission_classes = [SuperUserOnly]



