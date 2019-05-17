#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
csv文件的读写：

'''

import csv

# with open("002.csv","r") as f:
#     res = csv.reader(f)
#     for line in res:
#         print(line)

'''
需求：写一个函数，
函数功能：传递一个csv文件路径，并且传递一个参数n，
返回这个csv文件的前n行
'''

def getLine(path,n):
    list1 = []
    with open(path,"r") as f:
        infoline = csv.reader(f)
        num = 0
        for line in infoline:
            num += 1
            if num>n:
                return list1
            else:
                list1.append(line)
    return list1

print(getLine("002.csv",3))
