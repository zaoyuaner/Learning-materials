#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
赋值拷贝,引用拷贝
list1 = [1,2,3]
list2 = list1

浅拷贝
list2 = list1.copy()
对于一维列表适用,开辟一块新的内存空间
若出现二维列表的时候,由于在一维列表中存储的是列表的地址,
所以当二维列表的时候,又是操作的同一块区域

深拷贝
import  copy
list4 = copy.deepcopy(list1)
深拷贝是一个完全内存拷贝,将list1中所有的元素全部拷贝了一份
所以不会出现同时操作同一块内存的情况.

'''
a = 10
b = a
print(a)
print(b)
print(id(a))
print(id(b))
a = 20
print(b)

list1 = [1,2,3,4,[1,1,1]]
# list2 = list1
# print(list1)
# print(list2)
# print(id(list1))
# print(id(list2))
# list1[0] = "hello"
# print(list2)
# print(list1)
# list2[-1] = "good"
# print(list1)
list3 = list1.copy()
print(list3)
print(list1)
print(id(list1))
print(id(list3))
list3[-1][-1] ="nice"
print(list1)
print(list3)

import  copy

list4 = copy.deepcopy(list1)
print(list4)
print(list1)
print(id(list1))
print(id(list4))
list1[-1][-1] = "good"
print(list1)
print(list4)