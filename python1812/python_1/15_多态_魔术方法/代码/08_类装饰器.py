# 类装饰器          回顾装饰器的内容
class Pig:
	def __call__(self, func):
		def inner(*args, **kwargs):
			func(*args, **kwargs)
			print("*****")

		return inner


@Pig()  # 注意带()
def test():
	print("帅" * 5)


test()
