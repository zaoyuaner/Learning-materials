from django.shortcuts import render
from rest_framework import generics,viewsets
from app5.models import Student
from app5.serializers import StudentSerializer


# class StudentAPIView(generics.CreateAPIView, generics.ListAPIView):

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
