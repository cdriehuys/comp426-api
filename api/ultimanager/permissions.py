from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission that only allows write operations to be performed if the
    user owns the object that the permission is applied to.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to access the given object.
        """
        # Read-only methods are okay
        if request.method in permissions.SAFE_METHODS:
            return True

        # It's a write method, so the requesting user must be the
        # object's owner.
        return request.user == obj.user
