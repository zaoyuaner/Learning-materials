# 闭包 closure : 在一个函数中,返回一个函数
# 1.最简单的闭包
def outer():
	def inner():
		print("hello world")
	return inner         # 返回内层函数  注意return的缩进

fn = outer()        #  inner = outer()     fn就用于接收这个内层函数
fn()               #  fn() ==> inner()     调用内层函数

# 2.局部变量: 不能在函数外使用
# 局部变量的生命周期:  声明时,生(创建),  函数结束, 死(销毁)
def show():
	num = 100          # 变量在函数内部定义,那么这个变量称之为局部变量
	print(num)         # show函数调用结束,这个num就会被销毁
	                   # 函数调用时需要进内存跑的,就会占用内存空间,
	                   # 当函数使用完毕之后,变量会随之释放
	                   # 内存泄漏: 内存消耗一直增加,没有释放
show()
# print(num)           # 报错,num没有定义

# 3.使用闭包,能够在函数调用结束后,依然访问局部变量!
def outer():
	a = 10           # 外层函数的变量
	def inner():
		b = 20       # 内层函数的变量
		print(a+b)   # a+b可以打印出来,如果函数没有该变量,那么允许向上找
	return inner
fn = outer()         # outer调用结束后,a变量并不会随之销毁,因为内存函数还在使用
fn()                 # 30  执行内存函数


x =1000              # 函数外的变量
def show():
	print(x)
show()               # 可以打出1000,如果函数没有该变量,那么允许向上找

# 带参数的闭包
def outer(num1):
	def inner(num2):
		print(num1+num2,num1,num2)
	return inner
fn = outer(20)       # fn = inner   fn()执行outer函数
fn(10)               # 30  num2 = 10  num1 = 20
