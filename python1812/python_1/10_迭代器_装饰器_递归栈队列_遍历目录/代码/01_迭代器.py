# Iterable: 可迭代对象 :能够用for in遍历的就是可迭代对象

# Iterator: 迭代器 :  能够用for in遍历,并且能够用next()遍历  称之为迭代器
# 目前能称之为迭代器的只有生成器

# 能够使用next()的,一定能使用forin   ,  使用for in的不一定能使用next()

# generator: 生成器 : 能用for in,能用next()

# 可迭代对象不一定是迭代器,使用iter(),可以将可迭代对象转为迭代器....生成器是迭代器

# list1 = [1,2,3,4]
# next(list1)        # list列表不是迭代器,不能用next

result = (x for x in range(10) )     # 生成器   可以用next(),那么是迭代器
print(result)
print(next(result))

# 判断是不是什么类型的实例
# 判断是是不是什么类的对象
# 判断这个量是不是这个类型  isinstance(对象,类型)   返回布尔值

print(isinstance([],list))    # True
print(isinstance("3.23",float))    # false

from  collections  import  Iterator  # 迭代器需要导入才能进行比较,能用for in,next()
print(isinstance((x for x in range(10)),Iterator))    # True
print(isinstance([],Iterator))            # False
print(isinstance((),Iterator))            # False
print(isinstance({},Iterator))            # False
print(isinstance("hello",Iterator))       # False
print(isinstance(1223,Iterator))          # False   除了生成器,全部不是迭代器
print(isinstance(None,Iterator))          # False

from  collections import  Iterable    # 可迭代对象 也需要导入 能用for in遍历
print(isinstance([],Iterable))            # True
print(isinstance((),Iterable))            # True
print(isinstance({},Iterable))            # True
print(isinstance("hello",Iterable))       # True
print(isinstance(1223,Iterable))       # False   数字不是可迭代对象
print(isinstance(None,Iterable))       # False   None空类型不是可迭代对象


# 为什么使用生成器: 因为如果使用生成器,那么会拿到所有结果,会占用很大的内存空间
# 使用生成器,可以通过next(),一次只拿一个,不会占用那么多空间

# 使用iter()  将可迭代对象,转为迭代器. 需要导入函数Iterator
result = iter([1,2,3,4])

# 迭代器可以next
print(next(result))     # 1

print("------")
# 迭代器可以用for
for i in result:
	print(i)            # 2 3 4 , 1已经被next了!