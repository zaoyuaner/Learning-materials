import uuid
from django.core.cache import cache
from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from app2.authentications import UserAuthentication
from app2.models import User, Movie
from app2.permissions import UserLoginPermissions
from app2.serializers import UserSerializer, MovieSerializer


class UserAPIView(generics.CreateAPIView):  # 登录/注册，post
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # CreateAPIView >> self.create(request, *args, **kwargs) >> 注册功能
    def post(self, request, *args, **kwargs):
        # 区分不同的操作(必须带入)
        # http://127.0.0.1:8001/app2/user/?action=register
        # http://127.0.0.1:8001/app2/user/?action=login
        action = request.query_params.get('action')

        if action == 'register':    # 注册
            return self.create(request, *args, **kwargs)
        elif action == 'login':     # 登录
            return self.do_login(request, *args, **kwargs)
        else:
            raise APIException(detail='请提供正确的动作(register/login)')



    def do_login(self, request, *args, **kwargs):
        # post 获取参数
        u_name = request.data.get('u_name')
        u_password = request.data.get('u_password')

        try:
            user = User.objects.get(u_name=u_name)
        except:
            raise APIException(detail='用户不存在')

        if user.u_password != u_password:
            raise APIException(detail='密码错误')

        # 状态保持
        token = uuid.uuid5(uuid.uuid4(), u_name).hex
        cache.set(token, user.id, timeout=60*60)

        # 返回数据
        response_data = {
            'msg': '登录成功',
            'status': 200,
            'u_name': user.u_name,
            'token': token  # 标识你是谁
        }

        return Response(response_data)



# 视图集 都需要认证通过后才能操作
# class MovieAPIView(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     authentication_classes = UserAuthentication,
#     permission_classes = UserLoginPermissions,



# 列表 》》 权限: 不需要  》》 路由: 不带参数
class MoviesAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# 单个 》》 权限: 不需要 》》 路由: 带参数
class MovieAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# 添加 》》 权限: 需要 》》 路由: 不带参数
class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = UserAuthentication,
    permission_classes = UserLoginPermissions,



