from django.contrib.auth.models import User
from rest_framework import serializers

# 用户数据序列化
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')