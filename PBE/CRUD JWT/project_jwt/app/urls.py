from django.urls import path
from . import views

urlpatterns = [
    path('criarUsuario/', view=views.create_user, name='create_user'),
    path('logar/', view=views.logar, name='logar'),
    path('fazAlgumaCoisa/', view=views.view_protegido, name="view_protegida"),
    path('listarUsuario/', views.listar_usuario, name='listar_usuario'),
    path('usuario/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('usuario/new/', views.criar_usuario, name='criar_usuario'),
    path('usuario/<int:pk>/edit/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuario/<int:pk>/delete/', views.deletar_usuario, name='deletar_usuario'),
]

