from rest_framework.permissions import BasePermission
from app2.models import User


class UserLoginPermissions(BasePermission):
    # True有权限、False没权限
    def has_permission(self, request, view):
        # 假如认证通过， 会自动将user 赋值到 request.user
        return bool(request.user and isinstance(request.user, User))
