

# 1. 判断是否是闰年
def isleap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

#获取每个月的天数
def get_day(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if isleap(year) else 28

#输入年 1月日 到1900年 1月1日的总天数
def get_year_total_days(year):
    #声明一个变量记录总天数
    total = 0
    for y in range(1900, year):
        total += 366 if isleap(y) else 365

    return total

#输入月份1号 距离当前1月1日有多少天
def get_month_total_days(month, year):
    #变量记录总天数
    month_total = 0
    for m in range(1, month):
        month_total += get_day(m, year)

    return month_total

#键盘输入年 和 月
year = int(input("请输入年份:"))
month = int(input("请输入月份:"))

#相加总天数
total_days = get_year_total_days(year) + get_month_total_days(month, year)

#用总天数 对 7取余
week = (total_days + 1) % 7
print(week) # 星期天 --- 星期六  0 --- 6

print("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六")   # \t缩进
'''
空格 和 天数

空格+天数 % 7 == 0

3 月 1
                1   2   3
4   5   6   7   8   9   10
'''
#先填补空格
for i in range(week):
    print(" ", end="\t\t")

#打印天数
days = get_day(month, year)
for m in range(1, days + 1):
    print(m, end="\t\t")
    #换行
    if (week + m) % 7 == 0:
        print()