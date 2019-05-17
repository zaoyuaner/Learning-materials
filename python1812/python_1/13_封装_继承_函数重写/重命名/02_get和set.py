# getXxx  setXxx  读取和修改私有属性
class Person():
	def __init__(self,name,age):
		self.__name = name        # 私有
		self.__age = age
		# 特殊变量 ,不推荐使用,一般python系统自己用
		self._height = 180        # _为受保护的变量,不是私有变量,能被访问!使用from import * 不能访问
		self.__money__ = 10000    # 系统内置变量,一般不用

	# 通过set和get函数间接访问私有变量
	def getName(self):
		return self.__name
	def setName(self,name):
		self.__name = name

p = Person("小明",20)
p.setName("小李")
print( p.getName())
print( p._height)           # 可以访问,非私有
print( p.__money__)         # 可以访问,非私有
