#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
字符串为什么可以相加？
list为什么可以相加？
我们写的对象能不能相加？
'''
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age+other.age


'''
需求：重写字典，支持字典的相加，要求返回一个新的字典。
'''

class dictdemo(dict):
    def __add__(self, other):
        obj = {}
        for k,v in self.items():
            obj[k] = v

        for k2,v2 in other.items():
            obj[k2] = v2

        return dictdemo(obj)


dict1 =  dictdemo({"1":1,"2":2,"3":"hello"})
dict2 = dictdemo({"3":3,"4":4})
dict3 = dictdemo({"33":3,"44":4})
print(dict1+dict2+dict3)
# len(1233)
'''
重写int，可以使用len获取长度
'''
# per1 = Person("lili",18)
# per2 = Person("xiaoming",20)
# per3 = Person("xiaohong",19)
# print(per1+per2)

class Int(int):
    def __len__(self):
        res = 0
        for x in str(self):
            res += 1
        return res



int1 = Int(123456)
print(len(int1))





