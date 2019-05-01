#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

#使用一行代码
# dict2 = {1:"aa",2:"bb"} #---> {"aa":1,"bb":2}
# print(dict(zip(dict2.values(),dict2.keys())))

# 1.冒泡排序，从控制台输入一个数值列表，对列表进行冒泡排序
"""
例如：[1, 3, 2, 6, 8, 5]
结果：[8, 6, 5, 3, 2, 1]
"""
# str1 =input("请输入一个数值列表")
#
#
# list2 = []
# for i in range(len(list1)):
#     list2 += list1[i]
#     print(list2)
#     for j in range(len(list2)-1):
#         if list2[j] > list2[j+1]:
#             list2[j],list2[j+1]=list2[j+1],list2[j]
#         else:
#             break
# print(list2)

"""
2.#从控制台输入一个时间【06：34：52】，打印出这个时间的下一秒【06：34：53】
"""
# time1 = input("请输入一个时间，时：分：秒")
# tlist = time1.split(":")
# shi = int(tlist[0])
# fen = int(tlist[1])
# miao = int(tlist[2])
# if miao == 59:
#     miao =0
#     fen += 1
#     if fen == 60:
#         fen=0
#         shi+=1
#         if shi == 24:
#             shi = 0
# else:
#     miao +=1
# print("下一秒为%02d:%02d:%02d"%(shi,fen,miao))


import time


musicLrc = '''
[00:03.50]传奇
    [00:19.10]作词：刘兵 作曲：李健
    [00:20.60]演唱：王菲
    [00:26.60]    
    [04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
    [04:49.00]
    [02:47.44][00:43.69]再也没能忘掉你容颜
    [02:54.83][00:51.24]梦想着偶然能有一天再相见
    [03:02.32][00:58.75]从此我开始孤单思念
    [03:08.15][01:04.30]
    [03:09.35][01:05.50]想你时你在天边
    [03:16.90][01:13.13]想你时你在眼前
    [03:24.42][01:20.92]想你时你在脑海
    [03:31.85][01:28.44]想你时你在心田
    [03:38.67][01:35.05]
    [04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
    [04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
    [04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
    [04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
    [04:39.55][04:09.00][02:07.85]
    '''

musicLrc = musicLrc.strip()
mList = musicLrc.splitlines()
print(mList)
for line in mList:
    line = line.strip()





