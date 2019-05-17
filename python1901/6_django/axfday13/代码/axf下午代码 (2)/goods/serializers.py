
from rest_framework import serializers

from goods.models import MainWheel, MainNav, MainShop, MainMustBuy, MainShow, FoodType, Goods


class MainWheelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainWheel
        fields = '__all__'


class MainNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainNav
        fields = '__all__'


class MainMustBuySerialzier(serializers.ModelSerializer):
    class Meta:
        model = MainMustBuy
        fields = '__all__'


class MainShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainShop
        fields = '__all__'


class MainShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainShow
        fields = '__all__'


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'


class Goodserializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'
