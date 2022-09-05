from usersapp.models import Users
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('is_superuser', 'is_staff')


class UserCastomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email')

