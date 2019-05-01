# 类的信息

class Person(object):
	name = "无名"

	def __init__(self, name):
		self.name = name


print(type(Person), type(Person.__name__), Person.__name__)  # 类类型, 字符串类型
print(Person.__dict__)  # 类本身的信息,包括属性,方法,模块,文档字符串等等
print(Person.__bases__)  # 父类  (<class 'object'>,)


# 对象信息
class A:
	def testA(self):
		print("testA")


class B(A):
	def test(self):
		print("B:test")


class C(A):
	def test(self):
		print("C:test")


class D(B, C):
	def __init__(self):
		self.name = "tom"


d1 = D()
d1.test()  # B.test
print(D.__mro__)  # 查看继承顺序
print(dir(d1))  # 对象的信息
print(d1.__class__)  # 对象的类名
print(d1.__dict__)  # 对象属性字典  {'name': 'tom'}
print(d1.__module__)  # 对象的模块名

# issubclass(Sub,Sup)    # 判断子类  如果sub是sup的子类，返回True，
# 							 否则返回False;sub和sup必须是类
# isinstance(obj,class)  # 判断是不是对象或者子类对象   如果obj是class的对象或子类对象，返回True，
# 							 否则返回False；obj可以对象也可以是类，但class必须是类

# callable(object)       # 判断一个对象是否可调用  对象重写__call__方法后可以调用
