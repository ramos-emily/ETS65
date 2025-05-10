from django.db import models

class Sensor(models.Model):
    sensor_id = models.CharField(max_length=100, unique=True)
    mac_address = models.CharField(max_length=100, unique=True)
    unidade_med = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    def __str__(self):
        return self.sensor_id

class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='historicos', on_delete=models.CASCADE)
    ambiente = models.ForeignKey('Ambientes', related_name='historicos', on_delete=models.CASCADE) 
    observacoes = models.TextField() 

    def __str__(self):
        return f"Histórico do Sensor {self.sensor.sensor_id} em {self.ambiente.descricao}"


class Ambientes(models.Model):
    sig = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)
    ni = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao