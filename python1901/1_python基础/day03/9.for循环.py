#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
for循环
语法:
for 变量 in 序列:
    循环体

变量:自己取的名字
序列:要访问的序列
功能: 依次将序列中的元素取出赋值给变量,当元素全部取出的时候,循环结束.
'''
list1 = [1,2,3,4,5,6,7,8,9,10]
for x in list1:
    print(x)

'''
需求:使用for循环1+2+3..+10的和
'''
res = 0
for x in list1:
    res += x
print(res)
'''
range([start,]end[,step])
start:若不写默认从0开始
end:必须写
step:步长,默认为1
功能:产生一个[start,end)的一个序列步长为step.
'''

# for i in range(10,0,-1):
#     if i%2 != 0:
#         print(i)

'''
需求:从控制台输入一个整数n,求1+2+..+n的和
从控制台输入一个整数n,求1*2*..*n的积
'''
# n = int(input("请输入一个整数:"))  #10
# res = 0
# ji = 1
# for x in range(1,n+1):
#     res += x
#     ji *= x
# print(res)
# print(ji)

'''
需求:求1!+2!+3!+...+n!
n! = 1x2x3..xn
'''
n = int(input("请输入一个整数")) #n=5
res = 0
for j in range(1,n+1): #j=1    j=2
    ji = 1
    for x in range(1,j+1):  #x=1, [1,2)  x=1 [1,3)
        ji *= x            #1!        #ji=1!*2
    # print(ji)
    res += ji
print(res)