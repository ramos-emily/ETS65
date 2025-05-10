from rest_framework import serializers
from .models import Sensor, Historico, Ambientes

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_id', 'mac_address', 'unidade_med', 'valor', 'latitude', 'longitude']

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ['id', 'sensor', 'ambientes', 'observacoes']

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = ['id', 'sig', 'descricao', 'ni', 'responsavel']
        

        
