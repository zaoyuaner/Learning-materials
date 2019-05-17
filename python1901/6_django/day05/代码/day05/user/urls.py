from django.contrib.auth.decorators import login_required
from django.urls import path

from user.views import register, login, logout, index, \
    my_register, my_login, my_index

urlpatterns = [
    # 使用django自带的User模型实现登录注册注销
    path('register/', register),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', login_required(index), name='index'),
    # 自定义User模型，并实现登录注册注销（采用cookie+token的形式）
    path('my_register/', my_register),
    path('my_login/', my_login, name='my_login'),
    path('my_index/', my_index, name='my_index'),

]