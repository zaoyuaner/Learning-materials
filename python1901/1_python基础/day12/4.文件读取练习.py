#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

def getNumCount(path):
    f = open(path,"r",errors="ignore")
    count = 0
    line = f.readline()
    while line != "":
        # print(line,end="")
        for x in line:
            if x.isdigit():
                count += 1
        line = f.readline()
    return count


path = r"E:\python\python1901\day12\3.文件的读写.py"
print(getNumCount(path))