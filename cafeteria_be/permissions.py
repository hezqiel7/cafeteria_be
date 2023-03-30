from rest_framework import permissions
    
class IsRecepcionista(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.get().name == 'recepcion'
    
class IsCocinero(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.get().name == 'cocina'
    
class IsRecepcionistaOrCocinero(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.user.groups.get().name
        return role == 'recepcion' or role == 'cocina'