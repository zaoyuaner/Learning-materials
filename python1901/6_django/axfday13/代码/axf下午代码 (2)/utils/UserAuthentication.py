
from rest_framework.authentication import BaseAuthentication
from django.core.cache import cache

from user.models import AXFUser
from utils import errors


class UserAuth(BaseAuthentication):

    def authenticate(self, request):
        # 用户登录认证方法，该方法必须被重构，且返回结构必须为（user，token）

        # token = request.query_params.get('token')
        # if not token:
        #     token = request.data.get('token')
        # 三元运算符
        token = request.query_params.get('token') if request.query_params.get('token') else request.data.get('token')
        user_id = cache.get(token)
        if user_id:
            user = AXFUser.objects.filter(pk=user_id).first()
            return user, token
        res = {
            'code':1007,
            'msg': '用户认证失败，无法操作'
        }
        raise errors.ParamsException(res)

