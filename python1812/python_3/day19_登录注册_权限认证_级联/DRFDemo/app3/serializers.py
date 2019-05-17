from rest_framework import serializers

from app3.models import UserModel, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'u_name', 'u_password')


class AddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'a_addr')
