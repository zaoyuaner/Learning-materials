# 类属性       类方法
# 对象属性     对象方法

class Person():
	# 类属性: 支持类名.类属性  和  对象.类属性
	name = "xiaoming"

	# 类方法: 支持   和  对象.类方法
	@classmethod
	def show(cls):
		print("hello")

	# 对象属性: 支持  对象.属性名
	def __init__(self,age,name):
		self.age = 20
		self.name = "xiaoming"

	# 对象方法: 支持  对象.方法名
	def myPrint(self):
		print("66666")

print(Person.name)     # 类名.类属性
print(Person.show)     # 类名.类方法

p2 = Person(18,2000)
print(p2.age)          # 对象名.对象属性  20
p2.myPrint()           # 对象名.对象方法
# Person.myPrint(Person)