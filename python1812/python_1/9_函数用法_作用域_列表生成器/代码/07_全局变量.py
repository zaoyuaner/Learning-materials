# 全局变量: 定义在函数之外,任何函数都可以访问的变量

# 白色框框之内就是一个global,全局作用域

num = 100

def test():
	print(num)        # 100  在函数中访问(读取,不能写)全局变量


def show():
	num = 10
	print(num)

test()
show()                 # 10   局部变量已经定义

print(num)             # 100


