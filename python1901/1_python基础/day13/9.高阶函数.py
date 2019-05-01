#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
map(func,iter)
功能：将iter中的每一个元素一一作用于func，并且将作用后的结果
作为一个迭代器返回。
func有且只能有一个参数。

'''

# def map2(func,iter1):
#     res = []
#     for x in iter1:
#         res.append(func(x))
#     return iter(res)

list1 = ["1","2","3","4","5"]
'''
需求：将list1转为[1,2,3,4,5]
'''

def func(list1):
    list2 = []
    for x in list1:
        list2.append(int(x))
    return list2


obj = map(int,list1)
print(next(obj))

list2 = [1,2,-3,4,-5,6]
'''
需求：

得到：
list3 = [1,2,3,4,5,6]
使用map函数来解决
list4 = [1,4,9,16,25,36]
'''
obj2 = map(abs,list2)
print(list(obj2))

obj3 = map(lambda x:x*x,list2)
print(list(obj3))


