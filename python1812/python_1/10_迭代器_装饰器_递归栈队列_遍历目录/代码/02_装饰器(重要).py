# 装饰器:  在不修改函数的情况下,为函数增加功能! (基于闭包)

def show():
	print("秀")


# 想打出"天秀",做一个闭包

# 装饰器创建步骤:
# 1.先写出标准的闭包
# 2.在外层函数中接收一个函数为形参fn
# 3.在闭包(inner)中将这个传入的函数fn调用:fn()
# 4.将新增的功能实现,实现在闭包(inner)中.
# def outer(fn):              # 对于装饰器fn必须是函数
# 	def inner():
# 		fn()
# 		print("天秀")     # 需要添加的功能
# 	return inner
#
# f = outer(show)       # 调用ouer函数,并传入show函数作为参数 show == fn
#                       # 对于装饰器,这个参数必须是函数,其他类型一律不接!
#                       # f = inner 返回的inner
#
# f()                   # inner().  调用inner时,第一步就会执行show函数,
                        # 第二步才是执行增加的功能

# 写一个装饰器,为show函数添加一句打印"蒂花之秀",先打印"蒂花之秀",show后打印

# def show2(X):
# 	def show3():
# 		print("蒂花之秀")
# 		X()
# 	return show3
#
# Y = show2(show)
#
# Y()

# 给一个函数添加打印9*9乘法表
def show():
	print("秀")

def outer(fn):
	def inner():
		fn()
		# 这个才是每个装饰器不同的操作
		for i in range(1,10):
			for j in range(1,i+1):
				print("%d*%d=%d"%(j,i,j*i),end=" ")
			print(" ")
	return inner
f = outer(show)
f()


@outer     #
def show():
	print("秀")

show()