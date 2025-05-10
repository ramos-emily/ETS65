from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Sensor, Ambientes, Historico
from .serializer import SensorSerializer, AmbientesSerializer, HistoricoSerializer
from .permissions import IsGestor, IsProfessorOwner


class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

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
