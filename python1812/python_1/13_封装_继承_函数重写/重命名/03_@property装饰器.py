# @property 装饰器 : 简化get函数和set函数,让他们像属性一样使用,使用后可以继承私有属性

class Person():
	def __init__(self,name,age):
		self.__name = name
		self.__age = age

	# get函数
	@property
	def name(self):        # 这个函数名可以随意写
		return self.__name

	# set函数
	@name.setter
	def name(self,myName):
		self.__name = myName

	# 写age的getset函数
	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,myAge):
		self.__age = myAge

p = Person("张三",20)
p.name = "李四"           # 实质上是调用了set函数
print( p.name)           # 李四  实质上是调用了get函数

p.age = 23
print( p.age)