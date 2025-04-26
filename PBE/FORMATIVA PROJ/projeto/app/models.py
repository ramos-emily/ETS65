from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ni = models.CharField(max_length=9)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.PositiveIntegerField(blank=True, null=True)
    dataNascimento = models.DateField()
    dataContratacao = models.DateField()
    disciplinaAtribuida = models.ManyToManyField('Disciplina',blank=True)
# many é pra atribuir mais de uma coisa veir


    def __str__(self):
        return f'{self.nome} ({self.ni})'


class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    cargaHoraria = models.IntegerField()
    descricao = models.CharField(max_length=50)
    professorResponsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

class ReservaAmbiente(models.Model):
    dataInicio = models.DateField()
    dataTermino = models.DateField()
    periodo = models.CharField(max_length=50)
    salaReservada = models.CharField(max_length=50)
    professorResponsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)
    disciplinaAssociada = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Reserva {self.salaReservada} - {self.dataInicio}'

 