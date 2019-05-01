# python是一门弱类型的编程语言，它的变量类型需要通过值来倒推
# python中，变量一定要赋值

# 七种基本数据类型：
# 1.数字   number:包含整数，浮点数，复数，布尔值（False，True）
a = 10    # 赋值
print(type(a)) # type() 求出括号中参数的类型  int

b = 5.23
print(type(b))   # float

c = 2+3j
print(type(c))   # complex

d = True
print(type(d))   # bool 布尔值
print(True == 1) # 1,非0就代表True ， 0代表False。在python2中，没有True和False,用1和0代替。
print(False == 0)


# 2.字符串 str , 单双引号括起来的字符。双引号不能嵌套双引号，单引号不能嵌套单引号。
string1 = "hello world"
string2 = "    zhangsan"  # 空格算长度
string3 = "小米说：'你好'" # 单双嵌套
string4 = "小明说：\"你好\""  # \" 转义字符，让这个引号正常输出
string5 = "\\"    # 打印\需要两个
print(string4)
print(type(string5))

# 3.列表  list
mylist = ["a","b","c"]
print(type(mylist))

# 4.元组  tuple  不可改变
myTuple = (1,2,3,4,5)
print(myTuple)
print(myTuple,type(myTuple))

# 5.字典  dict  里面存储的是键值对   键：值
myDic = {"name":"xiaoming","age":"20"}
print(myDic["name"])  #通过name这个键，取值
print(type(myDic))

# 6.集合  set   去重。如何对列表去重，转成集合！
mySet = set([1,2,3,4,5,5,5,5,5,5]) # 通过列表创建集合
mySet2 = {1,2,3,4,5,5,5,6,7}       # 通过大括号创建集合
mySet3 = {}                        # 这种产生并不是空集合，而是空字典
set2 = set()                       # 空集合
print(mySet)
print(mySet2)
print(mySet,type(mySet))           # ,代表空格

list1 = [1,2,3,3,4,4,5,6,3]
set1 = set(list1)       # 将参数转集合
list2 = list(set1)      # 将参数转列表
print(list2)            # 去重

# 7.空    None    一般为对象设置初值
