from django.urls import path
from usapp.views import UserListAPIView

app_name = 'usapp'

urlpatterns = [

    # path('api/<str:version>/users/', UserListAPIView.as_view()),
    path('', UserListAPIView.as_view()),

]

