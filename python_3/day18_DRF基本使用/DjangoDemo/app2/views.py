from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from app2.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # 数据源
    queryset = User.objects.all()
    serializer_class = UserSerializer