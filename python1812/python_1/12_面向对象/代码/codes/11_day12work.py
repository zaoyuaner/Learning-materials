# 利用面向对象的思想写下面的程序：直接赋值

# 1.小美在朝阳公园溜旺财【注：旺财是狗】
# 类:人  狗
# 对象: 小美  旺财
# 方法: 溜
# 属性: 朝阳公园
class Dog():
	def __init__(self,name):
		self.name = name

class Person():
	def __init__(self,name,place):
		self.name = name
		self.place = place

	def walkDog(self,dog):
		print(self.name,"在",self.place,"溜",dog.name)

xiaomei = Person("小美","朝阳公园")
dog = Dog("旺财")
xiaomei.walkDog(dog)

# 2.小明穿着白色的特步运动鞋在奥林匹克公园跑步
# 类: 人  鞋
# 对象: 小明  运动鞋
# 属性: 白色  特步  名字  运动
# 方法: 跑步  穿
class Shoes():
	def __init__(self,brand,color,type):
		self.brand = brand
		self.color = color
		self.type = type

class Person():
	def __init__(self,name):
		self.name = name

	def wear(self,shoe):
		print("%s穿着%s%s%s鞋"%(self.name,shoe.color,shoe.brand,shoe.type),end="")
	def run(self):
		self.wear(shoe)
		print("在奥林匹克公园跑步")

xiaoming = Person("小明")
shoe = Shoes("特步","白色","运动")
# xiaoming.wear(shoe)
xiaoming.run()

# 3.赵老师在讲台上讲课，小刚认真的听课做笔记
# 类: 老师  同学
# 对象: 赵老师  小刚
# 属性:
# 方法: 讲课 听课 做笔记
class Teacher():
	def __init__(self,name):
		self.name = name

	def teach(self):
		print(self.name,"在讲台上讲课")

class Student():
	def __init__(self,name):
		self.name = name

	def listen(self):
		print(self.name,"在认真听课")

	def takeNotes(self):
		self.listen()
		print(self.name,"在认真做笔记")

zhaolaoshi = Teacher("赵老师")
xiaogang = Student("小刚")
zhaolaoshi.teach()
xiaogang.takeNotes()

# 4.张阿姨和李阿姨在物美超市买红富士
# 类: 人 ,苹果
# 对象: 张阿姨 李阿姨 红富士
# 方法: 买
# 属性: 阿姨
class Person():
	def __init__(self,name):
		self.name = name
	# @classmethod
	def Buy(self,apple):
		print(self.name,"在物美超市买",apple.kind)

class Apple():
	def __init__(self,kind):
		self.kind = kind

aunt_zhang = Person("张阿姨")
aunt_li = Person("李阿姨")
apple = Apple("红富士")
aunt_zhang.Buy(apple)
aunt_li.Buy(apple)

# 使用构造函数的方式写下面的程序

# 1.定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积
import math
class Circle():
	def __init__(self,point,r):
		self.r = r
		self.point = point
	def perimeter(self):
		return "圆的周长为:",2*math.pi*self.r

	def Area(self):
		return "圆的面积为:",math.pi*self.r**2

class Point():
	def __init__(self,x,y):
		self.x = x
		self.y = y


point = Point(640,600)
circle = Circle(point,20)
print(circle.perimeter())

# 2.李晓在家里开party，向朋友介绍家中的黄色的宠物狗【彩彩】具有两条腿走路的特异功能。
# 类: 人  狗
# 对象: 李晓 彩彩
# 属性: 黄色 宠物狗
# 方法: 开party  介绍  两条腿走路
class Dog():
	def __init__(self,color,kind,name):
		self.color = color
		self.kind = kind
		self.name = name

	def walkingOnTwoLegs(self):
		return "能两条腿走路"

class Person():
	def __init__(self,name):
		self.name = name

	def HeldaParty(self):
		print(self.name,"在家开party")

	def Introduce(self,dog):
		print("向朋友介绍家中的",dog.color,"的",dog.kind,dog.name,"具有",dog.walkingOnTwoLegs(),"的特异功能")

dog = Dog("黄色","宠物狗","彩彩")
lixiao = Person("李晓")
# dog.walkingOnTwoLegs()
lixiao.HeldaParty()
lixiao.Introduce(dog)

# 3.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
# 类: 人  猪
# 对象: 王梅  笨笨
# 属性: 荷兰  宠物猪  笨笨
# 方法: 哭 贴 跑丢
class Person():
	def __init__(self,name):
		self.name = name

	def Cry(self):
		return "哭着"

	def Paste(self):
		print(self.name,"家的",pig.Run(),"她",self.Cry(),"贴寻猪启示")

class Pig():
	def __init__(self,name,breed,kind):
		self.name = name
		self.breed = breed      # 品种
		self.kind  = kind

	def Run(self):
		return "%s%s%s跑丢了"%(self.breed,self.kind,[self.name])

wangmei = Person("王梅")
pig = Pig("笨笨","荷兰","宠物猪")
# pig.Run()
# wangmei.Cry()
wangmei.Paste()

# 4.富二代张三向女朋友李四介绍自己的新跑车：白色的宾利
# 类: 人  车
# 对象: 张三  李四  宾利
# 属性: 富二代  跑车 白色
# 方法: 介绍
class Car():
	def __init__(self,brand,color,value):
		self.brand = brand        # 品牌
		self.color = color
		self.value = value        # 价值

class Person():
	def __init__(self,name,kind):
		self.name = name
		self.kind = kind

	def Introduce(self,car,girlfriend):
		print(self.kind,self.name,"向女朋友",girlfriend.name,"介绍自己的",car.value,":",car.color,car.brand)
zhangsan = Person("张三","富二代")
lisi = Person("李四","穷逼")
car = Car("宾利","白色","新跑车")
zhangsan.Introduce(car,lisi)
