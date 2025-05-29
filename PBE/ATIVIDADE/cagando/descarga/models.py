from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    especie_escolhas = [
        ('E', 'Experimento'),
        ('H', 'Humano'),
        ('A', 'Alien')
    ]
    especie = models.CharField(max_length=2, choices=especie_escolhas, default='E')
    idade = models.PositiveIntegerField()        
    planeta = models.CharField(max_length=50)
    cor = models.CharField(max_length=15)

