from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    cargo = request.data.get('cargo')
    email = request.data.get('email')
    telefone = request.data.get('telefone')

    if not username or not password or not email or not cargo:
        return Response ({'Erro': 'Informaçoes insuficientes'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({'Erro': 'Username ja existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email=email).exists():
        return Response({'Erro': 'Username ja existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = UserAbs.objects.create_user(
        username=username,
        password=password,
        email=email,
        cargo=cargo,
        telefone=telefone,
    )

    return Response({'Mensagem': f'Usuario {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    username = request.data.get
    password = request.data.get

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user()
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuario ou senha invalido'}, status=status.HTTP_401_UNAUTHORIZED)



    
