# 有一个参数的函数
# 求圆面积,需要一个半径作为参数
import math
def getArea(radius):
	print(("%.2f"%(math.pi*radius**2)))

getArea(10)

# 有两个参数的函数
# 求和. num1 num2 叫做形式参数,是一个变量,值不确定
def add(num1,num2):  # 多个参数用逗号隔开
	print(num1 + num2)

add(10,200)       # 10,200 叫做实际参数,它的值确定
add("a","casd")
add(112,1,)

# 有多个参数的函数   *后面的args是一个元组形式
def myMax(*args):          # 加*号不定长参数,相较于max,可以输入任意个参数
	print(args)
	if args:         # 空类型都会代表False
		max1 = args[0]
		for item in args:
			if item > max1:
				max1 = item
		print(max1)

myMax()            # 空元组无法取第0个,添加判断语句
myMax(5)          # (5,)  元组,单个会加个,
myMax(23,23,234)