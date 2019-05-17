import calendar

# 直接输出对应月的万年历
print( calendar.month(2019,2))

# 打印一整年的日历
print( calendar.calendar(2019))

# 以二维列表的形式显示某个月,空格补0
print( calendar.monthcalendar(2019,1))

# calendar.setfirstweekday(6)            # 设置日历每周的第一天! 6代表周日

# 查询日历中以哪天开头,0代表周一
print( calendar.firstweekday())

# 判断是不是闰年
print( calendar.isleap(2000))            # True

# 统计两个年份之间闰年的总数   4年一闰
print( calendar.leapdays(2000,2020))

# 获取是周几  0【星期一】~6【星期天】
print( calendar.weekday(2019,1,2))