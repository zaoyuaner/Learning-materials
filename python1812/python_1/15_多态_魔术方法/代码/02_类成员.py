# 类成员: 类属性, 类方法
# 对象成员: 对象(成员)属性, 对象方法

class Person(): # 类名的定义规则,只能是字母,数字,下划线,遵循驼峰原则# 首字母必须大写!(约定)
# 类属性         通过类名访问, 通过实例化对象访问
	name = "231"
	age = 0
	__sdw = 29           # 私有类属性
# 对象属性(成员)
	def __init__(self,name1,age):    # 实例化对象时,才能访问
		self.name = name1
		self.age = age

# 对象方法(成员)
	def show(self):      # self指,当前对象,会代表等下实例产生的对象
		print("hello")

# 类方法(装饰器), 不用实例化对象就可以调用
	@classmethod
	def myPrint(cls):
		# print(cls.show(cls))
		print("6666")

# 静态方法    就是类内的全局函数   可以通过类名和对象调用
	@staticmethod
	def homework():
		pass

# 静态方法和类方法的区别: 静态方法没有固定参数cls

p = Person("i",20)
p.myPrint()
p.show()
p.homework()
Person.myPrint()
# Person.show(Person)