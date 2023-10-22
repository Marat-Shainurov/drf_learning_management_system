from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    message = "You are not the object's owner!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsModerator(BasePermission):
    message = "You are not a moderator!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
