#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
内置模块：自己没有定义，也没有安装的模块
第三方模块：pygame，自己没有定义，需要安装的
'''
import functools

print(int("101010",base=2))
# print(int("101010",base=8))
# print(int("101010",base=16))
def int2(str1):
    return int(str1,base=2)

print(int2("101001"))

int3 = functools.partial(int,base=2)
print(int3("101010"))

def login(user,psd):
    if user == "admin" and psd =="123456":
        print("登陆成功")
        return True
    else:
        print("登陆失败")
        return False

'''
使用偏函数，设计函数功能将psd固定住，只判断用户名。
'''
login2 = functools.partial(login,psd="123456")
print(login2("12343"))
print(login2("admin"))

'''
设计一个加法的偏函数，使用add()的时候需要导入operator模块，
偏函数需要实现的功能是，求任意数与100相加的和。
'''
import operator

add2 = functools.partial(operator.add,100)
print(add2(10))
print(add2(-10))

