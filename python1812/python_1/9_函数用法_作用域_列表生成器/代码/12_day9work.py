# 练习:
# 万年历
# a: 先输出提示语句,并接受用户输入的年\月
# b: 根据用户输入的年,先判断是否是闰年
# c: 根据用户输入的月来判断月的天数
# d: 用循环计算用户输入的年份距1900年1月1日的总天数
# e: 用循环计算用户输入的月份距输入的年份的1月1日共有多少天
# f: 相加d与e的天数,得到总天数
# g: 用总天数来计算输入月的第一天的星期数    1900,1,1星期一
# h: 根据g的值,格式化输出这个月的月历


def isLeapyear(year):                # b:判断是不是闰年
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		return True
	return False
# result1 = isLeapyear(year)
# if result1:
# 	print("是闰年")
# else:
# 	print("不是闰年")
# dict1 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def getMonthDay(month,year):               # c:判断月的天数
	# if month%2==0 :
	# 	if 2 < month <7:
	# 		return 30
	# 	elif 7 < month < 13:
	# 		return 31
	# 	elif month == 2:
	# 		if result1:
	# 			return 29
	# 		else:
	# 			return 28
	# else:
	# 	if 0 <month <7:
	# 		return 31
	# 	elif 7 <month <13:
	# 		return 30
	if month in [1,3,5,7,8,10,12]:
		return 31
	elif month in [4,6,9,11]:
		return 30
	else:
		return 29 if isLeapyear(year) else 28    # 如果是闰年返回29,否则返回28
		# if isLeapyear(year):
		# 	return 29
		# else:
		# 	return 28     #等同上一句
# 	return getMonthDay
# result2 = getMonthDay(month)
# print("有",result2,"天")

def getD_value(year):       # d:距离1900.1.1的总天数   闰年366天,平年365天
	sum1 = 0
	for i in range(1900,year):
		sum1 += 366 if isLeapyear(year) else 365
	return sum1
# 		isLeapyear(i)
# 		if isLeapyear:                #如果是闰年，计数
# 			count1 += 1
# 	sum1 = (count1 * 366 + (year -1900 - count1)*365 - 1)
# 	return sum1
# result3 = getD_value(year)
# print("距1900年1月1日的总天数:",result3)



def getM_value(month,year):      # e: 用循环计算用户输入的月份距输入的年份的1月1日共有多少天
	total = 0
	for i in range(1,month):
		total += getMonthDay(i,year)
	return total

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
# 	sum3 = 0
# 	for i in range(1,month):
# 		sum3 += getMonthday(i)
# 	return sum3
# result4 = getM_value(month)
# print("距离输入的年份的1月1日共有:",result4,"天")

totalDays = getD_value(year) +getM_value(month,year)
# def SumDay():               # f: 相加d与e的天数,得到总天数
# 	sum4 = result4 + result3
# 	return sum4
# result5 = SumDay()
# print("总共",result5,"天")

# def week(month):      # 对7取余!     # g: 用总天数来计算输入月的第一天的星期数
week = (totalDays +1 )%7        # 因为1900年1月这个时间不加1就会得到0
print(week)
# week用0表示周一,6表示周天

# def monthlyCalendar():      # h: 根据g的值,格式化输出这个月的月历
# print("星期一","\t","星期二","\t","星期三","\t","星期四","\t","星期五","\t","星期六","\t","星期日")
print("\t".join(["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]))
# 	pass
#
# monthlyCalendar()
# 先打印这个星期几之前的空格
# 是周几,就打出week-1个空格  i = 0,1,2,3
for i in range(week+1):
	print(" ",end="\t\t")

# 将这个月的所有天数打印出来
monthDays = getMonthDay(month,year)

for day in range(1,monthDays+1):
	print(day,end="\t\t")
	if (week + day +1)%7 ==0:    # 如果一周打印完毕,换行
		print(" ")




