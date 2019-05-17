from django.db import models

class User(models.Model):
    u_name = models.CharField(max_length=100, unique=True)
    u_password = models.CharField(max_length=256)



class Movie(models.Model):
    m_name = models.CharField(max_length=100)
    m_price = models.IntegerField()
