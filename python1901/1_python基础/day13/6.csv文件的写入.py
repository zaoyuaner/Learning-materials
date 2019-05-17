#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import csv
from day13.csvhelper import getLine

with open("001.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow([1,2,3])


'''
需求，将读取的csv文件写入到新的文件中。
写成函数
'''

def writerData(path,data):
    with open(path,"w",newline="") as f:
        writer = csv.writer(f)
        for line in data:
            writer.writerow(line)

list1 = getLine("002.csv",4)
writerData("003.csv",list1)
