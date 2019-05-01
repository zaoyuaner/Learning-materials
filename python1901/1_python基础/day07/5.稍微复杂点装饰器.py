#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
稍微复杂点的装饰器：
def outer(func):
    def inner(参数列表):
        #要添加的功能
        return func(参数列表)
    return inner

取决于被装饰的函数，若被装饰的函数存在参数，
使用复杂点的装饰器，若不存在，则使用简单的装饰器即可。
'''



'''
从控制台输入成绩，判断成绩是否及格
'''
def outer(f):
    def inner(score):
        if score>100 or score<0:
            return  "输入非法"
        else:
            return f(score)
    return inner


@outer
def func(score):
    if score>=60:
        return "及格"
    else:
        return "不及格"

print(func(120))
print(func(90))

def outer2(f):
    def inner(age):
        if age>=180 or age<0:
            return -1
        else:
            return f(age)
    return inner

'''
需求：给函数添加非法判断的功能,若输入非法返回-1，
age[0,180]
'''
@outer2
def getAge(age):
    return age+1


# print(getAge(-10))
# print(getAge(10))
# print(getAge(180))


'''
需求：对登陆函数添加过滤，user必须全部都字母，4~8位
psd必须全是数字，6位的。
'''
def outerLogin(func):
    def inner(user,psd):
        if user.isalpha() and len(user)>=4 and len(user)<=8 :
            if psd.isdigit() and len(psd)==6:
                return func(user,psd)
            else:
                print("密码非法")
                return None
        else:
            print("用户名非法")
            return None

    return inner

# 登陆
@outerLogin
def login(user,psd):
    if user == "admin" and psd =="123456":
        print("登陆成功")
        return True
    else:
        print("登陆失败")
        return False


print("*"*50)
print(login("hello","12344"))
print(login("hello","123443"))
print(login("admin","123456"))