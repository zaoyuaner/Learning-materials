# 一个子类可以有多个父类,子类有所有父类的属性和方法
class Father():
	def __init__(self,name,money):
		self.name = name
		self.money = money

	def eat(self):
		print("来自Father的吃")
	def palyGame(self):
		print("打LOL")

class Mother():
	def __init__(self,faceValue):
		self.faceValue = faceValue

	def eat(self):
		print("来自Mother的吃")
	def shopping(self):
		print("败家")

class Son(Father,Mother):         # 相同的方法,谁在前就调谁
	def __init__(self,name,money,faceValue):
		# 调用两个父类的构造函数
		Father.__init__(self,name,money)
		Mother.__init__(self,faceValue)

s = Son("小明",100,7)
print(s.name)
print(s.money)
print(s.faceValue)
s.palyGame()
s.shopping()
s.eat()    # Father的吃   相同的方法,谁在前面就选谁 Son(Mother,Father),就会是Mother的吃
