
# 不定长参数装饰器
def wrapper(fn):
	def inner(*args):         # 闭包接收不定长参数

		print("hello world")

		fn(*args)             # 将这个不定长参数，同样给fn函数

	return inner



@wrapper        # 上面这个装饰器的功能就是多打印了一句hello world
def  show(a,b):
	print(a+b)

show(3,4)       # hello world    7    闭包中多加的功能 + 函数原有的功能

@wrapper
def  show2(a,b,c,d):
	print(a,b,c,d)

show2("hello","world","adsa","sdasd")

