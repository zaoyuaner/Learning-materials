#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
列表:
本质:就是一种有序的集合.
列表的定义:
列表名 = [元素1,元素2,...,元素n]
元素的取值可以任意类型.
列表中元素的访问:
list1[index]
index就是索引值/下标值  取值范围[0,len(list1))
index可以为负,当取值为负,代表倒数第几个元素.

列表中元素的更改
list1[index] = 值
功能:对我们指定的列表中元素进行重新赋值.
'''
list1 = [1,1.1,"1",True,[1,2,3]]
list2 = []
print(list1[0])
print(list1[-1])


list1[0] = "hello"
print(list1)

'''
list() 内置函数,可以将可迭代对象转为列表
'''
# print(list(range(10)))





