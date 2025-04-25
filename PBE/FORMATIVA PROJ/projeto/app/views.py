from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *


class ProfessorListView(ListView):
    model = Professor

class ProfessorCreateView(CreateView):
    model = Professor

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ProfessorDeleteView(DeleteView):
    model = Professor

class ProfessorUpdateView(UpdateView):
    model = Professor


# class PlanetaListCreateAPIView(ListCreateAPIView):
#     queryset = Planet.objects.all()
#     serializer_class = PlanetaSerializer
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [IsAuthenticated()]
#         return [isHumano]



# class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_fields = ['account', 'username']

