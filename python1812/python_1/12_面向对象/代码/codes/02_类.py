# 类 class 类别  : 将相同的事物的共同点抽出来,就成了类   比如: 模具
#                 相同的属性    相同的方法

# 对象: 通过类创建的实例               比如: 通过模具产生的产品
#      属性
#      方法

# 人类:  属性: 身高, 体重, 颜值, 财富
#       方法: 吃, 喝, 玩, 睡
#
# 对象:  小明: 身高: 180cm  体重: 140斤  颜值: 5分  财富:1000元
#             吃, 喝, 玩, 睡, 玩游戏, 敲代码
#
#        小丽: 身高:160cm   体重: 90斤   颜值: 8分  财富: 1000000元
#             吃, 喝, 玩, 睡, 玩游戏, 化妆


# 一个对象其实也可以作为别的对象的类 !  类与对象没有严格区分!

# python中7种数据类型就是7个类! 数字(int.float.True.False).str.list.tuple.dict.set.None

# 实例化:  使用类创建对象的过程
num = 123    # 实例化int类,得到num对象

str1 = "wes"   # 实例化str类,得到str1对象


# 一般其他编程语言中,数字不会当做对象处理,但是python会

class Person(): # 类名的定义规则,只能是字母,数字,下划线,遵循驼峰原则
# 类属性                # 首字母必须大写!(约定)
	name = "231"
	age = 0

	# 对象属性
	def __init__(self,name,age):    # 实例化对象时,才能访问
		self.name = name
		self.age = age

	# 对象方法
	def show(self):      # self指,当前对象,会代表等下实例产生的对象
		print("hello")

# 类方法(装饰器)
	@classmethod
	def myPrint(cls):
		print("6666")

p = Person("yi",12)             # 实例化Person,得到p对象  self -> p
p.show()                 # 使用对象所有拥有的方法
print( p.name )
print( p.age )
print( Person.name )
print( Person.age )

# Person.show()            # 崩溃! 对象方法只能用对象来调用,不能用类调用

# 类属性： 直接写在类中, 可以用对象,和类名来调用, 是所有对象共有成员
# 对象属性： 在构造函数__int__中声明, 必须实例化才能访问属性
# 类方法： 通过类名直接调用的方法   @classmethod    也可以用对象来调用  p.myPrint()
# 对象方法： 通过对象调用的方法

# 类方法   可以用对象,和类名来调用
Person.myPrint()
p.myPrint()
