
# 外层函数嵌套内层函数
# 外层函数返回内层函数
# 内层函数调用外层函数的参数
from functools import wraps

from flask import session, render_template


def login_required(func):
    @wraps(func)
    def check(*args, **kwargs):
        try:
            # 登录情况
            # func()为被logi_required装饰的函数
            username = session['username']
            return func(*args, **kwargs)
        except:
            # 没登录情况
            return render_template('login.html')
    return check
