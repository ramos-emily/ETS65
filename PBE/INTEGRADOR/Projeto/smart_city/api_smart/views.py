from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Sensor, Ambientes, Historico
from .serializers import SensorSerializer, AmbientesSerializer, HistoricoSerializer
from .permissions import IsGestor, IsProfessorOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import pandas as pd
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exportar_sensores_excel(request):
    sensores = Sensor.objects.all().values()
    df = pd.DataFrame(list(sensores))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=sensores.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sensores')

    return response

class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'sensor_id']
    search_fields = ['sensor_id']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

class SensorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_permissions(self):
        return [IsGestor()] 


class AmbientesListCreateAPIView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  
        return [IsGestor()]  

class AmbientesDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer

    def get_permissions(self):
        return [IsGestor()] 


class HistoricoListCreateAPIView(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

class HistoricoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer

    def get_permissions(self):
        return [IsGestor()] 
