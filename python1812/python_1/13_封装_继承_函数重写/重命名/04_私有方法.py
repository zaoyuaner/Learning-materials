# 私有方法

class Person():
	def __init__(self,name,age,weight):
		self.__name = name
		self.__age = age
		self.__weight = weight

	def showName(self):
		print("我的名字是:",self.__name)

	def __showWeight(self):            # 私有方法,只能在本类调用,不能再类外调用
		print("我的体重是:",self.__weight)

	# 如果要使用私有方法,只能间接调用
	def show(self):
		self.__showWeight()       # 对象方法,需要对象来调用
p = Person("小丽",20,110)
p.showName()                           # 可以访问
# p.__showWeight                       # 无法访问
p.show()                               # 间接调用