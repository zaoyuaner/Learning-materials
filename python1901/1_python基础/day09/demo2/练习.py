#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
写函数：
从控制台输入我发布的内容的时间，若时间小于1小时的，
显示具体多少分钟前发送的，若发送的时间24小时以内，
显示多少小时前发送，若发送的时间72小时以内，显示多少天前发送
若超过72小时，直接显示日期。
'''
from datetime import datetime


def func(year,mon,day,hour,min,sec):
    nowtime = datetime.now()
    sendtime = datetime(year,mon,day,hour,min,sec)
    #返回时间间隔对象
    dtime = nowtime - sendtime
    if dtime.days==0 and dtime.seconds < 1*60*60:
        print("%d分钟前发布"%(dtime.seconds/60))
    elif dtime.days==0 and dtime.seconds < 24*60*60:
        print("%d小时前发布" % (dtime.seconds / 60/60))
    elif dtime.days <3:
        print("%d天前发布"%dtime.days)
    else:
        strt = sendtime.strftime("%Y/%m/%d %X")
        print("%s发布"%strt)


func(2018,12,20,12,12,12)
func(2019,3,1,16,40,10)
func(2019,3,1,13,40,10)
func(2019,2,28,13,40,10)

