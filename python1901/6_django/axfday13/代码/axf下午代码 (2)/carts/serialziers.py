
from rest_framework import serializers

from carts.models import Cart
from goods.serializers import Goodserializer


class CartSerializer(serializers.ModelSerializer):

    c_goods = Goodserializer()

    class Meta:
        model = Cart
        fields = '__all__'
