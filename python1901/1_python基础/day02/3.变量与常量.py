#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
变量：
定义：在程序的运行中会改变的量，我们称他为变量
作用：将不同的数据类型存储到内存中
变量的定义：
变量名 = 值
变量名【标识符】

常量：
定义：在程序的运行中不改变的量，我们称之为常量
作用：给变量赋值的。

type()  查看变量的数据类型
id()  查看变量的地址

删除变量
del 变量名
注意：变量一旦删除，则不能使用

变量的类型是由它的值来决定的。
'''
name,age = "lili",18
print("name=",name)
print("age=",age)

# 交叉赋值
name,age = age,name
# tuple1 = "lili",18
# print(tuple1)
# print(type(tuple1))
print("name=",name)
print("age=",age)

# print(type(name))
# print(id(name))
#
del name
print(name)
