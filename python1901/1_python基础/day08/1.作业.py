#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

'''
1.需求：对注册函数，进行数据过滤处理
要求写一个装饰器：用户名长度6~8，由字母数字下划线组成，
密码6位，由0~9数字组成，
若不满足条件打印用户名或者密码不合法
'''
def outer(func):
    def inner(user,password):
        if len(user) in [6,7,8]:
            for x in user:
                if x>='0' and x<='9' or x>='a' and x<='z' or x>='A' and x<='Z' or x=="_":
                    pass
                else:
                    return print("用户名或者密码不合法")
            else:
                if len(password) == 6 and password.isdigit():
                    return func(user,password)
                else:
                    return print("用户名或者密码不合法")
        else:
            return print("用户名长度不合法")
    return inner

@outer
def register(user,password):
    print("您的用户名为%s，密码为%s，请牢记密码；"%(user,password))



register("adm1in","123344")
register("adm_in","123344")
register("adm_in","1233 4")
