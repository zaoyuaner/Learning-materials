class Animal():
	def __init__(self,name,age):
		self.name = name
		self.__age = age      # 私有属性无法被继承


	def eat(self):
		print("吃")

	def __show(self):
		print("秀")

class Dog(Animal):
	def myShow(self):
		self.__show()         # 私有方法无法被调用,继承

d = Dog("金毛",2)
d.eat()
# d.show()
# d.myShow()
# print( d.age)
print( d.name)