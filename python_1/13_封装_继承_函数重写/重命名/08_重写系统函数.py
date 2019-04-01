# __str__ 打印对象时输出自定义信息, 优先级高于__repr__

# __repr__打印对象时输出自定义信息

class Person():
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __str__(self):         # name = 小明,age = 20 重写系统函数后
		# 返回一个字符串
		return "name = %s,age = %d"%(self.name,self.age)

p = Person("小明",20)
print(p)               # 默认打出内存地址 <__main__.Person object at 0x10e3f8240>

# 结论 __repr__  __str__ 都未重写时,默认输出内存地址
# __repr__ 重写时,输出__repr__返回的字符串
# __str__重写时,输出__str__ 返回的字符串
# 都重写时,__str__ 优先级高于 __repr__
