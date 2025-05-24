from rest_framework import serializers
from .models import Sensor, Historico, Ambientes

class SensorSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Sensor
        fields = '__all__'
        
    def get_display_name(self, obj):
        return f"Contador de Pessoas\n#{obj.mac_address}"
        
class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ['id', 'sensor', 'ambiente', 'valor', 'timestamp', 'observacoes']

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = ['id', 'sig', 'descricao', 'ni', 'responsavel']