#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
函数能够作为返回值返回
在python中，函数不但能够作为参数还能够作为返回值，当作为参数的时候
我们成这个函数为回调函数，当这个函数作为返回值，我们称他为返回函数。
'''
import functools

int2 = functools.partial(int,base=2)
f = lambda x,y: x if x>y else y

def func():
    return "表达式"

def outer(func):
    def inner():
        pass
        return func()
    return inner

def func2(*args):
    res = 0
    for x in args:
        res += x
    return res

def lazy_func2(*args):
    def func2():
        res = 0
        for x in args:
            res += x
        return res
    return func2


print(lazy_func2(1,2,3,4,5)())