from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Sensor, Ambientes, Historico
from .serializers import SensorSerializer, AmbientesSerializer, HistoricoSerializer
from .permissions import IsGestor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
import pandas as pd
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

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

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not username or not email or not password:
            return Response({'error': 'Todos os campos são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
            
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Nome de usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)
            
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'success': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)

class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'sensor']
    search_fields = ['mac_address']

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