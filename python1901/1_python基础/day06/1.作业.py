#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.冒泡排序，从控制台输入一个数值列表，对列表进行冒泡排序
例如：[1, 3, 2, 6, 8, 5]  6
结果：[1,2,3,5,6,8]
外循环控制比较的轮数 个数-1
内循环控制比较的次数
1  5
2  4
3  3
4  2
'''
# str1 = input("请输入要排序的数据")
# numList = str1.split()
# print(numList)
# numList2 = []
# for x in numList:
#     numList2.append(int(x))
# print(numList2)
#
# # len = 6 [1,6)
# for i in range(1,len(numList2)): #控制比较的轮数
#     for j in range(len(numList2)-i): #控制比较的次数
#         if numList2[j]>numList2[j+1]:#判断当前元素与下一个元素的大小
#             # 若当前元素大于下一个元素，则调换位置
#             numList2[j],numList2[j+1]=numList2[j+1],numList2[j]
# print(numList2)

'''
2.#从控制台输入一个时间【06：34：52】，
打印出这个时间的下一秒【06：34：53】
'''
time1 = input("请输入一个时间 时:分:秒")
tlist = time1.split(":")
print(tlist)
shi = int(tlist[0])
fen = int(tlist[1])
miao = int(tlist[-1])
if miao==59:
    miao = 0
    fen += 1
    if fen == 60:
        fen = 0
        shi += 1
        if shi == 24:
            shi = 0
else:
    miao += 1

print("下一秒时间为%02d:%02d:%02d"%(shi,fen,miao))




