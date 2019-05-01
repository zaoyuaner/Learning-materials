#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

# print(10/0)
# print(ZeroDivisionError)
'''
自定义错误,定义一个类，定义的类要选好继承关系，
所有的错误都继承与BaseException。
只有我们需要的时候才自己定义错误，一般情况下，若python存在此错误
类型，我们无需自己定义，直接使用即可
'''


class FooException(ArithmeticError):
    pass


def fun(n):
    if n == 0:
        raise FooException()
    else:
        return abs(n)

# print(fun(0))
print(fun(-30))

