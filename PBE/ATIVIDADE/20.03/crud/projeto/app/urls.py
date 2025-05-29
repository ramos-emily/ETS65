from django.urls import path
from . import views

urlpatterns = [
    path('eventos/<int:pk>/', views.detalhe_evento),
    path('eventos/', views.listar_eventos),
    path('eventos/criar/', views.criar_evento),
    path('evento/alterar/<int:pk>', views.alterar_evento),
    path('evento/apagar/<int:pk>', views.deletar_informacoes),
]

