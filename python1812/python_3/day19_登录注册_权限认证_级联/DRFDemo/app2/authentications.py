from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from app2.models import User


class UserAuthentication(BaseAuthentication):
    # 重写
    def authenticate(self, request):
        try:
            # http://127.0.0.1:8000/app2/movie/?token=a58c6e6b90e65c61af9e3e81685957bf
            token = request.query_params.get('token')
            userid = cache.get(token)
            user = User.objects.get(pk=userid)

            # 注意返回值
            return (user, token)
        except Exception as e:
            # 没找到，认证不通过
            return None