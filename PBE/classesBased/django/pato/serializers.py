from rest_framework import serializers 
from .models import Pato, Dono
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class PatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pato
        fields = '__all__'
        read_only_fields = ['id', 'cagaTorrada']

class DonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dono
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get['username']
        password = attrs.get['password']
        if username and password:
            usuario = authenticate(request=self.context.get('request'), username=username, password=password)
            if not usuario:
                mensagem = "nao tem veir, sua credencial nao foi identificada"
                raise serializers.ValidationError(mensagem, code='authorization')
        
            if not usuario.is_active:
                mensagem = "desativou vei"
                raise serializers.ValidationError(mensagem, code='authorization')
            
            refresh = RefreshToken.for_user(usuario)

            attrs['usuario'] = usuario
            attrs['refresh'] = refresh
            attrs['access'] = str(refresh.access_token)

            return attrs
        else:
            mensagem = 'tem q colocar usuario E senha ne burro'
            raise serializers.ValidationError(mensagem, code='authorization')
