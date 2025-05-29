from django.contrib import admin
from .models import Dono, Pato
from django.contrib.auth.admin import UserAdmin

class DonoAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'foto_perfil']

    fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {'fields': ('nome', 'foto_perfil', 'bio')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {'fields': ('nome', 'foto_perfil', 'bio')}),
    )

admin.site.register(Pato)
admin.site.register(Dono, DonoAdmin)