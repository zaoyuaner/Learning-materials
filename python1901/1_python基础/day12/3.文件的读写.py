#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
文件读写：
在python提供了内置的方法可以进行文件读写。
注意：当我们读写文件的时候，并不是直接操作磁盘，因为现在所有的
操作系统都不允许普通程序直接操作磁盘，我们其实向操作系统发出文件
读写的请求，通过操作系统预留的接口（API）来进行操作。

'''

'''
读取文件：
语法：
f = open(path,mode,encoding,errors="ignore")
path:文件的路径
mode:文件打开的模式、默认"r"读取
encoding：指定文件的编码格式
errors：ignore 忽略编码错误

注意：当文件读取完毕之后，必须要调用close的方法，因为打开的文件是占用
系统资源的，并且同一时间系统打开的个数也是有限制的。

f.read()
一次性读取文件

f.read(size)
一次性读取size字节的文件【若文件较大，建议使用该方法】

f.readlines()
一次性读取所有行，按行读的。【配置文件】

f.readline()
一次性读取一行,按行读取

注意:当使用read(size)和readline() 要循环读取。

'''
'''
从文件中随便选取一个文件进行读取，读取完毕之后，统计数字出现的次数。
'''
path = r"E:\python\python1901\day12\2.运算符重载.py"
f = open(path,errors="ignore")
# str1 = f.read(100)
# while str1 !="":
#     print(str1,end="")
#     str1 = f.read(100)
# for line in f.readlines():
#     print(line,end="")
# print(f.readline())
str1 = f.readline()
while str1 != "":
    print(str1,end="")
    str1 = f.readline()
f.close()