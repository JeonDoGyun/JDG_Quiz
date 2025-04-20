from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.user import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("추가 정보", {"fields": ("role",)}),
    )
    list_display = BaseUserAdmin.list_display + ("role",)
