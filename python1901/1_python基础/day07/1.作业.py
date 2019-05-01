#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

'''
1.设计一个函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
若是返回True，否则返回False
'''
def func1(obj):
    if type(obj) in [str,list,tuple,dict,set]:
        if len(obj)>5:
            return True
        else:
            return False
    else:
        return None

# print(func1(1233))

'''
2.设计一个函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
【字符串中含有空格，列表与元组中含有空串】。若含有则返回True，否则返回False
”hello world“ [12,34,"",23]
'''

def func2(obj):
    if type(obj) == str:
        if " " in obj:
            return True
        else:
            return False
    elif type(obj) in [list,tuple]:
        if "" in obj:
            return True
        else:
            return False
    else:
        return None

# print(func2([1," ",2,3]))
# print(func2([1,"",2,3]))
# print(func2("helllo "))
# print(func2("helllo"))
# print(func2(12133))
'''
3.设计一个函数，从控制台输入一个整数，计算整数绝对值的阶乘，
n！=1 x 2 x … x n【写成函数】
'''

def absjiecheng(n):
    n = abs(n)
    ji = 1
    for i in range(1,n+1):
        ji *= i
    return ji

# print(absjiecheng(5))
# print(absjiecheng(-5))
'''

4.从控制台输入两个正数，求这两个正数的最大公约数，与最小公倍数
注意：最大公约数的公式：
m % n = r ，m = n  n = r  ，r == 0  输出m ，若不为0则继续循环
最小公倍数的公式：
最小公倍数 = 两个正数的乘积/最大公约数
'''

def func3(m,n):
    chengji = m*n
    while True:
        r = m%n
        m = n
        n = r
        if r==0:
            return m,chengji/m
        else:
            continue
# print(func3(6,3))
# print(func3(6,9))

'''
1.将音乐加入到歌词解析器
2、将歌词解析封装成函数
'''