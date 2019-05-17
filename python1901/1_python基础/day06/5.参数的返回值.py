#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
return关键字的功能：
1.函数的返回值，函数执行结束之后的结果。
2.结束函数
'''

'''
定义一个函数，求三位的水仙花数，返回水仙花数的个数以及水仙花数。
'''
#
# def getFlower():
#     list1 = []
#     for x in range(100,1000):
#         ge = x%10
#         shi = x//10%10
#         bai = x//100
#         if x == ge**3+shi**3+bai**3:
#             list1.append(x)
#     return len(list1),list1
#
# print(getFlower())


'''
定义一个函数，实现返回一个数整数部分与小数部分。
'''

def getmodf(num):
    numList = str(num).split(".")
    #123.34  123  34
    if len(numList) == 1:
        return float(numList[0]),0.0
    # return float(numList[0]), float(numList[1]) /(10 ** len(numList[1]))
    return float(numList[0]),float("0."+numList[1])

#
print(getmodf(124))
print(getmodf(124.23))
#
#
# def func():
#     for x in range(100):
#         for j in range(100):
#             if j >50:
#                 return
#             else:
#                 print(x,j)
#
#
# func()