from django.urls import path
from .views import *

urlpatterns = [
    path("professores/", ProfessorListView.as_view()),
]
