#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
歌词解析器
1.把歌词进行解析切片处理，把时间转成对应的浮点数
2.使用字典将时间与歌词进行存储{时间：歌词}
3.循环自动打印歌词【结束循环的条件，key为None的时候】
'''
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
#创建dict存放时间与歌词
musicDict = {}
#去掉歌词前后的空白符
musicLrc = musicLrc.strip()
# print(musicLrc)
#将歌词按行分割
mList = musicLrc.splitlines()
# print(mList)
# 分别处理每一行的歌词
for line in mList:
    #去掉空白符
   line = line.strip()
   #  将时间与歌词分割开
   lineList = line.split("]")
   # print(lineList[-1]) 歌词
   #  遍历时间字符串、分别进行处理
   for i in range(len(lineList)-1):
      #  去掉时间字符串的"[",并且分割为分、秒
      timeList = lineList[i][1:].split(":")
      #将时间字符串转为float类型
      timeF = float(timeList[0])*60 + float(timeList[1])
      #将对应的时间与歌词存储到字典中
      musicDict[timeF] = lineList[-1]
#获取字典中存储的所有时间节点
tList = list(musicDict)
#对时间节点进行排序处理
tList.sort()
#在打印前睡眠第一次的时间【首次打印】
time.sleep(tList[0])
for i in range(len(tList)):
    #判断不是首次
    if i>0:
        #睡眠时间= 当前时间-上次时间
        time.sleep(tList[i]-tList[i-1])
    #打印歌词
    print(musicDict.get(tList[i]))


