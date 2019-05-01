#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
**********************
* 欢迎来到酷我音乐播放器*
**********************

请选择以下功能：
***********************
* 1.播放       2.停止  *
* 3.下一曲     4.上一曲 *
* 5.增大音量   6.减少音量*
************************
'''

import time
import pygame


def weclome():
    print('''
    **********************
    * 欢迎来到酷我音乐播放器*
    **********************
    ''')


def choice():
    print('''
    ***********************
    * 1.播放       2.停止  *
    * 3.下一曲     4.上一曲 *
    * 5.增大音量   6.减少音量*
    ************************
    ''')
    num = input("请选择要操作的功能：")
    return num

def play(path,volume=0.5):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)


def perMusic(path,musicList,index):
    if index == 0:
        print("已经是第一曲了。。。")
        return index
    index -= 1
    play(path+"\\"+musicList[index])
    return index


def nextMusic(path,musicList,index):
    if index == len(musicList)-1:
        print("已经是最后一曲了。。。")
        return index
    index += 1
    play(path+"\\"+musicList[index])
    return index

def stopMusic():
    pygame.mixer.music.stop()

def addVolume(volume):
    if volume >= 1:
        print("已经是最大音量了")
        return volume
    volume += 0.1
    pygame.mixer.music.set_volume(volume)
    return volume


def subVolume(volume):
    if volume <= 0:
        print("已经是最小音量了")
        return volume
    volume -= 0.1
    pygame.mixer.music.set_volume(volume)
    return volume


weclome()
path = r"D:\kugou"
musicList = ["薛之谦 - 演员.mp3","薛之谦 - 绅士.mp3","薛之谦 - 你还要我怎样.mp3","薛之谦 - 刚刚好.mp3","薛之谦 - 丑八怪.mp3"]
index = 0
volume = 0.5
while True:
    time.sleep(1)
    n = choice()
    if n == "1":
        print("播放音乐")
        play(path+"\\"+musicList[index])
    elif n == "2":
        print("停止")
        stopMusic()
    elif n == "3":
        print("下一曲")
        index = nextMusic(path,musicList,index)
    elif n == "4":
        print("上一曲")
        index = perMusic(path,musicList,index)
    elif n == "5":
        print("音量增大")
        volume = addVolume(volume)
    elif n == "6":
        print("音量减小")
        volume = subVolume(volume)

