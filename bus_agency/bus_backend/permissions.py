from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the ticket.
        return obj.passenger == request.user


class IsAnonymousOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only unautenticathed users passenger registration
        # or superuser
        return request.user.is_anonymous or request.user.is_superuser


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()


class IsManagerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.groups.filter(name='Manager').exists()
            or request.user.is_superuser
        )


class IsManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed for a manager account
        return request.user.groups.filter(name='Manager').exists()


class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Driver').exists()


class IsPassenger(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Passenger').exists()
