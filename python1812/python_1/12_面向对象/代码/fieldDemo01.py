class Person(object):
    #1.定义位置
    #类属性：直接定义在类中
    name = "abc"
    age = 0

    def __init__(self,name):
        #实例属性：定义在构造函数中
        self.name = name


#2.访问方式
print(Person.name)  #类属性：类名.属性 或者 对象.属性

p = Person("hello")
print(p.name)   #实例属性：对象.属性

#3.优先级不同：实例属性的优先级高于类属性
print(p.name)   #hello

#4.不同对象的类属性在内存中是不是同一块空间？----->不是
p1 = Person("小白")
p2 = Person("小红")
print(p1.age)
print(p2.age)
p1.age = 33
print(p1.age)
print(p2.age)
print(id(p1.age))
print(id(p2.age))
"""
0
0
33
0
1420404832
1420403776
"""

#注意：尽量避免类属性和实例属性的重名

#删除属性【类属性，实例属性】
del p1.age




