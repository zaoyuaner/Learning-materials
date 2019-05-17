# 需求：富二代王思聪开着豪车，很自豪的向他的新女友炫耀
# 类: 人类, 车
# 属性: 富, 新
# 方法: 开车, 炫耀
# 对象: 王思聪, 女友

class Car():
	def __init__(self,brand,color):
		self.brand = brand    # 牌子
		self.color = color    # 颜色

class Person():
	def __init__(self,name,money):
		self.name = name
		self.money =money

	def driveCar(self,car):
		print( "%s驾驶着%s色%s在高速上飙车"%(wang.name,car.color,car.brand))

	def showCar(self,car,per):
		print( self.name,"向新女友",per.name,"炫耀:我有",self.money,"亿,我有:",car.brand,"牌的车")

car = Car("法拉利","骚红")
wang = Person("王思聪",999999)
snow = Person("雪梨",10000)

wang.driveCar(car)
wang.showCar(car,snow)


