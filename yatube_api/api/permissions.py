from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorReadOnly(BasePermission):
    def has_obj_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
