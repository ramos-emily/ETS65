from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAbs
# Register your models here.

class UserAbsAdmin(UserAdmin):
    list_display = ('username', 'escolaridade', 'idade', 'bio', 'animais', 'telefone', 'endereco', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('escolaridade', 'idade', 'bio', 'animais', 'telefone', 'endereco')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('escolaridade', 'idade', 'bio', 'animais', 'telefone', 'endereco')}),
    )

admin.site.register(UserAbs, UserAbsAdmin)