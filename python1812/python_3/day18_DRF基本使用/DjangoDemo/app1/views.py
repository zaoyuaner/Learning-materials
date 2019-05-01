from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from app1.models import Wheel


# FBV
def wheels(request):

    wheel_list = Wheel.objects.all()

    wheel_arr = []
    for wheel in wheel_list:
        dir = {}
        dir['id'] = wheel.id
        dir['name'] = wheel.name
        dir['img'] = wheel.img
        wheel_arr.append(dir)

    response_dir = {
        'msg': '轮播图数据获取成功',
        'status': 200,
        'data': wheel_arr
    }

    return JsonResponse(response_dir)


# CBV
class HelloView(View):
    def get(self, request):
        return HttpResponse('[get]hello view')

    def post(self, request):
        return HttpResponse('[post]hello view')

