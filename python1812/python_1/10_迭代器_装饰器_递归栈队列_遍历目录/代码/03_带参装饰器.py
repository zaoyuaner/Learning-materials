def getAge(age):
	print(age)

# getAge(10)
# getAge(-4)       # 年龄不能为负,若是负数  归零

# 为getAge添加一个功能,如果年龄为负,那么设置为0

# 如果装饰器带参,那么多两个步骤
# 1.给inner添加一个参数
# 2.将这个参数放到fn()中

def outer(fn):
	def inner(age):     # 如果装饰器要带参,那么参数要写成闭包inner的形参
		# 新增功能
		if age < 0:
			age = 0      # 校正之后再执行getAge函数

		fn(age)          # 放参

	return inner

f = outer(getAge)       # getAge -->fn  fn() -->getAge()

f(10)                   # 10   inner(10)
f(-5)                   # 0    inner(-5) --> getAge(0)

