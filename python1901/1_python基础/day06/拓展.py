#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
# import pygame
# import  time
# path = r"C:\Users\Administrator\Downloads\dang.mp3"
# # 初始化音频的部分
# pygame.mixer.init()
# #加载音乐
# pygame.mixer.music.load(path)
# #播放音乐
# pygame.mixer.music.play()
#
#
# time.sleep(20)
# #暂停音乐
# pygame.mixer.music.stop()
# time.sleep(20)


'''
1.将音乐加入到歌词解析器
2、将歌词解析封装成函数
'''

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
import pygame
import  time
path = r"C:\Users\Administrator\Downloads\dang.mp3"
pygame.mixer.music.load(path)
pygame.mixer.init()
str1 = "*"
print(str1*30)
print("*"+"欢迎来到酷我音乐播放器".center(18)+"*")
print(str1*30)
choice = input("请选择以下功能：*1.播放   *2.停止   *3.下一曲   *4.上一曲    *5.增大音量   *6.减少音量")
if choice == 1:
    pygame.mixer.music.play()
elif
