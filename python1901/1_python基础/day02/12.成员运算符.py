#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
成员运算符：
in： 判断元素是否存在于序列中，若存在则返回True，若不存在，则返回False
not in：判断元素是否不存在于序列中，若不存在则返回True，若存在，则返回False
'''
a = 10
list1 = [1,2,3,4,5,10]
tuple1 = (1,2,3,4,5)
dict1 = {"hello":10,"good":20,10:"hello"}
set1 ={'10',20,30}
print(a in list1)
print(a in tuple1)
print(a in dict1)
print(a in set1)
