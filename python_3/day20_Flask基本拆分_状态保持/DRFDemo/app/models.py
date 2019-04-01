from django.db import models

class Wheel(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 描述
    desc = models.CharField(max_length=100)
    # 详情页ID
    detailid = models.IntegerField()
