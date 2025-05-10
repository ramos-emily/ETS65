from django.urls import path
from .views import (
    SensorListCreateAPIView,
    SensorDetailAPIView,
    HistoricoListCreateAPIView,
    HistoricoDetailAPIView,
    AmbientesListCreateAPIView,
    AmbientesDetailAPIView
)

urlpatterns = [
    path('sensores/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorDetailAPIView.as_view(), name='sensor-detail'), 
    path('historicos/', HistoricoListCreateAPIView.as_view(), name='historico-list-create'), 
    path('historicos/<int:pk>/', HistoricoDetailAPIView.as_view(), name='historico-detail'),  
    path('ambientes/', AmbientesListCreateAPIView.as_view(), name='ambientes-list-create'),  
    path('ambientes/<int:pk>/', AmbientesDetailAPIView.as_view(), name='ambientes-detail'),  
]
