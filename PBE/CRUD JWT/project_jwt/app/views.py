from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import UserAbsSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    endereco = request.data.get('endereco')
    idade= request.data.get('idade')
    telefone = request.data.get('telefone')
    bio = request.data.get('bio')
    animais = request.data.get('animais')
    escolaridade = request.data.get('escolaridade')

    if not username or not password or not endereco or not idade or not telefone:
        return Response({'ERRO' : 'Informações Insuficientes'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({"ERRO" : 'Username já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(endereco = endereco).exists():
        return Response({'Erro':'endereco Já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = UserAbs.objects.create_user(
        username = username,
        password = password,
        endereco = endereco,
        idade = idade,
        telefone = telefone,
        bio = bio,
        animais = animais,
        escolaridade = escolaridade,
    )
    return Response({'Criado' : f'Usuário {usuario} criado'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access' : str(refresh.access_token),
            'refresh' : str(refresh),
        }, status=status.HTTP_200_OK)

    else:
        return Response({'Erro' : 'Usuario ou senha inválido'}, status=status.HTTP_401_UNAUTHORIZED)
    
#listar
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuario(request):
    usuarios = UserAbs.objects.all()
    serializer = UserAbsSerializer(usuarios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#detalhes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalhes_usuario(request, pk):
    userAbs = get_object_or_404(UserAbs, pk=pk)
    serializer = UserAbsSerializer(userAbs)
    return Response(serializer.data, status=status.HTTP_200_OK)

#criar
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_usuario(request):
    serializer = UserAbsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#att
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar_usuario(request, pk):
    userAbs = get_object_or_404(UserAbs, pk=pk)
    serializer = UserAbsSerializer(userAbs, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deletar 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletar_usuario(request, pk):
    userAbs = get_object_or_404(UserAbs, pk=pk)
    userAbs.delete()
    return Response({'mensagem': 'Usuário deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

#seila
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegido(request):
    return Response({'mensagem': 'Olá DS14'}, status=status.HTTP_200_OK)