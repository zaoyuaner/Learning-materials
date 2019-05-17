# 匿名函数: lambda 没有名字的函数,是一个使用":"冒号的表达式.不用 def+函数名
result = lambda num1,num2:num1+num2         # 要用一个变量接收
#                  参数      返回值

print(result(20,30))           # 50
# 等同于
# def add(num1,num2):
# 	return num1+num2

result = lambda x,y:x**2 + y**2
print(result(2,3))
print(result(y=4,x=3))

result = lambda x=0,y=0:x*y       # 默认关键字参数
print(result(2,3))
print(result())

# 按照列表中字符串的长度进行排序
list1 = ["king","key","z","hello"]
#   使用系统函数
list1.sort(key=len)     # 让list1中的每个元素都来调用len,通过这个返回值大小,来排序
print(list1)
#   使用匿名函数
list1.sort(key= lambda str:len(str))   # str是列表中的每个元素,返回每个元素的长度排序
print(list1)

# 求字典中,值最大的键值对
dict1 = {"name":20,"age":40,"money":33}
# for key in dict1
# print( max(dict1))     # 直接使用max,那么获取的是最大的key,ASCII码

result = max(dict1,key= lambda k:dict1[k])  # 遍历字典是使用的key,得到最大的键
                 # lambda 传入一个键,返回一个值,再通过这个值比较大小,最后返回最大的键
print("最大的键是:",result,"最大的值是:",dict1[result])

# 将字典,按照值的大小排序
result = sorted(dict1,key= lambda k:dict1[k])
print(result)          # ['name', 'money', 'age']  返回一个已排序列表