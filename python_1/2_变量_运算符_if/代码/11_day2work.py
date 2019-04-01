# 1.判断下面标识符是否合法并说明不合法的原因
# 	@abc.com        不合法，特殊字符
# 	123ok           不合法，首位不能是数字
# 	_xiaoming       合法
# 	Xiaoming_$      不合法，特殊字符
# 	interface       合法
# 	sina@163        不合法，特殊字符

# 2.从控制台输入圆的半径，计算周长和面积
import math

r = float(input("请输入圆的半径："))
C = 2 * r * math.pi  # 周长
S = math.pi * r ** 2  # 面积
print("周长：", "%.2f" %C, "面积：", "%.2f" %S)   # %.2f 保留两位小数。
# 格式化输出
# %d 打印整数
# %f 打印浮点数
# %s 打印字符
print("面积：%.2f %d %s"%(S, 10,"hello"))

# 3.汽车速度40KM/h，行驶了45678.9km，求所用时间。
S = 45678.9
v = 40
print("汽车所用时间为：", "%.2f" % (S / v), "小时")  # 保留两位小数

# 4.将华氏温度转换为摄氏温度
F = float(input("请输入华氏温度："))
C = (F - 32) / 1.8
print("摄氏温度为：", "%.2f" % C)  # "%.2f" %保留两位小数

# 5.输入两个数，输出较大的值
sum1 = float(input("请输入第一个数："))
sum2 = float(input("请输入第二个数："))
if sum1 >= sum2:
	print("第一个数%f大"%(sum1))
else:
	print("第二个数%f大"%(sum2))

# 6.模拟玩骰子游戏
import random
# random.choice(range(5))  首先通过range（5）生产一个序列，值为0 1 2 3 4 ，从这个序列中随机抽一个。
# for n in range(6):    不需要for循环！range(6)是0-5，不包括6。
num1 = random.randint(1, 6)  # randint 随机整数！包括上下限！
print("掷出的数字为：", num1)
if num1 == 1:
	print("跳舞")
elif num1 == 2:
	print("唱歌")
elif num1 == 3:
	print("深蹲")
elif num1 == 4:
	print("学狗叫")
elif num1 == 5:
	print("请吃饭")
elif num1 == 6:
	print("倒立")
print("哈哈哈哈！")

# 中级1.0<x<99,0<y<199,if x>y 则输出x,if x=y 则输出x+y,if x<y 则输出y
import random
x = random.randint(0,99)    # x = random.choice(range(99))
y = random.randint(0,199)   # y = random.choice(range(199))
print(x)
print(y)
if x < y:
	print(y)
elif x == y:
	print(x + y)
else:
	print(x)

# 从控制台输入三个数，输出较大的值。。。假设一个最大值，比较就ok
print("请输入三个数：")
num1 = int(input())
num2 = int(input())
num3 = int(input())
max = num1
if num2 > max:
	max = num2
if num3 > max:
	max = num3
print("最大的数：", max)

#从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
num = int( input("请输入一个三位数：") )    #非三位数就要校验
if num<100 or num>999:      # 所有由用户输入的数，都要进行校验
	print("输入不正确")
else:
	#正确的数进行运算
	a = num // 100  #百位
	b = num // 10 %10            #十位
	c = num % 100                #个位
	if num == a**3 + b**3 + c**3:
		print("是水仙花数")
	else:
		print("不是水仙花数")

# 从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
num = int( input("请输入一个五位数：") )   #如果输入的是六位数或者四位数怎么办。
a = num % 10                 #个位
b = num // 10 % 10           #十位
c = num // 1000 % 10         #千位
d = num // 10000             #万位
if a == d and b == c:
	print("这个数是回文数")
else:
	print("这个数不是回文数")
