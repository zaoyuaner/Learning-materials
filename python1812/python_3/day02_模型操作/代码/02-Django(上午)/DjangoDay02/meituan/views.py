import random

from django.http import HttpResponse
from django.shortcuts import render

from meituan.models import Student


def index(request):
    return HttpResponse('首页 | 美团')


def cart(request):
    return HttpResponse('购物车 | 美团')


def addstu(request):
    stu = Student()
    stu.s_name = str(random.randrange(1,10000)) + '-zyz'
    stu.s_score = random.randrange(1,100)
    stu.s_weight = 75.00000022211
    stu.s_height = 180.33333333
    stu.s_detail = 'hello world!'

    # 数据存储
    stu.save()

    return HttpResponse('添加学生成功:' + stu.s_name)


def changestu(request):
    stu = Student.objects.get(pk=1)
    stu.s_name = str(random.randrange(1,10000)) + '-atom'
    stu.save()

    return HttpResponse('更新学生信息')