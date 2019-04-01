# 单例
# 使用__new__ 来实现单例设计模式
class Sing(object):
	__instance = None
	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		return cls.__instance
	# @classmethod
	# def getInstance(cls):
	# 	return cls.__instance

p = Sing()
print(p)
p2 = Sing()
print(p2)

