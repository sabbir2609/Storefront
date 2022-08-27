from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer): 
    class Meta(BaseUserCreateSerializer.Meta): # lookup BaseUserCreateSerializer
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']