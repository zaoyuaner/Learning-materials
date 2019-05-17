
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.core.cache import cache

from user.models import AXFUser
from user.serializers import UserSerializer, UserRegisterSerializers, UserLoginSerilizers
from utils import errors


class UserView(viewsets.GenericViewSet,
               mixins.ListModelMixin):

    queryset = AXFUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        # 用于返回登录用户信息
        # 1. 先获取前端请求中传递的token
        token = request.query_params.get('token')
        # 2. 通过token从redis中取用户的id值
        user_id = cache.get(token)
        # 3. 序列化用户对象
        user = AXFUser.objects.filter(id=user_id).first()
        serializer = self.get_serializer(user)
        # TODO: 订单的代付款和待收货后面在做
        res = {
            # 当前登录系统用户的信息
            'user_info': serializer.data,
            # 订单未支付数量
            'orders_not_pay_num': 0,
            # 订单未发送数量
            'orders_not_send_num': 0
        }
        return Response(res)


    @list_route(methods=['POST'], serializer_class=UserRegisterSerializers)
    def register(self, request, *args, **kwargs):
        # /api/user/auth/register/  POST
        serializer = self.get_serializer(data=request.data)
        # serializer = UserRegisterSerializers(data=request.data)
        # 校验字段的必填，长度等信息，还校验账号不存在，且密码相等
        result = serializer.is_valid(raise_exception=False)
        if not result:
            raise errors.ParamsException({'code': 1003,
                                          'msg': '参数校验失败',
                                          'data': serializer.errors})
        # 保存用户信息
        user = serializer.register_user(serializer.data)
        # 返回结构 {’code‘: 200, 'msg': '请求成功', 'data': {’user_id‘: id值}}
        res = {
            'user_id': user.id
        }
        return Response(res)

    @list_route(methods=['POST'], serializer_class=UserLoginSerilizers)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if not result:
            raise errors.ParamsException({'code': 1006, 'msg': '登录参数有误'})
        # 登录用户
        token = serializer.login_user(serializer.data)
        # 登录返回结构: {'code': 200, 'msg': ''，'data': {token: token值}}
        res = {
            'token': token
        }
        return Response(res)

