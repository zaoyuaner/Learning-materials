# 高阶函数
# 如果一个函数的参数是另外一个函数，那么这个函数就可以称为高阶函数

# map(function,iterable): 接收两个参数，一个是函数，一个是可迭代对象(Iterable)，map将传入的函数依次
#      作用到序列的每个元素，并把结果作为新的Iterator返回。
a = [1,3,5,9]
def fun(x):
	return x **2
# 需求: 获取一个列表中每个元素的平方,生成一个新的列表
result = map(fun,a)      # 返回可迭代对象
# print(result)
# print(next(result))    # 1
print(list(result))      # 转换成列表

b = ['2','4',9,'10']
def test(x):
	if isinstance(x,str):
		x = int(x)
	return x * 10
result = map(test,b)
print(list(result))       # [20,40,90,100]

# 多个可迭代对象
a = [1,2,3,4,5]
b = [10,20,30]
def test1(x,y):
	"""
	以元素少的为主,多余的元素去除
	:param x: 取第一个可迭代对象的元素
	:param y: 取第二个可迭代对象的元素
	:return:
	"""
	return x + y
result = map(test1,a,b)
print(list(result))          # [11,22,33]

# reduce 累加 functools模块中的一个高阶函数。需要引入functools模块才能使用。
from functools import reduce
# reduce(func, iterable, initializer)
# 参数1：函数，这个函数需要两个参数。
# 参数2：可迭代对象
# 参数3：可选，是默认值
# 需求: 列表除10 再求和
a = [10,20,30,40,50]
def test2(x,y):
	return x + y/10
res = reduce(test2,a,0)   # 初始值为0 x第一个取值为0
"""
(1) 0->x 10->y  res = 1
(2) 1->x 20->y  res = 3
(3) 3->x 30->y  res = 6
(4) 6->x 40->y  res = 10
(5) 10->x 50->y  res = 15

"""
print(res)           # 15

b = ['1','2','3']
res = reduce(lambda x,y: x+y,b)
print(res)           # '123'

# filter(function,iterable) 过滤: 可以对可迭代对象进行过滤，去除不满足条件的元素
# 参数： function 确定是否保留元素，为真保留，为假去除元素,function的值可以None
#        iterable 可迭代对象
# 返回值：一个新的迭代器或迭代对象
a = [10,-9,0,20,99,-23,-3]
# 需求干掉负数,保留正数
res = filter(lambda x:x>0,a)
print(list(res))           # [10, 20, 99]

# 判断回文数
def is_palindrome(x):
	x = str(x)
	y = x[::-1]
	return x == y
res = filter(is_palindrome,range(1,1001))
print(list(res))

# sorted: 用于对有序序列进行排序，生成一个新序列
# sorted(iterable , key=None , reverse=False])
a = [1,22,33,40,12,4]
print(a)
print(sorted(a,reverse = True))

# 复合元素
a = [(1,2,3),(2,3),(3,4,5),(1,9)]
res = sorted(a, key= lambda x:x[0])
print(res)

# 自定义类的对象排序
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __str__(self):
		return self.name + " " + str(self.age)
c = [Person('tom',2),Person('jerry',4),Person('mary',33)]
res = sorted(c,key= lambda x:x.age)
for p in res:
	print(p)
