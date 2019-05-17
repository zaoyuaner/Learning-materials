import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from rest_framework import serializers

from user.models import AXFUser
from utils import errors


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AXFUser
        fields = '__all__'

class UserRegisterSerializers(serializers.Serializer):
    # 注册序列化, 启到校验字段的作用
    u_username = serializers.CharField(required=True, max_length=10,
                                       min_length=3,
                                       error_messages={
                                           'required': '注册账号必填',
                                           'blank': '注册账号不能为空',
                                           'max_length': '注册账号不超过10字符',
                                           'min_length': '注册账号不少于3字符'
                                       })
    u_password = serializers.CharField(required=True, max_length=10,
                                       min_length=5,
                                       error_messages={
                                           'required': '注册密码必填',
                                           'blank': '注册密码不能为空',
                                           'max_length': '注册密码不超过10字符',
                                           'min_length': '注册密码不少于5字符'
                                       })

    u_password2 = serializers.CharField(required=True, max_length=10,
                                       min_length=5,
                                       error_messages={
                                           'required': '注册确认密码必填',
                                           'blank': '注册确密码不能为空',
                                           'max_length': '注册确认密码不超过10字符',
                                           'min_length': '注册确认密码不少于5字符'
                                       })

    u_email = serializers.EmailField(required=True,
                                     error_messages={
                                        'required': '注册邮箱必填',
                                        'blank': '注册邮箱不能为空',
                                        'invalid': '格式错误'
                                    })

    def validate(self, attrs):
        # 1. 注册账号是否存在
        username = attrs.get('u_username')
        user = AXFUser.objects.filter(u_username=username).first()
        if user:
            raise errors.ParamsException({'code': 1001, 'msg': '注册账号已存在，请更换账号'})
        # 2. 注册密码和确认密码是否一致
        pwd1 = attrs.get('u_password')
        pwd2 = attrs.get('u_password2')
        if pwd1 != pwd2:
            raise errors.ParamsException({'code': 1002, 'msg': '密码不一致，请确认密码是否一致'})
        # 3. 邮箱正则是否匹配（使用charField()时候，写正则匹配）
        # 如果以上校验有问题，则抛异常
        return attrs

    def register_user(self, validate_attr):
        # 注册账号
        username = validate_attr.get('u_username')
        password = make_password(validate_attr.get('u_password'))
        email = validate_attr.get('u_email')
        user = AXFUser.objects.create(u_username=username,
                                      u_password=password,
                                      u_email=email)
        return user


class UserLoginSerilizers(serializers.Serializer):

    u_username = serializers.CharField(required=True, max_length=10,
                                       min_length=3,
                                       error_messages={
                                           'required': '登录账号必填',
                                           'blank': '登录账号不能为空',
                                           'max_length': '登录账号不超过10字符',
                                           'min_length': '登录账号不少于3字符'
                                       })
    u_password = serializers.CharField(required=True, max_length=10,
                                       min_length=5,
                                       error_messages={
                                           'required': '登录密码必填',
                                           'blank': '登录密码不能为空',
                                           'max_length': '登录密码不超过10字符',
                                           'min_length': '登录密码不少于5字符'
                                       })

    def validate(self, attrs):
        # 1. 判断账号是否存在
        username = attrs.get('u_username')
        password = attrs.get('u_password')
        user = AXFUser.objects.filter(u_username=username).first()
        if not user:
            raise errors.ParamsException({'code': 1004, 'msg': '登录账号不存在，请更换账号'})
        # 2. 判断密码是否正确
        if not check_password(password, user.u_password):
            raise errors.ParamsException({'code': 1005, 'msg': '登录密码错误'})

        return attrs

    def login_user(self, validate_attr):
        # 登录，返回token参数给前端，且保存token参数到redis
        token = uuid.uuid4().hex
        username = validate_attr.get('u_username')
        user = AXFUser.objects.filter(u_username=username).first()
        # 后端使用redis进行保存数据
        cache.set(token, user.id, timeout=86400)

        return token
