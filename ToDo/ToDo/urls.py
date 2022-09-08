"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from taskapp.views import ProjectModelViewSet, TasksModelViewSet

from usersapp.views import UsersModelViewSet

router = DefaultRouter()
router.register('users', UsersModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('tasks', TasksModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='ToDo',
        default_version='v1',
        description='Documentations',
        contact=openapi.Contact(email='admin@admin.ru'),
        license=openapi.License(name='MIT LICENSE'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    # path('', include('usapp.urls')),
    path('api/user/v1', include('usapp.urls', namespace='v1')),
    path('api/user/v2', include('usapp.urls', namespace='v2')),

    # path('swagger<str:format>/', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),

    path('graphql/', GraphQLView.as_view(graphiql=True)),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
