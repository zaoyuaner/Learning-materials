def getAge(age):
	print(age)

# 装饰器
def outer(fn):
	def inner(age):
		if age<0:
			age = 0
		fn(age)
	return inner

@outer          # 使用@（语法糖） 装饰器修饰这个函数，这个函数新增功能就在outer中
def getAge(age):
	print(age)

# 每次使用装饰器，都要获取闭包，再来调用闭包，比较麻烦，python提供了简化方法
f = outer(getAge)
f(10)            # 10
f(-5)            # 0

# 修饰后
getAge(10)       # 10  -->  f = outer(getAge)  -->f(10)
getAge(-5)       # 0

# 语法糖： @outer是一个语法糖，本质上操作并没有改变，还是让程序员用起来更方便