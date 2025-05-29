from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Professor, Disciplina, ReservaAmbiente
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaAmbienteSerializer
from .permissions import IsGestor, IsProfessorOwner
from rest_framework.permissions import IsAuthenticated

class ProfessorListCreateAPIView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

class ProfessorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get_permissions(self):
        return [IsGestor()]

class DisciplinaListCreateAPIView(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

class DisciplinaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        return [IsGestor()]

class ReservaListCreateAPIView(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

class ReservaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor() | IsProfessorOwner()]
    
