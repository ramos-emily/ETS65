from rest_framework.permissions import BasePermission


class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Gestor').exists()


class IsProfessorOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
