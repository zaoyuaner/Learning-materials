
print()
"""
format方法
"""
#括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
print("我叫{},今年{}!".format("张三",22))

#括号中的数字用于指向传入对象在 format() 中的位置
print("我叫{0},今年{1}!".format("张三",22))
print("我叫{1},今年{0}!".format("张三",22))
#
#在format()中使用关键字参数,它们的值会指向使用该名字的参数
print("我叫{name},今年{age}!".format(name="张三",age=22))
print("我叫{name},今年{age}!".format(age=22,name="张三"))

#位置及关键字参数可以任意的结合
print("我叫{0},今年{1},现住{place}!".format("张三",22,place="深圳"))
print("我叫{0},现住{place},今年{1}!".format("张三",22,place="深圳"))
# print("我叫{name},现住{0},今年{1}!".format(name="张三","深圳",22))

#':'和格式标识符可以跟着字段名。可以对值进行更好的格式化
a = 3.1415926
print("a的值为{0:.3f}".format(a))
print("{0:5}---{1:05d}".format("张三",18))


# __call__
# __str__
# __add__
# __repr__
# __iter__
# __next__
# __dict__
#

#
# 2007  iphone
# 2008  iphone3
# 2009  iphone3GS
# 2010  iphone4
# 2011  iphone4S
# 2012  iphone5
# 2013  iphone5S
# ...
#






