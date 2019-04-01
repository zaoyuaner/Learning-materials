# 变量的作用域: 变量可以被使用的范围 L --> E --> G --> B 从小到大查找
# L:局部作用域 local .闭包的作用域
# E:函数作用域 enclosing .闭包的外层函数作用域
# G:全局作用域 global .函数之外
# B:内建作用域 bulit-in .内建函数所在的地方

# python程序能够直接使用 list str tuple max min 等内建函数,
# 因为程序启动之后,会自动产生一个内建作用域,让你能够使用这些内建函数

num = abs(-2)    # B 内建作用域  built-in
print(abs)       # <built-in function abs>

x = 10           # G 全局作用域  global变量定义在函数之外,就是这个写代码的白框

def outer():
	y = 10       # E 函数作用域  enclosing   闭包的外层函数作用域
	def inner():
		z = 30   # L 局部作用域  local 闭包
		print(num,x,y,z)        # 闭包最小,没有变量时,可以向上寻找,所以可以打印这四个变量
	return inner
