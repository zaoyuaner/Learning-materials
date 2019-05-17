"""
1.设计一个Person，包含姓名、年龄和性别三个私有对象属性，另外Person类还包含males和females两个私有类属性，用来记录男生和女生的数量，可以通过number_male和number_female两个公有类方法获取males和females两个私有类属性的值。自己完成Person类的设计，然后实例化多个Person的对象，分别统计男女的人数
"""
# class Person:
#     __males = 0  # 男生数量
#     __females = 0  # 女生数量
#     def __init__(self,name,age,sex):
#         self.__name = name
#         self.__age = age
#
#         if sex in ['男','m']:
#             self.__sex = 'm'
#             Person.__males += 1
#         else:
#             self.__sex = 'w'
#             Person.__females += 1
#
#     def __del__(self):
#         if self.__sex == 'm':
#             Person.__males -= 1
#         else:
#             Person.__females -= 1
#     @classmethod
#     def number_male(cls):
#         return cls.__males
#     @classmethod
#     def number_female(cls):
#         return cls.__females
#
# if __name__ == '__main__':
#     p1 = Person('test1',20,'m')
#     p2 = Person('test1',20,'m')
#     p3 = Person('test1',20,'w')
#     p4 = Person('test1',20,'m')
#     p5 = Person('test1',20,'w')
#     p6 = Person('test1',20,'w')
#     del p6
#     print(Person.number_male(),Person.number_female())

"""
2.编写一个简单的工资管理程序,系统可以管理以下四类人：工人（worker）、销售员(salesman)、经理(manager)、销售经理（salemanger）。所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
  1）工人：工资计算法方法为工作小时数*时薪，另外具有设置工作小时数，时薪的方法，具有工作小时数和时薪的属性。
  2）销售员：工资计算方法为销售额*提成比例，另外具有设置销售额，提成比例的函数，具有销售额和提成比例的属性。
  3）经理：工资计算方法为固定月薪，另外具有设置固定月薪的函数，具有固定月薪的属性
  4)销售经理：工资计算方法为销售额*提成比例+固定月薪。
请根据以上要求设计合理的类，完成以下功能：
   1）添加所有类型的人员
   2）计算月薪
   3）按从大到小的顺序显示所有人工资情况

"""
class Employee:
    """
    员工类，抽象父类
    """
    def __init__(self,eno,ename):
        self.__eno = eno            # 工号
        self.__ename = ename
        # self.__esalary = 0
    def __str__(self):
        return "姓名：{}  工资：{}".format(self.__ename,self.esalary)
    @property
    def eno(self):
        return self.__eno
    @property
    def ename(self):
        return self.__ename
    @property
    def esalary(self):
        return self.__esalary
    @esalary.setter
    def esalary(self,num):
        self.__esalary = num
    @ename.setter
    def ename(self,name):
        self.__ename = name

    def calculateSalary(self):
        """
        计算工资，在子类实现
        :return:
        """
        pass
# worker
class Worker(Employee):
    def __init__(self,eno,ename,hours,wage):
        super(Worker,self).__init__(eno,ename)  # 调用父类的构造函数初始化继承自父类的属性
        self.__hours = hours
        self.__wage = wage

    def calculateSalary(self):  # 计算工资
        self.esalary = self.__hours * self.__wage
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self,num):
        if num < 0:
            self.__hours = 0
        else:
            self.__hours = num

# 销售员
class Saler(Employee):
    def __init__(self,eno,ename,sales,rate):
        Employee.__init__(self,eno,ename)
        self.__sales = sales
        self.__rate = rate

    def calculateSalary(self):
        self.esalary = self.__sales * self.__rate
    @property
    def sales(self):
        return self.__sales
    @property
    def rate(self):
        return self.__rate
# 经理
class Manager(Employee):
    def __init__(self,eno,ename,monthSalary):
        super(Manager,self).__init__(eno,ename)
        self.__monthSalary = monthSalary

    def calculateSalary(self):
        self.esalary = self.__monthSalary
    @property
    def monthSalary(self):
        return self.__monthSalary

# 销售经理
class SaleManager(Saler,Manager):
    def __init__(self,eno,ename,monthSalary,sales,rate):
        Saler.__init__(self,eno,ename,sales,rate)
        Manager.__init__(self,eno,ename,monthSalary)

    def calculateSalary(self):
        self.esalary = self.monthSalary + self.sales * self.rate

# 工资管理类   不用实例化对象，直接调用类方法
class SalaryManage:
    empList = []  # 员工列表
    @classmethod
    def addEmpolyee(cls,emp):  # 增加员工
        cls.empList.append(emp)

    @classmethod
    def compute(cls):  # 计算月薪
        for emp in cls.empList:
            emp.calculateSalary()

    @classmethod
    def sortSalary(cls):
        cls.empList.sort(key=lambda emp:emp.esalary)

    @classmethod
    def show(cls):
        for emp in cls.empList:
            print(emp)

if __name__ == '__main__':
    # res = SaleManager(4, '张译文', 10000, 200000, 0.05)
    # res.calculateSalary()
    # print(res.__dict__)
    SalaryManage.addEmpolyee(Worker(1,'龙周',22*8,200))
    SalaryManage.addEmpolyee(Saler(2,'罗成',1000000,0.05))
    SalaryManage.addEmpolyee(Manager(3,'徐明林',20000))
    SalaryManage.addEmpolyee(SaleManager(4,'张译文',10000,200000,0.05))

    SalaryManage.compute()
    SalaryManage.sortSalary()
    SalaryManage.show()
