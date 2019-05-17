# 运算符重载

class Rect:
	def __init__(self,width,height):
		"""
		:param width: 宽
		:param height: 高
		"""
		self.width = width
		self.height = height

	def __add__(self, other):   # 代表了系统 "+" 运算符

		return self.__class__(self.width+other.width, self.height+other.height)

	def __str__(self):
		return str(self.width)+ ":" + str(self.height)

r1 = Rect(12,23)
r2 = Rect(10,10)
print(r1.__add__(r2))               # 22:33
print(r1+r2)

# 重写 ">,<" 运算符  __gt__       >= __ge__
class Pig:
	def __init__(self,weight):
		self.weight = weight

	def __gt__(self, other):
		"""
		# 运算符重载不要违反运算符本身的规律
		:param other:  第二个对象,self是第一个对象
		:return:
		"""
		return self.weight < other.weight

pig1 = (100)
pig2 = (200)
res = pig1 < pig2  # True  pig1.__gt__(pig2) -> __gt__(pig1,pig2)
print(res)


