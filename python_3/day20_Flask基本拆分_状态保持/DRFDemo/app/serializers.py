from rest_framework import serializers
from app.models import Wheel


class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = ('id', 'img', 'desc', 'detailid')