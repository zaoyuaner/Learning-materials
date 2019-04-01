"""
map(function,iterable)
function:函数
iterable：可迭代对象
作用：将传入的函数依次作用于可迭代对象中的每一个元素，并把结果【Iterator】返回
"""
#需求1：给一个已知列表中的元素求平方
def square(x):
    return x ** 2
list1 = [1,2,3,4,5]
result1 = map(square,list1)
#注意:map是一个类，表示一种数据类型，集合或者序列，使用类似于list，tuple，set
print(result1)   #<map object at 0x000001EE25431DA0>
print(type(result1))   #<class 'map'>
print(list(result1))  #[1, 4, 9, 16, 25]

result2 = map(lambda x:x ** 2,list1)
print(list(result2))

#str = 10

#需求2：将整型元素的列表转换为字符串元素的列表
#举例：[1,2,3,4]------>["1","2","3","4"]
#str(1) ---- >字符串1
#注意：在使用系统函数之前，最好不要出现同名的变量
result3 = map(str,[1,2,3,4])
print(list(result3))


#需求3：已知两个整型列表，将两个列表中相同位置的元素相加，得到一个新的列表
def add(x,y):
    return  x  + y
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

result4 = map(add,l1,l2)
print(list(result4))


