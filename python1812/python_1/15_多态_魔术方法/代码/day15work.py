"""1.设计一个Person，包含姓名、年龄和性别三个私有对象属性，
另外Person类还包含males和females两个私有类属性，用来记录男生和女生的数量，
可以通过number_male和number_female两个公有类方法获取males和females两个私有类属性的值。
自己完成Person类的设计，然后实例化多个Person的对象，分别统计男女的人数
"""
class Person(object):
	__males = 0
	__females = 0

	def __init__(self, name, age, gender):
		# self.__name = name
		# self.__age = age
		self.__gender = gender
		if gender == "男":
			Person.__males += 1
		else:
			Person.__females += 1

	def number_male(self):
		print("男性人数为:", Person.__males)

	def number_female(self):
		print("女性人数为:", Person.__females)


p1 = Person("易", 24, "男")
p2 = Person("小明", 20, "男")
p3 = Person("莉莉", 21, "女")
p4 = Person("小华", 23, "男")
p5 = Person("大熊", 21, "男")
p6 = Person("小叮当", 20, "女")
p7 = Person("大叮当", 20, "女")
p8 = Person("小三", 22, "女")
p9 = Person("大四", 20, "男")

# Person.number_male(object)
# Person.number_female(object)

p1.number_male()
p1.number_female()


# 2.编写一个简单的工资管理程序,系统可以管理以下四类人：工人（worker）、销售员(salesman)、经理(manager)、销售经理（salemanger）。
#   所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
#   1）工人：工资计算法方法为工作小时数*时薪，另外具有设置工作小时数，时薪的方法，具有工作小时数和时薪的属性。
#   2）销售员：工资计算方法为销售额*提成比例，另外具有设置销售额，提成比例的函数，具有销售额和提成比例的属性。
#   3）经理：工资计算方法为固定月薪，另外具有设置固定月薪的函数，具有固定月薪的属性
#   4)销售经理：工资计算方法为销售额*提成比例+固定月薪。
# 请根据以上要求设计合理的类，完成以下功能：
#    1）添加所有类型的人员
#    2）计算月薪
#    3）按从大到小的顺序显示所有人工资情况      # 工资管理类

class Company(object):

	def __init__(self, name, num, salary):
		self.name = name
		self.num = num
		self.salary = salary

	@property
	def getName(self):  # 获取私有姓名
		return self.name

	@getName.setter     # 设置私有姓名
	def setName(self, myname):
		self.name = myname

	@property           # 获取私有员工号
	def getNum(self):
		return self.num

	def getSalary(self, hours, wage):  # 计算工资,子类重写
		"""
		:param hours:
		:param wage:
		:return:
		"""
		pass



class Worker(Company):

	def __init__(self, worker_num, worker_name, worker_salary, worker_wage, worker_hours):
		super(Worker, self).__init__(worker_num, worker_name, worker_salary)
		self.__worker_wage = worker_wage
		self.__worker_hours = worker_hours

	def getSalary(self, hours, wage):  # 计算工资
		Salary = hours * wage
		print(Salary)


A = Worker(1233, "易", None, 23, 100)
A.getSalary(23, 100)  # 2300
print(A.getName)  # 易
A.setName = "易志康"
print(A.getName)  # 易志康


class Salesman(Company):
	def __init__(self, salesman_num, salesman_name, salesman_salary, salesman_sale, salesman_rate):
		super(Salesman, self).__init__(salesman_num, salesman_name, salesman_salary)
		self.__salesman_sale = salesman_sale
		self.__salesman_rate = salesman_rate

	@property
	def getSalesman_sale(self):
		return self.__salesman_sale

	@getSalesman_sale.setter
	def setSalesman_sale(self, mysale):  # 设置销售额
		self.__salesman_sale = mysale

	@property
	def getSalesman_rate(self):
		return self.__salesman_rate

	@getSalesman_rate.setter
	def setSalesman_rate(self, myrate):  # 设置提成比例
		self.__salesman_rate = myrate


B = Salesman(1190, "大佬", None, 12000, 0.6)
print(B.getSalesman_sale)  # 12000
B.getSalary(12000, 0.6)  # 7200
B.setSalesman_rate = 0.9
B.setSalesman_sale = 20000
B.getSalary(B.setSalesman_sale, B.setSalesman_rate)  # 18000


class Manager(Company):
	def __init__(self, manager_num, manager_name, manager_salary):
		self.__manager_num = manager_num
		self.__manager_name = manager_name
		self.__manager_salary = manager_salary  # 固定工资

	@property
	def getManager_salary(self):  # 获取月薪
		return self.__manager_salary

	@getManager_salary.setter  # 设置月薪
	def setmanager_salary(self, mysalary):
		self.__manager_salary = mysalary


C = Manager(1122, "小明", 10000)
print(C.getManager_salary)  # 10000
C.setmanager_salary = 20000
print(C.getManager_salary)  # 20000


class Salemanger(Company):
	def __init__(self, salemanger_num, salemanger_name, salemanger_salary, salemanger_sale, salemanger_rate):
		self.__manager_sale = salemanger_sale
		self.__salemanger_num = salemanger_num
		self.__salemanger_name = salemanger_name
		self.__salemanger_rate = salemanger_rate
		self.__salemanger_salary = salemanger_salary

	def getSalary(self):  # 计算工资
		Salary = self.__manager_sale * self.__salemanger_rate + self.__salemanger_salary
		print(Salary)


D = Salemanger(1209, "周杰伦", 50000, 0.9, 20000)
D.getSalary()

# 3) 显示按照从大到小显示所有员工工资情况
# 	@classmethod
# 	def salarySort(self):
# 		self.com.sort(key=lambda com: com.salary, reverse = True)
