# global  声明现在这个变量是全局变量,如果函数内对这个变量重新复制,不会认为是局部变量.
num = 100

def show():
	global num           # 全局变量
	print(num)           # 100
	print( id(num))      # 4496189536    全局变量的地址,每次运行地址会变
	num =  50            # 已经声明num为全局变量,所以这个赋值不会被当做局部变量处理
	print(num)           # 50
	print( id(num))      # 4342084128 声明和全局变量同名的num,他是局部变量

show()

print(num)               # 50  全局变量跟着修改了