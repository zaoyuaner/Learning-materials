#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
没有名字的函数就叫匿名函数
定义匿名函数的使用lambda
匿名函数的定义：
lambda 参数列表: 表达式
好处：不用担心函数名冲突，结构简单，使用方便。
匿名函数的调用：
需要将匿名函数赋值给一个变量，调用的时候，我们通过调用这个变量来调用我们的函数
变量名(参数列表)
'''
func = lambda x,y: x if x>y else y
print(func(12,34))