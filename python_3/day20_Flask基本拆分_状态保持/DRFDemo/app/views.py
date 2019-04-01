from django.shortcuts import render
from rest_framework import generics

from app.models import Wheel
from app.serializers import WheelSerializer


class WheelAPIView(generics.ListCreateAPIView):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer

class WheelDetail(generics.UpdateAPIView):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer
