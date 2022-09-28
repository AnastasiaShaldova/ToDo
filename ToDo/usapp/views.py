from rest_framework import generics
from usersapp.models import Users
from .serializers import UserSerializers, UserCastomSerializers


class UserListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserCastomSerializers
        return UserSerializers
