from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Pato
from .serializers import PatoSerializer
from rest_framework.pagination import PageNumberPagination

class PatoPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class PatoListCreateAPIView(ListCreateAPIView):
    queryset = Pato.objects.all()
    serializer_class = PatoSerializer
    pagination_class = PatoPaginacao

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__incontains=nome)
        return queryset
    