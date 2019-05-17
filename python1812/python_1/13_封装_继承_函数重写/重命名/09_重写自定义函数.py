class Animal():
	def show(self):
		print("hello")

class Dog(Animal):
	def show(self):
		# 支持三种形式调用父类的方法
		super(Dog, self).show()      # 使用super调用父类函数
		super().show()
		Animal.show(self)

		print("world")

d = Dog()
d.show()
