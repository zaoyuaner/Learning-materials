# 原因是python的内存管理, 缓存了 - 5 - 256
# is
# a=1000
# b=1000
# print(id(a),id(b))
# print(a is b)
#
# a=100
# b=100
# print(id(a),id(b))
# print(a is b)

# ==
# __eq__()
#

# type()
# isinstance() : 也可以检测是否属于某个父类的子类对象
# def test():
#     pass
#
# test.xx = 1
# test.xx = 2
# print(test.__dict__)



# *****************************************************
# def deco(fun):
#     fun.x=1
#     fun.y=2
#     return fun
#
# @deco    # fun=deco(fun)
# def fun():
#     print("=====> fun")
#
# fun()
# print(fun.__dict__)

# *****************************************************

# ①hasattr(obj,name)------> 判断obj这个对象是否有name属性或者name这个方法
#
# ②setattr(obj,attr,v) --------》 给obj设置一个attr属性值为v(给对象添加修改值) 注:attr可为属性or方法
#
# ③getattr(obj,attr)-----------> 获取obj的attr属性,attr可以为一个方法, 如果attr不存在则报错
#
# ④delattr(obj,attr)------->  删除obj 的attr属性 如果删除的是一个方法那么这个方法在类的内部是会


# class Foo():
#     """xxxxxxxxxx
#     """
#     st='abc'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def run(self):
#         print("-------> run")
#
#     def fun(self):
#         print("-----> from the fun")

# print(Foo.__dict__)

# class Bar(Foo):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#
#     def run(self):
#         print("-------> Bar run")
#
#     def fun(self):
#         print("-----> Bar from the fun")
#
# print(Foo.__dict__)
# print(Foo.__module__)  # 模块名


# class A:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print("------run")
#
#     def fun1(self):
#         print("----->fun1")
#
#
# def obj_bind():
#     print("------boind Obj")
#
#
# a = A('alex', 181)
# getattr  得到属性的值或方法的地址 不存在则报错
# print(getattr(a, 'name'))  # 输出 ----------> alex
# print(getattr(a, 'xx'))  # 输出 ----------> <bound method A.fun1 of <__main__.A object at 0x0000016BBF9F6470>>
# setattr 给对象设置属性或绑定方法
# setattr(a, 'gender', 'male')
# print(a.gender)  # 结果 male
# setattr(a, 'name', 'yuanhao')
# print(a.name)  # 结果 yuanhao
# setattr(a, 'obj_bind', obj_bind)
# print(a.__dict__)
# print(a.obj_bind)  # 结果  <function obj_bind at 0x0000019EA5F4B8C8>
# # hasattr 返回一个布尔值 判断该对象是否存在
# print(hasattr(a, 'name'))  # 结果 True
# print(hasattr(a, 'obj_bind'))  # 结果 True
# # delattr 删除一个对象的属性或方法 没有返回值 删除不存在则报错
# print(delattr(a, 'name'))
# print(delattr(a, 'gender'))
# print(delattr(a, 'fun1'))  # 结果 会报错 不能删除方法，除非是在对象实例化之后绑上去的
# print(delattr(a, 'obj_bind'))


# 列表生成式
a = [i for i in range(1,10)]

# 字典生成式
b = {i:i+1 for i in range(1,10)}
print(b)

# 集合生成式
c = {i**2 for i in range(1,10)}
print(c)

