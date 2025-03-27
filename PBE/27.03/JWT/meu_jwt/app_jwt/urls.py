from django.urls import path
from . import views

urlpatterns = [
    path('criar/', view=views.create_user, name='create_user'),
    path('logar/', view=views.logar, name='logar'),
]
