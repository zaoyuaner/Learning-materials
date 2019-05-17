#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import os


path = r"E:\python\python1901"
'''
使用递归遍历目录：
1.列举出指定目录下所有的文件
2.进行路径拼接，判断该文件是否为目录
3.若为目录继续列举，若不为目录则打印文件名
'''

def getfile(path):
    #列举出path下所有的文件
    fileList = os.listdir(path)
    print(fileList)
    #遍历文件列表
    for filename in fileList:
        #获取文件的绝对路径
        abspath = os.path.join(path,filename)
        #判断该文件是否为目录
        if os.path.isdir(abspath):
            print("目录",filename)
            #若为目录则继续打印
            getfile(abspath)
        else:
            print("文件",filename)


def getfile2(path,sp=""):
    #列举出path下所有的文件
    fileList = os.listdir(path)
    sp += "\t"
    # print(fileList)
    #遍历文件列表
    for filename in fileList:
        #获取文件的绝对路径
        abspath = os.path.join(path,filename)
        #判断该文件是否为目录
        if os.path.isdir(abspath):
            print(sp,"目录",filename)

            #若为目录则继续打印
            getfile2(abspath,sp)
        else:
            print(sp,"文件",filename)
getfile2(path)


