#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
栈特点：先进后出
在python中，我们使用列表来模仿的栈结构
'''
mystack = []

mystack.append("1")
mystack.append("2")
mystack.append("3")
mystack.append("4")
mystack.append("5")
print(mystack)
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())

'''
需求:使用栈来进行遍历目录
1.根目录进栈
2.根目录出栈
3.列举根目录下面所有的文件
4.判断文件是否为目录
5.当该文件为目录的时候进栈
6.判断栈是否为空
7，不为空继续出栈
8.若为空，循环结束
'''
import os
def getalldir(path):
    #根目录进栈
    stack = []
    #入栈
    stack.append(path)
    while stack:
        #出栈
        path = stack.pop()
        fileList = os.listdir(path)
        for filename in fileList:
            abspath = os.path.join(path,filename)
            if os.path.isdir(abspath):
                print("目录",filename)
                stack.append(abspath)
            else:
                print("文件",filename)

path = r"E:\python\python1901"
getalldir(path)