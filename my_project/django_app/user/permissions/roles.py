from enum import Enum
from rest_framework.permissions import BasePermission


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == Role.ADMIN.value


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == Role.USER.value
