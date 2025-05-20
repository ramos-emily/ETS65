from django.db import models
import uuid

class Ambientes(models.Model):
    sig = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)
    ni = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Sensor(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    TIPO_SENSOR_CHOICES = [
        ('contador', 'Contador'),
        ('luminosidade', 'Luminosidade'),
        ('temperatura', 'Temperatura'),
        ('umidade', 'Umidade'),
    ]

    sensor_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    mac_address = models.CharField(max_length=100, unique=True)
    tipo_sensor = models.CharField(max_length=20, choices=TIPO_SENSOR_CHOICES, default='temperatura')
    unidade_med = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return f"{self.sensor_id} ({self.tipo_sensor})"

class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='historicos', on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, related_name='historicos', on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Histórico do Sensor {self.sensor.sensor_id} em {self.ambiente.descricao}"
