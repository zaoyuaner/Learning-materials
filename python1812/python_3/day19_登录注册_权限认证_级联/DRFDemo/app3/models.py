from django.db import models

# 用户
class UserModel(models.Model):
    u_name = models.CharField(max_length=100)
    u_password = models.CharField(max_length=100)

# 地址 (从表)
class Address(models.Model):
    a_addr = models.CharField(max_length=100)
    a_user = models.ForeignKey(UserModel, null=True, blank=True)
