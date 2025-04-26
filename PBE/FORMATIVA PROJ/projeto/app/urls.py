from django.urls import path
from .views import *

urlpatterns = [
    path("professores/", ProfessorListCreateAPIView.as_view(), name='professores'),
    path("professores/<int:pk>/", ProfessorDetailAPIView.as_view(), name='professor-detail'),
    path("disciplinas/", DisciplinaListCreateAPIView.as_view(), name='disciplinas'),
    path("disciplinas/<int:pk>/", DisciplinaDetailAPIView.as_view(), name='disciplina-detail'),
    path("reservas/", ReservaListCreateAPIView.as_view(), name='reservas'),
    path("reservas/<int:pk>/", ReservaDetailAPIView.as_view(), name='reserva-detail'),
]
