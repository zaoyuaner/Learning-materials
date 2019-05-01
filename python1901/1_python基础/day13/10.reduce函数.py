#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
from functools import reduce
import functools
import operator

'''
reduce(func,iter1)
参数一：被作用的函数【有且只有两个参数】
参数二：被作用的序列
功能:依次将序列中的元素作用于我们的函数，并且返回最终的结果
'''
'''
1+2+3+4...+100
'''
def func(n):
    res = 0
    for x in range(1,n+1):
        res += x
    return res

print(func(100))
print(reduce(operator.add,range(1,101)))

'''
求阶乘n！
'''
print(reduce(operator.mul,range(1,6)))
'''
现有一序列
返回结果"1234567"，使用一行代码实现。
'''
# list3 = [1,2,"3","4","5",6,7]
# print(reduce(lambda x,y:str(x)+str(y),list3))
# print(reduce(operator.add,map(str,list3)))
list1 = [1,2,3,4,5,6]
print(list1[3::-1])
print(list1[2::-2])


list2 = [1,2,3,4]
print(list2[::-2])
# a = 2 and 1
# print(a)
# b = True or False
# print(b)
# print(2*False)