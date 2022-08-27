from rest_framework import permissions


# custom class --> https://www.django-rest-framework.org/api-guide/permissions/#isauthenticatedorreadonly


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)