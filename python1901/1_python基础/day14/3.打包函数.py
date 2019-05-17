#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
zip(iter1,iter2,iter3,...)
将iter1，iter2，...中的对应的元素，打包成元组，并且返回这些元组组成对象,
作为迭代器返回，迭代器的长度于最短的iter的长度相同。


zip(*zipobj)
功能：将打包好的zip对象进行解包处理。
'''
list1 = [1,2,3,4,5]
list2 = ["hello","good","nice","hehe","haha","heihei"]
zip1 = zip(list1,list2)
# print(list(zip1))
print(list(zip(*zip1)))

'''
将列表转为字典：
'''

def getdict(list1,list2):
    dict1 = {}
    n = 0
    if len(list1)>len(list2):
        n = len(list2)
    else:
        n = len(list1)

    for  i in range(n):
        dict1[list1[i]] = list2[i]
    return dict1

print(getdict(list1,list2))

print(dict(zip(list1,list2)))

dict2 = {1: 'hello', 2: 'good', 3: 'nice', 4: 'hehe', 5: 'haha'}
print(dict(zip(dict2.values(),dict2.keys())))