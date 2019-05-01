#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import calendar

'''
calendar.month(year,month)
返回指定年月的日历

calendar.calendar(year)
返回指定年份的日历

calendar.isleap(year)
判断指定的年份是否为闰年

calendar.leapdays(year1,year2)
返回[year1,year2)之间的闰年的个数

calendar.monthrange(year,month)
返回该月的天数以及第一天的星期码

calendar.monthcalendar(year,month)
返回指定月份的以星期为单位的一个序列，若不是本月日期，使用0来代替

calendar.weekday(year,month,day)
返回指定日期的星期码
'''
# print(calendar.month(2019,3))
# print(calendar.calendar(2019))
# print(calendar.calendar(2020))
#
# print(calendar.isleap(2017))
# print(calendar.isleap(2018))
# print(calendar.isleap(2019))
# print(calendar.isleap(2020))
# print(calendar.leapdays(2000,2012))
#
#
# print(calendar.monthrange(2019,3))
# print(calendar.monthrange(2019,2))
# print(calendar.monthrange(2019,1))

# print(calendar.monthcalendar(2019,3))
#
# print(calendar.weekday(2019,3,1))


# print(calendar.leapdays(2000,2012))
# print(calendar.monthcalendar(2019,3))
print(calendar.weekday(2019,3,16))