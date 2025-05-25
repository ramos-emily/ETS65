from django.urls import path
from .views import (
    SensorListCreateAPIView,
    SensorDetailAPIView,
    HistoricoListCreateAPIView,
    HistoricoDetailAPIView,
    AmbientesListCreateAPIView,
    AmbientesDetailAPIView,
    RegisterAPIView,
    listar_ambientes,
    AmbientesSearchAPIView,
    exportar_sensores_excel
)

urlpatterns = [
    path('sensores/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorDetailAPIView.as_view(), name='sensor-detail'),
    path('historicos/', HistoricoListCreateAPIView.as_view(), name='historico-list-create'),
    path('historicos/<int:pk>/', HistoricoDetailAPIView.as_view(), name='historico-detail'),
    path('api/register/', RegisterAPIView.as_view(), name='register'),

    path('ambientes/', listar_ambientes),
    path('ambi', AmbientesListCreateAPIView.as_view()),
    path('ambi/<int:pk>', AmbientesDetailAPIView.as_view()),
    path('ambientes/search/', AmbientesSearchAPIView.as_view()),

    path('exportar-sensores/', exportar_sensores_excel, name='exportar-sensores'),
]