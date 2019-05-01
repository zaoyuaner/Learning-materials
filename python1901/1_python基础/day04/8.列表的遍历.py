#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
list1 = [1,2,4,5,6,7,8,9,10]
'''
分别适用while循环与for循环遍历列表
'''
# for x in list1:
#     print(x)
#
# index = 0
# while index<len(list1):
#     print(list1[index])
#     index += 1
#
# for i in range(len(list1)):
#     print(list1[i])

'''
enumerate()枚举函数
'''
a,b = (1,2)

for index,value in enumerate(list1):
    print(index,value)
