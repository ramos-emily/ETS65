from django.urls import path
from .views import (
    SensorListCreateAPIView,
    SensorDetailAPIView,
    HistoricoListCreateAPIView,
    HistoricoDetailAPIView,
    AmbientesListCreateAPIView,
    AmbientesDetailAPIView,
    RegisterAPIView,
    exportar_sensores_excel
)

urlpatterns = [
    path('sensores/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorDetailAPIView.as_view(), name='sensor-detail'),
    path('historicos/', HistoricoListCreateAPIView.as_view(), name='historico-list-create'),
    path('historicos/<int:pk>/', HistoricoDetailAPIView.as_view(), name='historico-detail'),
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('ambientes/', AmbientesListCreateAPIView.as_view(), name='ambientes-list-create'),
    path('ambientes/<int:pk>/', AmbientesDetailAPIView.as_view(), name='ambientes-detail'),
    path('exportar-sensores/', exportar_sensores_excel, name='exportar-sensores'),
]