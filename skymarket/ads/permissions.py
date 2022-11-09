from rest_framework import permissions

from users.managers import UserRoles
from users.models import User


class OwnerOrStaffPermission(permissions.BasePermission):
    message = 'У вас нет прав на редактирование'

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.author or request.user.role in [UserRoles.ADMIN])
