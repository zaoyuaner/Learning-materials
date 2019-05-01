#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
filter(func,iterable)
过滤函数：将可迭代对象中的元素依次作用于func，根据func返回的True还是
False决定是否保留该元素,当结果为True保留该元素，当结果False，去除此元素
返回的结果是一个迭代器。
'''
list1 = [1,2,3,4,5,55,67,878]
'''
需求：去除列表中的偶数。
'''
def func(list1):
    l = []
    for x in list1:
        if x%2 != 0:
            l.append(x)
    return l

print(func(list1))

print([x for x in list1 if x%2!=0])

print(list(filter(lambda x:True if x%2 !=0 else False ,list1)))
'''
需求；将爱好为“无”的数据剔除掉

data= [["lili",18,"美食"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]
，
'''
data= [["lili",18,"美食"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]

def func2(l1):
    if l1[-1]=="无":
        return False
    else:
        return True
print(list(filter(func2,data)))
print(list(filter(lambda l: False if l[-1] == "无" else True,data)))