from django.db import models

class Professor(models.Model):
    ni = models.CharField(max_length=9)
    Nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.PositiveIntegerField(blank=True, null=True)
    dataNascimento = models.DateField()
    dataContratacao = models.DateField()
    disciplinaAtribuida = models.ForeignKey('Disciplina', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ni

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    cargaHoraria = models.IntegerField()
    descricao = models.CharField(max_length=50)
    professorResponsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

class ReservaAmbiente(models.Model):
    dataInicio = models.IntegerField()
    dataTermino = models.IntegerField()
    periodo = models.CharField(max_length=50)
    salaReservada = models.CharField(max_length=50)
    professorResponsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)
    disciplinaAssociada = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.dataInicio

    