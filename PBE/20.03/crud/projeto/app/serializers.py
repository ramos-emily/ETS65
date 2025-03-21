from rest_framework import serializers
from .models import Dados

class appSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class meta:
        model = Dados
        fields = ('')