from rest_framework import mixins, viewsets
from .models import Users
from .serializers import UsersModelSerializer


class UsersModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer



