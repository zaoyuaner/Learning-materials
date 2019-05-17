# extends 继承: 1.将代码最大程度的复用 2.使逻辑更清晰 3.子类继承父类

# 将几个类相同的属性和方法抽取出来做成父类!

# 做游戏
# 伪随机算法: 30%暴击  3下暴击一次
# 非线性叠加: 20%闪避  ,带5件会是100%?  不会,就是非线性叠加!
# 碰撞检测:

# class Person(object):         # 不写的话默认,为object
# 	pass
#
# print( object)           # <class 'object'>  python中,object是所有类的祖先


# 父类(超类,根类,基类)
class Animal(object):     # 动物类
	def __init__(self,name,weight):
		self.weight = weight
		self.name = name

	def eat(self):
		print("吃")
	def sleep(self):
		print("睡觉")

# 猫类 (子类,派生类)     # 子类自动拥有父类所有的属性和方法
class Cat(Animal):            # 猫继承至动物类
	def __init__(self,name,weight,age):
		# self.name = name
		# self.weight = weight        # 因为父类已经接收过,所以这段代码不用重复写

		# python2的标准语法调用父类的构造函数
		# super(Cat, self).__init__(name,weight)

		# python3的简写
		super().__init__(name,weight)

		# 另外一种写法,多一个self. 类名.__init__(self,属性,属性)
		Animal.__init__(self,name,weight)

		self.age = age
	# 子类可以有和父类不同的属性和方法
	def huntFish(self):
		print("猫会摸鱼")

tom = Cat("tom",10,2)    # 可以调用父类的构造函数,来进行对象的初始化
print(tom.name)
print(tom.weight)
tom.eat()
tom.sleep()
print(tom.age)
tom.huntFish()

# 狗类

# class Dog(Animal):
# 	def __init__(self,name,color):      # 少了父类的weight, 这种最好不要继承,单独写! 继承就要一样的
# 		self.name = name
# 		self.color = color
#
# d = Dog("京巴","白色")

class Dog(Animal):
	def __init__(self,name,weight,color):
		Animal.__init__(self,name,weight)
		self.color = color

	def bark(self):
		print("狗吠")

	def eat(self):                 # 如果子类方法和父类重名,那么会重写
		pass


d = Dog("京巴",30,"白色")
print(d.color)
print(d.name)
print(d.weight)
d.bark()              # 自己特有的方法
d.eat()               # 父类的方法
d.sleep()


# 子类可以使用父类的属性和方法, 但是父类不能使用子类的特有的属性和方法

# .slots属性能否应用在子类中
# 结论：在父类中定义slots属性限制属性的定义，子类中是无法使用，除非在子类中添加自己的限制
# __slots__  不会被继承到子类

# 继承的特点：    缺点: 耦合性!   如果用get set修饰后  私有属性可以继承
#
# 	a.子类对象可以直接访问父类中非私有化的属性
#
#   ​b.子类对象可以调用父类中非私有化的成员方法
#
#  ​	c.父类对象不能访问或者调用子类 中任意的内容