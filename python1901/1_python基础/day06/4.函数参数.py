#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
参数列表：若函数在运算的过程中，会涉及到一些未知量，那么我们可以
将这些未知量，设置为参数。
传参的过程：
形参【形式参数】：定义在函数的参数列表中的，用于接收参数值
实参【实际参数】：函数调用的过程中，传递的参数,作用：给形参赋值的
'''

def hello(n,con):
    for x in range(n):
        print(con)

num = 5
str1 = "good"
hello(num,str1)



