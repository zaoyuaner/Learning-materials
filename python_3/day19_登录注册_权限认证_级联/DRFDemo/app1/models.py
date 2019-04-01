from django.db import models



class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    num = models.IntegerField()



