#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

# def func1(name,list1 = []):
#     list1.append(name)
#     return list1
#
# print(func1("lili"))
# print(func1("lili2"))

'''
值传递：
指的是不可变类型的参数的传递
str/number/bool/None/tuple
'''

'''
引用传递
指的是传递的可变类型，list/tuple/dict
'''

'''
原因：当实参给形参传递参数的时候，其实是一个赋值的过程，
若赋值对象是不可变类型的时候，正常的值传递的过程。
但是赋值对象是一个可变类型的时候，传递的是可变类型的数据地址，
当在函数中进行操作，与原本的变量操作的是同一块内存区域。
'''
'''
将冒泡排序封装一下，当我传递一个列表进去，将列表中的元素进行排序。
'''
def func2(name,age):
    #赋值拷贝
    # name = "小明"
    name.append("小明")
    print(name,id(name))
    print(age,id(age))

# name = "lili"
name2 = [1,2,3,4,4]
# print("name",id(name))
# print("name2",id(name2))
age = 18
# print(name,id(name))
# print(age,id(age))
func2(name2,age)
print(name2)


def maopao(list1):
    for i in range(1,len(list1)):
        for j in range(len(list1)-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]

numList = [1,23,445,56,12,34]
maopao(numList)
print(numList)
