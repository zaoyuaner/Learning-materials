from rest_framework.permissions import BasePermission
from app3.models import UserModel


class UserLoginPermissions(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and isinstance(request.user, UserModel))