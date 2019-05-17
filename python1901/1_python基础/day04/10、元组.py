#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
元组:本质也是一种有序的集合,与列表非常相似,使用()表示.
特点:一旦初始化则不能修改.
'''

'''
tuple() 内置函数,可以将其他类型的数据转为元组
元组的创建
元组名 = ()
t1 = 1,
t2 = (1,)
只有一个元素的时候为了消除歧义,要添加逗号.

元组元素的访问:
通过下标来进行访问的
tuple1[index]
index取值范围[0,len(tuple1))
index若为负,从倒数第一个开始取.

修改元组
元组是不可修改的,存储到元组中列表其实存储的是地址,这个地址是无法修改的
列表不修改地址,里面的元素也可以进行修改,通过修改列表中的元素进而达到
修改元组的目的.

元组的操作
tuple1 + tuple2
功能:将tuple1中元素与tuple2中元素进行重新组合返回一个新的元组

tuple1*n
功能:将tuple1中元素重复n次输出到一个新的元组中

元素 in tuple1
功能:判断元素是否存在tuple1中,若存在返回True,否则返回False

元组的截取
tuple1[start:end:step]

len(tuple1) 获取元组的长度

max(tuple1) 返回元组中最大值

min(tuple1) 返回元组中最小值

tuple(list) 可以列表转为元组

二维元组
tuple1 = (元组1,元组2,元组3,...,元组n)
访问:
tuple1[index1][index2]
index1:下标为index1的元组
index2:下标为index2的元素
'''
# tuple2 = (1,2,3)
# tuple3 = (4,5,6)
# print(tuple2+tuple3)
# list1 = [1,2,3,4]
# tuple1 = tuple(list1)
#
# print(tuple1)


# tuple2 = tuple2*4
# print(tuple2)

# tuple1 = (1,2,3,4,5,"hello",True,(1,2,3),{1,2,3},[1,2,3])
# print(tuple1[0])
# print(tuple1[-1])
#
# tuple1[-1][-1] = "nice"
# print(tuple1)
# del tuple1

# t1 = ()
#
# print(type(t1))
# print(t1)
#
# t2 = (1,)
# print(t2)
# t3 = 1,
# print(t3)
# t4 = 1,2
# print(t4)
# t5 = tuple()
# print(t5)
# print(type(t5))