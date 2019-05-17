# 属性私有化 private(封装)

class Person():
	def __init__(self,name,age):
		self.name = name
		self.age = age

# 没有保护的情况下,对象的属性可以随意被修改,不安全
p = Person("xiaoming",20)
p.name = "lili"
print(p.name)

class Person():
	def __init__(self,name,age):

		# 变量名前有两个下划线,代表这是私有变量
		# 私有变量: 只允许在本类方法使用,类外无法直接访问
		self.__name = name
		self.__age = age

	def showMyName(self):
		# 通过函数间接读取私有变量
		print("我的名字是:",self.__name)

p = Person("小明",20)
# print( p.__name)             # 类外,无法被访问
p.showMyName()                 # 类外,间接访问

# p.name = "李四"                 # 这个name是动态绑定,和__name不是同一个
# print( p.name)

# 这个私有变量,实际上是python把它变成了 _类名__属性名的一个格式
# 所以这种私有,并不是完全私有,想修改还是可以修改的
p._Person__name = "lisi"
# print(p._Person__name)       # 小明  不重新赋值就是小明.
p.showMyName()                 # lisi

