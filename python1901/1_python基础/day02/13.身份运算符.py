#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
is:判断两个标识符是否引用同一个对象。
is not：判断两个标识符是否引用不同的对象。
注意：python解析器还有pycharm内部会有些缓存，影响我们计算的结果。

什么时候引用是同一个对象？
当使用=进行赋值的时候
例如：num1 = [1,2,3]
num2 = num1
此时，num2与num1引用的就是同一个对象。
'''

num1 = 10000000
num2 = 10000000
print(id(num1))
print(id(num2))
print(num1 is num2)
list1 = ["hello","good","nice"]
list2 = ["hello","good","nice"]
list3 = list1
print(id(list1))
print(id(list2))
print(id(list3))
print(list3 is list1)
print(list1 is list2)