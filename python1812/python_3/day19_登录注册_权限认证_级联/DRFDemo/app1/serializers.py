from rest_framework import serializers

from app1.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('id', 'name', 'price', 'num')