#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
时间戳：从1970年1月1日到现在，单位s
UTC：格林尼治时间，世界标准时间 utc+8
DST：夏令时
time.struct_time(tm_year=2019, tm_mon=3, tm_mday=1, tm_hour=7, tm_min=28, tm_sec=25, tm_wday=4, tm_yday=60, tm_isdst=0)
year：年
mon ：月
mday：日
hour：时
min：分
sec：秒
wday：星期码（0~6） 0：周一  6：周日
yday:今年第多少天
isdst：1 夏令时  0 utc
'''
# print(365*24*60*60*100)
import time

'''
time.time()
功能:获取当前时间的时间戳。

time.gmtime(sec)
功能:将时间戳转为格林尼治时间元组

time.localtime(sec)
功能：将时间戳转为当前时间元组

time.asctime(lt)
功能：将时间元组转时间字符串

time.ctime(time1)
功能：将时间戳转时间字符串

time.strftime("%Y/%m/%d %H:%M:%S",lt)
功能：将时间元组格式化为时间字符串。

time.strptime(str3,"%Y/%m/%d %X")
功能：将时间字符串转为时间元组

time.mktime(strpt)
功能：将时间元组转为时间戳

time.sleep(1)
功能：让cpu休眠x秒执行

time.clock()
通常情况下，会两个一起连用，计算cpu的用时。
模块中出现的第一个clock，用来标记，第二个clock会返回从标记开始
到第二个clock出现的时候cpu的用时。
'''
#
time.sleep(1)
time1 = time.time()

# gt = time.gmtime(time1)
# print(gt)
# lt = time.localtime(time1)
# print(lt)
# asct = time.asctime(lt)
# print(asct)
#
# ct = time.ctime(time1)
# print(ct)

# strt = time.strftime("%Y/%m/%d %H:%M:%S",lt)
# print(strt)
# strt2 = time.strftime("%Y/%m/%d %X",lt)
# print(strt2)

str3 = "2019/03/01 15:42:12"
strpt = time.strptime(str3,"%Y/%m/%d %X")
print(strpt)
# time2 = time.mktime(strpt)
# print(time2)
#
time.clock()
time.sleep(2)
print(time.clock())
# time.sleep(2)
# print(time.clock())