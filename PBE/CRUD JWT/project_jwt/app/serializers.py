from rest_framework import serializers
from .models import UserAbs

class UserAbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAbs
        fields = '__all__'