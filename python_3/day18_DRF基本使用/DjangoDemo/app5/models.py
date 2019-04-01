from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    score = models.IntegerField()
