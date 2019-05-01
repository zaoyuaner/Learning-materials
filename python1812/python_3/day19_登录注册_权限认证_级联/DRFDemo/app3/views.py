import uuid
from django.core.cache import cache
from django.shortcuts import render
from rest_framework import generics, exceptions, viewsets, status
from rest_framework.response import Response
from app3.authentications import UserAuth
from app3.models import UserModel, Address
from app3.permissions import UserLoginPermissions
from app3.serializers import UserSerializer, AddrSerializer


class UserAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        action = request.data.get('action')
        if action == 'register':
            return self.create(request, *args, **kwargs)
        elif action == 'login':
            return self.login(request, *args, **kwargs)
        else:
            raise exceptions.APIException(detail='请填写操作类型(login/register)')

    def login(self, request, *args, **kwargs):
        name = request.data.get('u_name')
        password = request.data.get('u_password')

        try:
            user = UserModel.objects.get(u_name=name)

            if user.u_password != password:
                raise exceptions.AuthenticationFailed

            # 状态保持
            token = uuid.uuid3(uuid.uuid4(), name).hex
            cache.set(token, user.id, timeout=60*60)

            response = {
                'msg': '登录成功',
                'status': 200,
                'token': token
            }

            return Response(response)

        except UserModel.DoesNotExist:
            raise exceptions.NotFound



class AddrAPIView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddrSerializer
    # 添加认证个权限，就能保证以下操作都是 登录(有用户信息)
    authentication_classes = UserAuth,
    permission_classes = UserLoginPermissions,

    # create 需要做关联处理 【原有基础上添加新的操作】
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # 获取 addr对象
        addrid = serializer.data.get('id')
        addr = Address.objects.get(pk=addrid)
        addr.a_user = request.user
        addr.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request, *args, **kwargs):
        # self.get_queryset()  >> 获取上面赋值的queryset【类型判断】
        # self.get_queryset() >> QuerySet类型
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = self.filter_queryset(self.get_queryset().filter(a_user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)