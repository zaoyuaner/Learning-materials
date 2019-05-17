from rest_framework import serializers

from app2.models import User, Movie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'u_name', 'u_password')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'm_name', 'm_price')
