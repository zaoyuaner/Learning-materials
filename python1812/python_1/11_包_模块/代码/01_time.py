# 时间的三种表示形式
# 1.时间戳  距离1970.1.1 00:00:00的秒数, 是数字,便于进行数学计算,time.time  time.mktime
# 2.时间元组  便于获取时间的年月日时分秒  gmtime  localtime
# 3.时间字符串  便于显示时间  asctime(元组转字符串)  ctime(时间戳转字符串)  strftime(格式化) strptime
import time
# 1.获取当前时间戳
t1 = time.time()          # 0时区的时间戳,本地时间需要加减时区
print(t1)

# 2.时间元组
# gm  GMT. 格林尼治时间.
t2 = time.gmtime(t1)      # 0时区时间
# tm_wday: 星期几(0星期1,6星期天)  tm_yday:本年的第几天   tm_isdst:是不是夏令时(0不是)
print(t2)
print(t2[0],t2[1],t2[2])               # 2019 通过下标获取年月日

t3 = time.localtime(t1)   # 获取本地所在时区的时间元组
print(t3)

t4 = time.mktime(t3)      # 获取本地时间的时间戳,和t1值一样.0时区时间戳值和本地时间戳值一样
print(t4)

# 3.asctime()  将时间元组转成字符串的形式
t5 = time.asctime(t3)     # t3是元组
print(t5)

# ctime()      将时间戳转成字符串的形式
t6 = time.ctime(t4)       # 本地与0时时间戳都是一个值
print(t6)

# 将t3这个时间元组按照格式输出成字符串
# %y:两位数的年  (千年虫)
# %Y:年
# %m:月
# %d:日
# %H:时【24小时制】
# %I:时【12小时制】
# %M:分
# %S:秒
t7 = time.strftime("%Y-%m-%d %H:%M:%S",t3)    # 严格区分大小写
print(t7)

# 将字符串格式的时间通过指定格式转换成时间元组
t8 = time.strptime("2019/2/3 15:22:30","%Y/%m/%d %H:%M:%S")
print(t8)

print("asd")
time.sleep(2)     # 将程序睡眠2秒
print("123")


print(time.clock())   # 程序走完所花的时间


# 求 "2019-3-28"后三天的时间
# 1.将这个字符串转成时间元组
# 2.将这个时间元组转时间戳(能进行时间运算)
# 3.让这个时间戳加上 3*24*60*60
# 4.再将这个时间戳转成字符串
# 先转元组
t9 = time.strptime("2019-3-28","%Y-%m-%d")
print(t9)
# 将时间元组转时间戳
t10 = time.mktime(t9)
t10 += 3*24*60*60
# 将时间戳转时间元组
t11 = time.localtime(t10)
# 按照指定的格式字符串输出
t12 = time.strftime("%Y-%m-%d",t11)
print(t12)