# 多态   其他语言中, 一种方法多种实现, 在继承的前提下, 父类规定了子类的属性和方法,
#       使得可以相同的方式调用子类的方法，但会获得不同的功能。
# 鸭子类型
# python本身就是种动态语言, 多态只是python中普遍存在的一种特征! 并不能说是python的典型特点!

class Duck:
	def walk(self):
		print("鸭子走路")

	def swim(self):
		print("鸭子游泳")

class Person:
	def walk(self):
		print("鸭子走路")

	def swim(self):
		print("鸭子游泳")

class Dog:
	def walk(self):
		print("鸭子走路")

	def swim(self):
		print("鸭子游泳")

def show(obj):
	obj.walk()
	obj.swim()

show(Dog())
show(Person())
