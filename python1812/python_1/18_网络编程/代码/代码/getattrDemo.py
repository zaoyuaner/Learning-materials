#xxxxattr

#1.getattr
class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.age = age

    def show(self):
        print("show")

    @classmethod
    def func(cls):
        print("func")


#创建一个Person对象
p = Person("张三",10)
#print(p.name)
print(p.age)

#问题：已知字符串"age",获取10
#方式一
b = "age"
if b == "age":
    print(p.age)

#方式二
print(p.__dict__)
str = "age"
print(p.__dict__[str])

#方式三
"""
getattr(object,name,default) 获取某个对象的某个属性对应的值
object：对象
name：对应属性的字段名，使用字符串表示
default：如果指定字段不存在，则一个返回一个默认值
"""
value1 = getattr(p,"age","hello")
print(value1)

#获取成员方法
result1 = getattr(p,"show")
print(result1)

#获取类方法
result2 = getattr(Person,"func")
print(result2)


#2.hasattr    isxxx:判断一个指定的对象中是否有指定的成员
print(hasattr(p,"score"))

#3.setattr:给指定字段进行赋值
setattr(p,"age",30)

#4.delattr:删除指定字段
#del 变量名
delattr(p,"age")




