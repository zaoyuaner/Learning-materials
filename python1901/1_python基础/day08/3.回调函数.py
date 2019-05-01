#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
回调函数：把函数当作参数，传递到另外一个函数中，当这个函数【在传递的函数中】
被调用的时候，我们称这个函数为回调函数。
'''
import functools

int2 = functools.partial(int,base=2)
# int2("111")
#
# def outer(func):
#     def inner():
#         pass
#         return func()
#     return inner


def wake_one(times):
    print("在%s点，拧大腿叫醒你"%times)


def wake_two(times):
    print("在%s点，以泼冷水的方式叫醒"%times)


def wake_server(func,times):
    return func(times)

wake_server(wake_one,"12")

#int  int(str1,base)



