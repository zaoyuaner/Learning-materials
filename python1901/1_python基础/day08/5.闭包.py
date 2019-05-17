#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
闭包：在外函数中定义了一个内函数，内函数使用了外函数的临时变量
而外函数的返回值是内函数的引用【内函数的函数名】，这样构成了一个闭包。
装饰器是闭包,闭包不一定是装饰器。

闭包的特殊之处：
一般情况下，当函数执行结束，函数中所定义的临时变量都会销毁，但是
在闭包存在一种特殊的情况，外函数执行结束之后，发现自己的临时变量
在内函数中还需要使用，这时候外函数会将自己的临时变量绑定给内函数，
然后自己再结束

闭包的优点：
1.提高代码的复用性
2.减少函数名冲突，以及变量的定义
'''
def outer(func):
    def inner():
        pass
        return func()
    return inner


def lazy_func2(*args):
    def func2():
        res = 0
        for x in args:
            res += x
        return res
    return func2