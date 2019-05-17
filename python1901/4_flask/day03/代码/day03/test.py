from functools import wraps


def login_required(func):
    @wraps(func)
    def check(*args, **kwargs):
        # 实现业务逻辑（登录校验）
        return func(*args, **kwargs)
    return check

@login_required
def f():
    return '1234567'

print(f)
