#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
set集合：
与字典类似，只存储了字典中key，没有存储字典的value。
本质：无序且无重复的集合。
创建set集合：
set1 = {元素1,元素2,...,元素n}
set集合中元素特征：
1.不重复的
2.不可变的
set() 内置函数，去重功能，可以将其他类型数据转为set集合
'''
# set1 = {1,2,3}
# set2 = set((1,2,3))
# print(set2)
# dict1 = {}
# print(set1)
# print(dict1)
# print(type(set1))
# print(type(dict1))
# set3 = {(1,2,4,(1,2,3)),12,34}
# print(set3)

'''
添加元素
set1.add(ele)
ele必须是不可变类型

set1.update(iter)
iter必须是可迭代对象，不能是二维的list、dict
对象可以是str/range/一维的list、dict/set

删除元素
set1.remove(ele)
删除指定的元素，若不存在则报错。
'''

set4 = {1,2}
# set4.add([1,2,3,4])
# print(set4)
# set4.add(True)
# print(set4)

# set4.update([3])
# print(set4)

# set4.update(set3)
# print(set4)

# set4.remove("hello")
# print(set4)
#
# for x in set4:
#     print(x)

# for index,value in enumerate(set4):
#     print(index,value)

#
# set5 = {1,2,3,45,56,67}
# set6 = {1,2,3,78,89,90}
# print(set5 & set6)
# print(set5 | set6)
set4.add((1,2,3))
print(set4)