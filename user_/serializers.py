from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import CircularUser


class CircularUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CircularUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class CircularUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircularUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
