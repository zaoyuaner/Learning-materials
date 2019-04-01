from rest_framework import serializers
from app3.models import Book

# serializers.Serializer 原始序列化，手动序列化
# serializers.ModelSerializer 序列化模型(最常用)
# serializers.HyperlinkedModelSerializer 序列化模型，添加一个超链接
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'id')