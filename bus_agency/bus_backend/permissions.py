from rest_framework import permissions


class PassengerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed for manager or admin users
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user.groups.filter(name='Manager').exists()
                or request.user.is_superuser
            )
        elif request.method == 'POST':
            # Create is allowed only for anonymous or admin users
            return request.user.is_anonymous or request.user.is_superuser
        elif request.method == 'PUT':
            if request.user.has_perm(f'bus_backend.change_user'):
                return True
        elif request.method == 'PATCH':
            if request.user.has_perm(f'bus_backend.change_user'):
                return True
        elif request.method == 'DELETE':
            if request.user.has_perm(f'bus_backend.delete_user'):
                return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Read and Write permissions are allowed only
        # for account owner or admin
        return obj == request.user or request.user.is_superuser


class DriverPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed for driver, manager or admin users
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user.groups.filter(name='Manager').exists()
                or request.user.groups.filter(name='Driver').exists()
                or request.user.is_superuser
            )
        elif request.method == 'POST':
            # Create is allowed only for manager or admin users
            return (
                request.user.groups.filter(name='Manager').exists()
                or request.user.is_superuser
            )
        elif request.method == 'PUT':
            if request.user.has_perm(f'bus_backend.change_user'):
                return True
        elif request.method == 'PATCH':
            if request.user.has_perm(f'bus_backend.change_user'):
                return True
        elif request.method == 'DELETE':
            if request.user.has_perm(f'bus_backend.delete_user'):
                return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Write permissions are allowed only for account owner or superuser
        return obj == request.user or request.user.is_superuser


class ModelPermissions(permissions.BasePermission):
    model = None

    def has_permission(self, request, view):
        # Read permissions are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            if request.user.has_perm(f'bus_backend.add_{self.model}'):
                return True
        elif request.method == 'PUT':
            if request.user.has_perm(f'bus_backend.change_{self.model}'):
                return True
        elif request.method == 'PATCH':
            if request.user.has_perm(f'bus_backend.change_{self.model}'):
                return True
        elif request.method == 'DELETE':
            if request.user.has_perm(f'bus_backend.delete_{self.model}'):
                return True
        else:
            return False


class StationPermissions(ModelPermissions):
    model = 'station'


class RoutePermissions(ModelPermissions):
    model = 'route'


class BusPermissions(ModelPermissions):
    model = 'bus'


class TripPermissions(ModelPermissions):
    model = 'trip'


class TicketPermissions(ModelPermissions):
    model = 'ticket'

    # Write permissions are allowed only for ticket owner or superuser
    def has_object_permission(self, request, view, obj):
        return obj.passenger == request.user or request.user.is_superuser
