import datetime

# 获取当前的时间
d1 = datetime.datetime.now()
print(d1,type(d1))             # datetime类型

# 通过元组生成时间
d2 = datetime.datetime(2019,2,22,2,34,12)   # 输入元组生成
print(d2)

# 通过指定的格式生成时间,需要接受一个时间元组,和一个格式
d3 = datetime.datetime.strftime(d2,"%Y/%m/%d")
print(d3)

# 通过指定字符串获取时间  前后格式需要保持一致
d4 = datetime.datetime.strptime("2018-5-20 10:22:22","%Y-%m-%d %H:%M:%S")
print(d4)

# 求时间差
d5 = datetime.datetime(2018,5,4,10,00,00)
d6 = datetime.datetime(2018,5,10,10,55,00)
result = d6 - d5
print(result)
print(result.days)     # 6 获取结果中的天数
print(result.seconds)   # 3300 获取时分秒所组成的秒数