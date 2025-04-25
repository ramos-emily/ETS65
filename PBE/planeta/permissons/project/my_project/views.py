from django.shortcuts import render
from .serializer import LoginSerializer, UserProjectSerializer, PlanetaSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView
from .models import UserProject, Planet
from .permissions import isHumano, isAlien, isExperimento
from .serializer import UserProjectSerializer
from rest_framework.permissions import IsAuthenticated

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserProjectListCreateAPIView(ListCreateAPIView):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer
    permission_classes = [isHumano]

class PlanetaListCreateAPIView(ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetaSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [isHumano]
