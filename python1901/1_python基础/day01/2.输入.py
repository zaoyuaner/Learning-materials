#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

# print("请输入您姓名")
#输入语句
'''
input(string)
string:提示语句
'''
# a = input("请输入您的姓名")
# print(a)
# print(input("请输入您的姓名"))
'''
使用控制台输入姓名、年龄以及爱好，把输入的东西，打印一个自我介绍
'''
name = input("请输入您的姓名")
age = input("请输入您的年龄")
hobby = input("请输入您的爱好")
print("大家好，我是",name,"我今年",age,"我喜欢",hobby)

'''
格式化输出
%s 代表字符串
字符串：使用单引号或是双引号括起来的任意字符，我们就称它为字符串。
print("%s"%(变量)),注意%s的个数，要跟后面小括号中变量的个数相同，
数据类型要保持一致。
'''
print("大家好，我是%s,我今年%s岁，我喜欢%s"%("lili",age,hobby))