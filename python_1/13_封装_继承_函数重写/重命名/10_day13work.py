#
# 1.利用封装和继承的特性完成如下操作：
# 小学生：elementary school 中学生: middle school   大学生:university student
#       属性：                 属性:                     属性:
#           姓名                   姓名                      姓名
#           学号                   学号                      学号
#           年龄                   年龄                      年龄
#           性别                   性别                      性别
#       行为：                 行为:                     行为:
#           学习                   学习                      学习
#           打架                   谈恋爱                    打游戏
# 测试类中：
#        创建小学生对象
#               调用学习的方法
#               打印内容为： xx
#               学习的内容为：语文 数学 英语
#        创建中学生对象
#               调用学习的方法
#               打印内容为：xx
#               学习的内容为：语数外 生物化 史地政
#        创建大学生对象
#               调用学习的方法：
#               打印内容为： 逃课中。。。。。。
class Students():
	def __init__(self,name,stu_number,age,gender):
		self.name = name
		self.stu_number = stu_number
		self.age = age
		self.gender = gender

	def Study(self,*args):
		print("学习",args)

class ElementaryStus(Students):
	# def __init__(self,name,stu_number,age,gender):
	# 	super().__init__(name,stu_number,age,gender)
	def fight(self):
		print("打架")

xiaoming = ElementaryStus("小明",20123212,8,"男")
xiaoming.fight()
xiaoming.Study("语文","数学","英语")

class MiddleStus(Students):
	# def __init__(self,name,stu_number,age,gender):
	# 	Students.__init__(self,name,stu_number,age,gender)
	def fallInLove(self):
		print("谈恋爱")
xiaoli = MiddleStus("小丽",20331231,13,"女")
xiaoli.Study("语数外", "生物化" ,"史地政")
xiaoli.fallInLove()

class UniversityStus(Students):
	# def __init__(self,name,stu_number,age,gender):
	# 	super().__init__(name,stu_number,age,gender)
	def playGames(self):
		print("打游戏")
xiaohua = UniversityStus("小华",20441321,20,"男")
xiaohua.playGames()
xiaohua.Study("逃课中........")
print(xiaohua.name)
print(xiaoli.stu_number)

# 2. 主人杨夫人向客人李小姐介绍自己家的宠物狗和宠物猫
#           宠物狗：
#               昵称是：贝贝
#               年龄是：2
#               性别：雌
#               会两条腿行走的才艺
#           宠物猫
#               昵称是：花花
#               年龄是: 1
#               性别是：雄
#               会装死的才艺
class Person():
	def __init__(self,name):
		self.name = name

	def Introduce(self,dog,cat,per):
		print("向客人",per.name,"介绍自己家的宠物狗","昵称是:",dog.name,"年龄是:",dog.age,"性别:",dog.gender,"会",dog.walk(),"的才艺")
		print("向客人",per.name,"介绍自己家的宠物猫","昵称是:",cat.name,"年龄是:",cat.age,"性别:",cat.gender,"会",cat.deathMimicry(),"的才艺")

class Animals():
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

class Dog(Animals):
	def walk(self):
		return "两条腿走路"

class Cat(Animals):
	def deathMimicry(self):
		return "装死"

beibei = Dog("贝贝",2,"雌")
huahua = Cat("花花",1,"雄")
yang = Person("杨夫人")
li = Person("李小姐")
yang.Introduce(beibei,huahua,li)

# 3.学生类：姓名、年龄、学号、成绩
#   班级类：班级名称、学生列表
#           显示所有学生
#           根据学号查找学生
#           添加一个学生
#           删除一个学生（学生对象、学号）
#           根据学号升序排序
#           根据成绩降序排序
class Student(object):
	def __init__(self,name,age,num,score):
		self.name = name
		self.age = age
		self.num = num
		self.score = score
	def __str__(self):
		return "姓名:%s,年龄:%d,学号:%d,成绩:%d"%(self.name,self.age,self.num,self.score)

class Class():               # 丢学生对象！
	def __init__(self,ClassName,stuList):
		self.ClassName = ClassName
		self.stuList = stuList

	# 显示所有学生
	def showAllStudent(self):
		# 遍历学生列表,打印所有的学生
		for item in self.stuList:
			print(item)

	# 添加一个学生
	def addStudent(self,stu):               # 直接加对象
		if stu not in self.stuList:         # 避免重复添加
			self.stuList.append(stu)

	# 根据学号查找学生
	def findStu(self,num):      # 找到了返回下标,找不到返回-1
		for index,item in enumerate(self.stuList):
			if item.num == num:
				return index
		return -1

	# 删除一个学生(姓名,学号)      # arg可能是学号,也可能是一个学生对象
	def Del1(self,arg):
		if type(arg) == int:
			# 遍历学生列表,找到对应的学生删除
			for stu in self.stuList:
				if stu.num == arg:
					self.stuList.remove(stu)
		else:
			if arg in self.stuList:          # 如果对象存在列表中才删
				# 如果是学生对象,那么就直接删除
				self.stuList.remove(arg)

	# 根据学号升序排序
	def numSort1(self):
		self.stuList.sort(key = lambda stu:stu.num)        # stu 是stuList中的每个元素

	# 根据成绩降序排序
	def scoreSort2(self):
		self.stuList.sort(key = lambda stu: stu.score ,reverse = True)


stu1 = Student("小明",23,8990,65)
stu2 = Student("小华",22,9000,79)
stu3 = Student("小米",20,9110,100)
stu4 =Student("易",22,9910,90)
stu5 = Student("徐",24,9120,99)
stu6 = Student("王",19,9203,70)

class1 = Class("python1812",[])
class1.addStudent(stu1)
class1.addStudent(stu2)
class1.addStudent(stu3)
class1.addStudent(stu4)
class1.addStudent(stu5)
class1.addStudent(stu6)

# class1.Del1(9000)
# class1.Del1(xu)

print( class1.findStu(9110))
class1.numSort1()
class1.showAllStudent()
print("------------")
class1.scoreSort2()
class1.showAllStudent()




