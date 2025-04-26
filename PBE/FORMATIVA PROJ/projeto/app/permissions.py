from rest_framework.permissions import BasePermission


class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Gestor').exists()

class IsProfessorOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Professor').exists() and obj.professorResponsavel == request.user
