
class Employee(object):
	def __init__(self,num,name):
		self.__num = num
		self.__name = name
	def __str__(self):
		return