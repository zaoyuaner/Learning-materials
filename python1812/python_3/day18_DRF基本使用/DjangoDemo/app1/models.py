from django.db import models



class Wheel(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=256)

