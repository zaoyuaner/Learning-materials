from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from app3.models import UserModel


class UserAuth(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.query_params.get('token')
            userid = cache.get(token)
            user = UserModel.objects.get(pk=userid)

            return (user, token)
        except:
            return None
