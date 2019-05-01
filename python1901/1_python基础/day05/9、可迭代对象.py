#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
可以直接作用于for循环的对象，我们统称为可迭代对象
常见的可迭代对象：
1、list/dict/set/str/tuple
2.生成器/迭代器
在python中可以一边循环，一边计算的这种机制，我们称之为生成器。遍历的时候只能遍历一次
1,2,...,1000
'''
# list1 = [x for x in range(1,1001)]
# print(list1)
# g1 = (x for x in range(1,5))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(list(g1))

'''
迭代器：
不但能作用于for循环，还能被next函数调用，不断返回下一个值，直到出现StopIteration错误。
本质，内部复写了__next__,__iter__这个两个内置函数。
可迭代对象与迭代器的区别与联系：
迭代器一定是可迭代对象，可迭代对象不一定是迭代器。
'''

from collections import Iterator
from collections import Iterable


# print(isinstance([],Iterator))
# print(isinstance({},Iterator))
# print(isinstance((),Iterator))
# print(isinstance(range(10),Iterator))
# print(isinstance(g1,Iterator))


# print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance((),Iterable))
# print(isinstance(range(10),Iterable))
# print(isinstance(g1,Iterable))
# print(isinstance("111",Iterable))

'''
将可迭代对象转为迭代器
iter(iterable)
功能：将可迭代对象转为迭代器。 
'''
# g2 = iter([1,2,3])
# print(next(g2))


list1 = [1,2,34,5,6,7,5]
# list1.remove(5)
# print(list1.pop())
# print(list1)
for i in range(len(list1)):
    print(list1[i])

str1 = "you are good man"
table = str1.maketrans("you","123")
print(str1.translate(table))

str2 = "adah之前的"
print(str2.isalpha())