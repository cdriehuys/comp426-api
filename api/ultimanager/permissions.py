from rest_framework import permissions


class IsGameManagerOrReadOnly(permissions.BasePermission):
    """
    Permission that only allows write operations on games if the
    requesting user manages the team that is tracking the game.
    """

    def has_object_permission(self, request, view, obj):
        """
        Only allow access to the view if the request method is read-only
        or the requesting user manages the game being accessed.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.team.user


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


class IsPlayerManagerOrReadOnly(permissions.BasePermission):
    """
    Permission that only allows write operations on players if the
    requesting user manages the team that the player is a part of.
    """

    def has_object_permission(self, request, view, obj):
        """
        Only allow access to the view if the request method is read-only
        or the requesting user manages the player being accessed.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.team.user


class IsPointManagerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.game.team.user
