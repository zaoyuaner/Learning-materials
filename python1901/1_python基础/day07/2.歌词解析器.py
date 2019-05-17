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
import pygame

musicLrc1 = '''[00:01.49]动力火车 - 当
[00:20.53] 当 《还珠格格》主题曲（动力火车）
[00:21.89]喔...喔..喔.喔.喔
[00:28.60]喔...喔..喔.喔.喔
[00:35.44]喔...喔..喔.喔.喔
[00:42.27]喔...喔..喔
[00:52.01]当山峰没有棱角的时候
[00:55.39]当河水不再流
[00:58.79]当时间停住 日夜不分
[01:02.67]当天地万物化为虚有
[01:05.58]我还是不能和你分手
[01:09.70]不能和你分手
[01:12.47]你的温柔是我今生最大的守候
[01:19.19]当太阳不再上升的时候
[01:22.69]当地球不再转动
[01:26.12]当春夏秋冬 不再变化
[01:29.89]当花草树木全部凋残
[01:32.81]我还是不能和你分散
[01:37.10]不能和你分散
[01:39.67]你的笑容是我今生最大的眷恋
[01:42.00]歌词制作:CzBoy QQ:41304064
[01:46.79]让我们红尘作伴 活的潇潇洒洒
[01:50.72]策马奔腾 共享人世繁华
[01:54.17]对酒当歌唱出心中喜悦
[01:57.59]轰轰烈烈把握青春年华
[02:00.72]让我们红尘作伴 活的潇潇洒洒
[02:04.32]策马奔腾 共享人世繁华
[02:07.89]对酒当歌唱出心中喜悦
[02:11.37]轰轰烈烈把握青春年华
[02:18.26]喔...喔..喔.喔.喔
[02:25.17]喔...喔..喔.喔.喔
[02:38.78]喔...喔..喔.喔.喔
[02:38.69]喔...喔..喔
[02:48.80]当太阳不再上升的时候
[02:51.95]当地球不再转动
[02:55.42]当春夏秋冬 不再变化
[02:59.25]当花草树木全部凋残
[03:02.29]我还是不能和你分散
[03:06.13]不能和你分散
[03:09.11]你的笑容是我今生最大的眷恋
[03:16.25]让我们红尘作伴 活的潇潇洒洒
[03:19.91]策马奔腾 共享人世繁华
[03:23.35]对酒当歌唱出心中喜悦
[03:26.80]轰轰烈烈把握青春年华
[03:29.74]让我们红尘作伴 活的潇潇洒洒
[03:33.52]策马奔腾 共享人世繁华
[03:36.98]对酒当歌唱出心中喜悦
[03:40.46]轰轰烈烈把握青春年华
[03:46.71]让我们红尘作伴 活的潇潇洒洒
[03:50.62]策马奔腾 共享人世繁华
[03:54.07]对酒当歌唱出心中喜悦
[03:57.46]轰轰烈烈把握青春年华
[04:00.29]让我们红尘作伴 活的潇潇洒洒
[04:04.30]策马奔腾 共享人世繁华
[04:07.76]对酒当歌唱出心中喜悦
[04:11.16]轰轰烈烈把握青春年华'''

musicLrc2 = ""
#将字符串切割并存储到字典中  硬编码
def getMusicDict(musicLrc1):
    musicDict = {}
    musicLrc = musicLrc1.strip()
    mList = musicLrc.splitlines()
    for line in mList:
        lineList = line.split("]")
        #lineList[-1] 歌词
        for i in range(len(lineList)-1):
            tList = lineList[i][1:].split(":")
            timeF = float(tList[0])*60 + float(tList[1])
            musicDict[timeF] = lineList[-1]
    return musicDict


def printandplayMusic(musicDict,path):
    timeList = list(musicDict)
    timeList.sort()
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    time.sleep(timeList[0])
    for i in range(len(timeList)):
        if i>0:
            time.sleep(timeList[i]-timeList[i-1])
        print(musicDict.get(timeList[i]))





path = r"E:\python\python1901\day06\dang.mp3"
mdict = getMusicDict(musicLrc1)
printandplayMusic(mdict,path)
