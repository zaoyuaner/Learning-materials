#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
1.设计一个函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5'''
# def just(object1):
#     if len(object1)<5:
#         print("您输入的对象长度小于5")
#     elif len(object1)== 5:
#         print("您输入的对象长度等于5")
#     else:
#         print("您输入的对象长度大于5")
# just("dhwfff")

'''2.设计一个函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
【字符串中含有空格，列表与元组中函数有空串】。若含有则返回True，否则返回False
”hello world“ [12,34,"",23]'''
# def check(object1):
#     if ' 'in str(object1):
#         print("ture")
#     elif "" in list(object1):
#         print("ture")
#     elif ""in tuple(object1):
#         print("ture")
#     else:
#         print("False")
# print(check(hello wdd))




'''3.设计一个函数，从控制台输入一个整数，计算整数绝对值的阶乘，n！=1 x 2 x … x n【写成函数】'''
# def jiecheng(num):
#     num = int(abs(num))
#     ji = 1
#     for i in range(1,num+1):
#         ji*=i
#     return(ji)
# print(jiecheng(4))


'''4.从控制台输入两个正数，求这两个正数的最大公约数，与最小公倍数
注意：最大公约数的公式：
m % n = r ，m = n  n = r  ，r == 0  输出m ，若不为0则继续循环
最小公倍数的公式：
最小公倍数 = 两个正数的乘积/最大公约数
'''
# def maxgongyueshu(m,n):
#     list1=[]
#     for i in range(1,max(m,n)):
#         if m % i ==0 and n % i ==0:
#             list1.append(i)
#     maxgongyueshu=max(list1)
#     mingongbeishu=int(m*n/maxgongyueshu)
#     return (maxgongyueshu,mingongbeishu)
# print(maxgongyueshu(15,25))

'''
1.将音乐加入到歌词解析器
'''
import pygame
import time
musicLrc ='''
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
    [04:39.55][04:09.00][02:07.85]'''
path = r"D:\python\python1901（daima）\day06"
pygame.mixer.init()
pygame.mixer.music.load(path)
pygame.mixer.music.play()
musicDict = {}
musicLrc = musicLrc.strip()
mList = musicLrc.splitlines()
for line in mList:
   line = line.strip()
   lineList = line.split("]")
   for i in range(len(lineList)-1):
      timeList = lineList[i][1:].split(":")
      timeF = float(timeList[0])*60 + float(timeList[1])
      musicDict[timeF] = lineList[-1]
tList = list(musicDict)
tList.sort()
time.sleep(tList[0])
for i in range(len(tList)):
    if i>0:
        time.sleep(tList[i]-tList[i-1])
    print(musicDict.get(tList[i]))
'''
2、将歌词解析封装成函数
'''
def musicLrc():
    import time
    musicLrc ='''
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
        [04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远'''
    musicDict = {}
    musicLrc = musicLrc.strip()
    mList = musicLrc.splitlines()
    for line in mList:
       line = line.strip()
       lineList = line.split("]")
       for i in range(len(lineList)-1):
          timeList = lineList[i][1:].split(":")
          timeF = float(timeList[0])*60 + float(timeList[1])
          musicDict[timeF] = lineList[-1]
    tList = list(musicDict)
    tList.sort()
    time.sleep(tList[0])
    for i in range(len(tList)):
        if i>0:
            time.sleep(tList[i]-tList[i-1])
        print(musicDict.get(tList[i]))
print(musicLrc())

'''
写一个音乐播放器，五首歌：
**********************
* 欢迎来到酷我音乐播放器*
**********************
请选择以下功能：
***********************
* 1.播放       2.停止  *
* 3.下一曲     4.上一曲 *
* 5.增大音量   6.减少音量*
************************
使用函数来写。
'''
