from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import UserProject, Planet

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['userProject'] = {
            'nome': self.user.username,
            'planeta': self.user.planeta,
            'especie': self.user.especie
        }
class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = '__all__'

class PlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'