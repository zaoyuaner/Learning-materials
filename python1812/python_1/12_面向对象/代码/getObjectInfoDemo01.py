#1.type() :判断一个对象所属的类型
num = 10
print(type(num))
print(type("hello"))

class Check(object):
    pass
c = Check()
print(type(c))

#使用==判断type返回的结果
print(type(12) == type(57))  #True
print(type(12) == type("57"))  #False

#使用type返回的结果和数据类型直接判断
print(type(12) == int)

#2.isintance()  :判断一个对象是否属于某种指定的数据类型
#自定义的类中
class Dog(object):
    pass

d = Dog()
print(isinstance(d,Dog))
print(isinstance([1,2,4],list))

#特殊用法：可以判断一个对象是否属于多种数据类型中的某一种
print(isinstance([1,2,4],(tuple,list)))

#3.dir()  :列出指定对象中所包含的所有的内容【成员变量，成员方法】
dict = {}
print(dir(dict))

print(dir("abc"))

print(dir(d))




