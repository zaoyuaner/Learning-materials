# 函数的特殊用法

# 1.将一个函数赋值给一个变量,代表这个变量和函数指向同一片内存
# 他们会有相同的作用
print( abs(-4) )
print(abs)            # <built-in function abs> 内建函数(系统函数)
#   将函数赋值给变量 , 那么这个fn的用法与abs一样
fn = abs
print(fn(-4))         # 4 绝对值.fn也可以调用
#   将自定义函数赋值给一个变量
def show():
	print("show4444")
fn2 = show            # 直接将函数名赋值,不要带()
fn2()                 # fn2() = show()

# 2.变量和函数名同名,那么这个名字会被当做普通变量处理
print( max(1,2,3,4,5))
# max = 5
# print(max(1,2,3,4,5))   # 错误! max函数已经被赋值5,失去了max的功能,被当做普通变量处理

# 3.既然函数可以赋值给变量,那么函数同样也可以进行参数的传递
# x,y是变量,function是函数
def change(x,y,function):
	return function(x,y)

print( change(3,4,max))      # 4这个max函数,就会作为实参,传递给function形参
print( change(3,4,min))      # 3

# 传递自定义函数
def show():
	print("hello world")

def getArea(r,function):
	function()
	return 3.1415*r**2

print(getArea(10,show))     # 传递函数过去,第一步执行show函数打印helloworld,第二步return

# def outer():
# 	print("nice to")
#
# def syNodoa(l,d,funtion):
# 	funtion()
# 	return 2*l*d
#
# print(syNodoa(2,34,outer))


