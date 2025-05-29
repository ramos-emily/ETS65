from rest_framework.permissions import BasePermission

class isHumano(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.especie == 'H'
    

class isAlien(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.especie == 'A'
    
class isExperimento(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.especie == 'E'
    
class isHumanoOuMorador(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.especie == 'H':
            return True
        return obj.id == request.user.planeta.id