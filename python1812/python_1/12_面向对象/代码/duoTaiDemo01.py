#父类
class Animal(object):
    pass

#子类
class Dog(Animal):
    pass

class Cat(Animal):
    pass

#定义变量
a = []   #a是list类型
b = Animal()  #b是Animal类型
c = Cat()  #c是Cat类型

#isinstance():判断一个对象是否属于某种类型【系统还是自定义的类型】
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Cat))

print(isinstance(c,Animal))  #True

print(isinstance(b,Dog))   #False

#结论：子类对象可以是父类类型，但是，父类的对象不能是子类类型




