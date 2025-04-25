from django.db import models
from django.contrib.auth.models import AbstractUser

class Planet(models.Model):
    nome_planeta = models.CharField(max_length=50)
    atmosfera = models.BooleanField()
    plantas = models.CharField(max_length=150)
    cor = models.CharField(max_length=10)
    tem_agua = models.BooleanField()
    habitavel = models.BooleanField()
    foto = models.ImageField(upload_to='images/', blank=True, null=True)


class UserProject(AbstractUser):
    especies_escolhas = [
        ('E','Experimentos'),
        ('H', 'Humano'),
        ('A', "Alien")
    ]

    especie = models.CharField(max_length=1, choices=especies_escolhas, default='E')
    idade = models.PositiveIntegerField(blank=True, null=True)
    planeta = models.ForeignKey(Planet, on_delete=models.CASCADE, blank=True, null=True)
    cor = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)

