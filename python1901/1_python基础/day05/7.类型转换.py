#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
list1 = [1,2,3,4]
tuple1 = (1,2,3,4)
dict1 = {"1":1,"2":2,"3":3,"4":4}
set1 = {1,2,3,4}

# tuple、dict、set--》list 【dict只转了key】
# print(list(tuple1))
# print(list(dict1))
# print(list(set1))

#list、dict、set--》tuple 【dict只转了key】
# print(tuple(list1))
# print(tuple(dict1))
# print(tuple(set1))

#list、dict、tuple--》set 【dict只转了key】
# print(set(list1))
# print(set(tuple1))
# print(set(dict1))


# list、tuple、set直接转为字典是无法转的。
# print(dict(list1))
# print(dict(tuple1))
# print(dict(set1))

# list2 = ["hello","good","nice"]
# zip1 = dict(zip(list1,list2))
# print(zip1)


#使用一行代码
# dict2 = {1:"aa",2:"bb"} #---> {"aa":1,"bb":2}
#
# print(dict(zip(dict2.values(),dict2.keys())))


dict2 = {1:"aa",2:"bb"}
print(dict2.values())
print(type(dict2.values()))
# print(dict(zip(dict2.values(),dict2.keys())))

# list2 = ["good","nice","great"]
# print(type(zip(list1,list2)))
# print(type(list1))

