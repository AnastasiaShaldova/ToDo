from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users


class EmployeeAdmin(UserAdmin):
    pass


admin.site.register(Users, EmployeeAdmin)
# Register your models here.
