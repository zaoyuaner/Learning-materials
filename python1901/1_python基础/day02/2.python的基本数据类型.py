#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
python的基本数据类型：
1.number类型
a、整数(int) 包含正整数负整数 比如：100，-10
b、浮点数(float)【小数】比如：12.345
c、复数  例如：complex(a,b)
2.string类型
字符串：使用双引号或者单引号括起来的任意字符，我们就称他为字符串
3.bool类型
在python中，有True和False表示bool类型。
4.None类型
None是python中一个特殊类型的值，表示一个空值。
与0并不相同。
5.list类型
本质：一个有序的集合。

6.tuple类型
本质：一个有序的集合，一旦初始化就不能更改。
当tuple中只有一个元素的时候，我们需要在这个元素后面添加一个
逗号，用来消除歧义
例如：tuple1 = (1,)

7.dict类型
在其他语言中也称为map集合，在python中我们称之为字典。
存储数据的时候以键值对的方式来进行存储key-value
例如：dict1={"lili":18,"xiaoming":20}
语法：{key1:value1,key2:value2,...}

8.set类型
set是一个无序的集合。
set集合中只存储dict中的key值。
1.set集合中的值不重复【去重功能】
2.set集合中的值不可变【在set集合中不会出现list、dict、set】
'''

# set1 = {"lili","xiaoming"}
# print(set1)
# set2 = {19,20,18,20}
# print(set2)
dict1={"lili":18,"xiaoming":20}
print(type(dict1))
tuple1 = (1,2,3)
tuple2 = (1,)
print(type(tuple2))
print(tuple1)
print(type(tuple1))

list1 = [1,2,3,4,"hello",True,[1,2,3]]
print(list1)
print(type(list1))

num = None
print(None==0)
print(2>3)
# int可以将浮点数或者字符串转为整数
# age = int(input('请输入您的年纪：'))
# print(age)
# print(type(age))

# “hello”
print('"hello"')
# I'm ok

print("I'm ok")

# "I'm ok"
print('"I\'m ok"')

# a = 10
# print(a)
# print(type(a))
# a = 10.01
# print(a)
# print(type(a))
# a = "hello"
# print(a)
# print(type(a))