#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import json


class student():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

stu1 = student("lili",18,True)

def obj2dict(obj):
    return {"name":obj.name,"age":obj.age,"sex":obj.sex}


def dict2obj(dict1):
    return student(dict1["name"],dict1["age"],dict1["sex"])

# with open("demo2.txt","w") as f3:
#     res = json.dumps(stu1,default=obj2dict)
#     print(res)
#     f3.write(res)

with open("demo2.txt","r") as f:
    res = f.read()
    stu2 = json.loads(res,object_hook=dict2obj)
    print(stu2)
    # print(res)
    # print(type(res))
    # dict1 = json.loads(res)
    # print(dict1)
    # print(type(dict1))
    # stu2 = dict2obj(dict1)
    # print(stu2)
