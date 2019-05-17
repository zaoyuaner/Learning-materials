# nonlocal : local是局部作用域,定义域闭包中,nonlocal 将闭包中的变量作用域放大
# 所以在第二个def里面才会出现
x = 10
def outer():
	x = 20
	def inner():
		nonlocal x     # 将这个x的局部作用域放大到E函数作用域,不能将作用域放大到G全局作用域
		x = 30         # 所以在第二个def里面才会出现
		print(x)       # L 30
	inner()            # 30  inner函数在outer内,自己调用
	print(x)           # E 20  放大后 x变为30

outer()
print(x)               # 10

# y = 20
# def outt():
# 	y = 30
# 	def ooadi():
# 		y = 40
# 		nonlocal y     # 这样不行,会报错,nonlocal应该紧挨着def
# 		print(y)
# 	ooadi()
# 	print(y)
# outt()
# print(y)