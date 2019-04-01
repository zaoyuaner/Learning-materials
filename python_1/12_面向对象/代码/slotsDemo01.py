from  types import MethodType


class Person(object):
    #__slots__ = ("name","age")
    pass


#1.动态添加属性
per = Person()
str = "fjsgh"
per.name = str

#2.动态添加方法
def say(self):
    print("fhsj")
"""
per.test = say
per.test(per)
"""

#弊端：违背了普通函数定义
#解决方案：MethodType类，存在于types模块下

#类似于偏函数
#参数：函数名，对象
#作用：在现有函数的基础上生成了一个对象【新的函数】，赋值给成员变量，则认为给对象添加了一个成员方法
per.test = MethodType(say,per)
per.test()



