#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

from datetime import datetime
import time

'''
datetime.now()
功能:返回一个datetime对象

dt.strftime(formstr)
功能:将datetime对象格式化为字符串

dtt = dt2-dt
两个datetime对象相减的时候，会返回一个时间差对象
dtt.days
获取间隔的天数
ddt.seconds
获取间隔的秒数
'''
'''
写函数：
从控制台输入我发布的内容的时间，若时间小于1小时的，
显示具体多少分钟前发送的，若发送的时间24小时以内，
显示多少小时前发送，若发送的时间72小时以内，显示多少天前发送
若超过72小时，直接显示日期。
'''
# d1 = datetime(2018,12,2,14,36,52)
# print(d1)

dt = datetime.now()
print(dt)
# print(type(dt))
# #
# strt = dt.strftime("%X")
# print(strt)
# print(type(strt))
time.sleep(2)
dt2 = datetime.now()
print(dt2)
dtt = dt2-dt
print(dtt)
print(type(dtt))
print(dtt.days)
print(dtt.seconds)

