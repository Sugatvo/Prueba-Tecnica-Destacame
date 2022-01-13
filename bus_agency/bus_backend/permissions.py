from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the ticket.
        return obj.passenger == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser


class IsGroupUserOrReadOnly(permissions.BasePermission):
    group = None

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.groups.filter(name=self.group).exists()


class IsManager(IsGroupUserOrReadOnly):
    group = 'Manager'


class IsDriver(IsGroupUserOrReadOnly):
    group = 'Driver'


class IsPassenger(IsGroupUserOrReadOnly):
    group = 'Passenger'
