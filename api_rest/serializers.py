from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#Devolver para o front só o email (exemplo)

class UserMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_email']

