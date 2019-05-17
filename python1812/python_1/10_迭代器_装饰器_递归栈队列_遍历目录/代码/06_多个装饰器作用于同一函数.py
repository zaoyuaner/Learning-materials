
# 多个装饰器作用于同一函数
def wrapper(fn):
	def inner():
		print("11111")
		fn()
	return inner

def wrapper2(fn):
	def inner():
		print("111112222")
		fn()
	return inner

@wrapper
@wrapper2                 # 多个装饰器可以修饰同一个函数,装饰器新增的功能都会执行
						  # 但是原函数只会被执行一次
#
def show():               # 原函数有参,则装饰器inner就带参
	print("秀")

show()                    # 只会打出一个秀!