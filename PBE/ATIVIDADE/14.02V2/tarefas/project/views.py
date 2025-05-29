from django.shortcuts import render
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all() #vou ter todas as tarefas do BD
    return render(request, 'project/templates.html', {'tarefas': tarefas})