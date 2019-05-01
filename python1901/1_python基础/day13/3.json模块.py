#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import json

# dict1 = {"name":"lili","age":18}
# dict2 = {"name":"lili","age":18,"sex":True,"score":None}
#

# res = json.dumps(dict1)
# print(res)
# print(type(res))
# print(str(dict1))

# print(json.dumps(dict2))

# with open("demo.txt","w") as f:
#     f.write(json.dumps(dict2))

# with open("demo.txt","r") as f2:
#     res = f2.read().strip()
#     if res!="":
#         dict3 = json.loads(res)
#         print(dict3)
#         print(type(dict3))
    # res = json.load(f2)
    # print(res)

class student():
    def __int__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

stu1 = student("lili",18,"girl")
# stu2 = student("lilei",19,False)
'''
将stu1对象存储到demo2.txt文件中，然后再读取出来
'''
def obj2dict(obj):
    return {"name":obj.name,"age":obj.age,"sex":obj.sex}


with open("demo2.txt","w") as f3:
    studict = obj2dict(stu1)
    res = json.dumps(studict)
    f3.write(res)