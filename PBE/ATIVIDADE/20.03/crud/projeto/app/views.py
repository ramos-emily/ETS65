from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def detalhe_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'Evento não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def listar_eventos(request):
    eventos = Evento.objects.all()
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def alterar_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'Evento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_informacoes(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    evento.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

