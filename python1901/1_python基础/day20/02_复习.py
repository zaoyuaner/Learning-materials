''''''
# 前4周内容复习
#
'''
1. 装软件
    Python，PyCharm(IDE), Sublime Text, Notepad++, Hbuilder, HbuilderX(vue)
    VM：虚拟机
    数据库：MySQL，Redis,Mongodb
    ... 
    
2. 计算机基础
    计算机原理： 软件，硬件
            物联网：嵌入式
    
    前端H5
    移动端：iOS,Android
    /后端: Python，Java(企业级开发)，Go(区块链), PHP，C#, C/C++;
    
    进制转换
    原码反码补码（了解）
    
    input,print
    注释： 
        单行： #
        多行： ''' '''， """ """
    
        JSON： '[{"a"：10}, {"b": 20}]',json,key需要使用双引号
    
3. 数据类型
    Boolean, Number, Str, List, Tuple, Dict, Set, None, Bytes
    
4.变量
    定义变量：
        a = 10
        a, b = 10, 20
        a = b = c = 100
        # a = 1, b = 2  # 报错
        a, *b, c = 1, 2, 3, 4
    命名规范：
        1.只能使用字母数字下划线，且不能以数字开头
        2.不能是关键字
            import keyword
            keyword.kwlist()
        3.区分大小
        4.尽量见名知意，多单词情况下：
                1.使用下划线：my_student_name
                2.使用小驼峰: myStudentName
    删除变量
        del name
    
5. 运算符
    一元运算符：del, (位运算)~,^， del name   
    二元运算符：+，-, *,...
    # 三元运算符/三目元算符: ?： python语言没有
    Python: a = 10 if 3>4 else 20

    算术运算符：+ - * / // % 
    比较运算符：> < >= <= == !=
    逻辑运算符：and or not, 注意短路操作
    成员运算符：in  not in
    身份运算符：is  is not
    *位运算符：<<, >>, &, |, ~, ^
    赋值运算符：=, +=， -=， *=...
    
    
6. 分支：IF
    单分支：if
    双分支：if-else
    多分支：if-elif-else
    
7. 循环：for,while
    for: 一般情况都使用for, 在已知遍历次数
    while: 未知遍历次数
    for-else
    while-else

8. List列表
    定义列表: ages = []
    基本操作：
        len: len(ages)
        [index]: ages[index]
        [:]: ages[3:]
        + : ages + ages2
        * : ages * 2
        in : n in ages
    列表的方法：
      增：
        list.append(n) : 追加一个元素
        list.extend([a, b]) ： 追加多个元素
        list.insert(index, n) : 插入元素
      删：
        list.pop(index) : 弹出指定下标的元素
        list.remove(n): 删除指定元素
        list.clear() : 清空列表
        del list[index] :删除指定元素
        del list[3:] : 删除多个元素
        del list: 删除整个列表
      改：
        list[index] = newN
      查：
        print(list[index])
        for n in list:
            pass
        for i in range(len(list)):
            pass 
    排序：
        list.sort() : 升序
        list.sort(reverse=True): 降序
        list.reverse() : 倒序，逆序
        list.sort(key=) ：升序
        newList = sorted(list,key=) : 升序，不改变原列表
        newList = sorted(list, reverse=True,key=) : 降序，不改变原列表
        newList = list(reversed(list)): 倒序,不改变原列表
        
    复制：
        浅拷贝/浅复制：copy
        深拷贝/深复制：deepcopy
    
9. 元组
    定义元组: ages = ()
    基本操作：
        len: len(ages)
        [index]: ages[index]
        [:]: ages[3:]
        + : ages + ages2
        * : ages * 2
        in : n in ages
    元组的方法：
      查：
        print(tuple[index])
        for n in tuple:
            pass
        for i in range(len(tuple)):
            pass 
    排序：
        newList = sorted(tuple,key=) : 升序，不改变原列表
        newList = sorted(tuple, reverse=True,key=) : 降序，不改变原列表
        newList = list(reversed(tuple)): 倒序,不改变原列表
    复制：
        浅拷贝/浅复制：copy
        深拷贝/深复制：deepcopy
   
10. 字典：
    定义字典：d = dict(), d = {}空字典， d={'name':'zs'}
    基本操作：
        len: len(dict)
        in: key in dict
    字典的方法：
        增，改：
            dict[key] = value
        查：
            dict[key] : key不存在会报错
            dict.get(key): 如果不存在会返回None
            dict.get(key, 'default') ：如果不存在会返回默认值
            
            dict.items()
            dict.keys()
            dict.values()
            
            for k in dict:
                pass
            for v in dict.values():
                pass
            for k, v in dict.items():
                pass
            
        删：
            dict.pop(key)
            dict.popitem(): 随机删除一个
            dict.clear() ：清空字典
            del dict[key]
            del dict
    

11. 字符串str
    定义字符串：s = ''
    基本操作：
        len: len(ages)
        [index]: ages[index]
        [:]: ages[3:]
        + : ages + ages2
        * : ages * 2
        in : n in ages
    字符串的方法:
        str.upper()
        str.lower()
        str.title()
        str.capitalize()
        str.swapcase()
        
        str.isupper()
        str.islower()
        str.istitle()
        str.isalpha()
        str.isalnum()
        str.isdigit()
        str.isspace()
        str.isdecimal()
        
        str.center(100)
        str.center(100, "*")
        str.ljust()
        str.rjust()
        
        str.strip() 
        str.lstrip()
        str.rstrip()
        
        str.index()
        str.rindex()
        str.find()
        str.rfind()
        
        str.split(): 拆分
        str.splitlines()
        ''.join(list) : 合并
        str.replace
        
        ord() : 转为ASCII码
        chr() ：转为字符
        
        str.encode() : 编码
        bytes.decode() ： 解码
        
        str.startswith()
        str.endswith()

12.number
    int, float
    int()
    float()
    max()
    min()
    abs()
    sum()
    
    math模块：
        math.sqrt()
        math.pow()
        math.ceil()
        math.floor()
        math.fabs()
        math.sin()
        math.cos()
        math.tan()
        ...
    random模块:
        random.choice(list)
        random.random() : [0,1)
        random.randrange(start, end, step):  [start,end),步数为step
        random.randint(start, end): [start, end]整数
        random.uniform(start, end) : [start, end]小数
        random.shuffle(list): 乱序

13. Boolean
    True : 1
    False : 0

14. 函数
    def fn():
        return 
    参数：
        位置参数(必需参数)，默认参数，关键字参数，不定长参数
        
        def fn(a,b)：
            pass
        
        def fn(a=10):
            pass
        
        def fn(a=10):        
            pass
        fn(a=20)

        def fn(*args, **kwargs):
            print(args)  # ()
            print(kwargs)  # {}
        fn(1,2,3, a=10,b=20)
        
    函数的种类：
        普通函数：
            def fn():
                pass
        匿名函数:
            fn = lambda user: user
        回调函数:
            def fn1(fn):
                fn(10)
            fn1(lambda u:u+1)
        生成器函数:
            def fn():
                yield
            gen = fn()
            next(gen)
        
        生成器：
        
        json模块：
            loads()
            dumps()
        pickle模块
            dump()
            load()
        
    装饰器
    
    
15.面向对象
    class A:
        money = 100
        name = '张三'
        family = ['哥哥', '妹妹']  # 引用类型是共享属性
        def __init__(self, name, age):
            self.name = name
            self._age = age
        
        def run(self):
            print('run')
        
        @classmethod
        def fn1(cls):
            pass

        @staticmethod
        def fn2():
            pass
        
    clss B(A):
        def __init__(self):
            super().__init__()
                    
                    
16. 文件操作
    # model: r,w,a,  rb,wb,ab
    with open('') as fp:   
        fp.read()
        fp.read(100)
        fp.readline()
        fp.readlines()
        fp.write()
    
17. 异常处理
    try: 
        pass
    except Exception as e: 
        pass
    # finally:
    #     pass
    else: 
        pass
    
18. 序列化
    pickle
    json

19. 高阶函数
    map(), reduce(), filter(), sorted(), reversed(), zip()

20. Python2和Python3的区别
    
21. pip操作

22. 正则表达式

23. TCP&UDP区别，TCP'三次握手'和'四次挥手'
    
24. 进程，线程，协程
    
25. 虚拟环境virtualenv
    
'''

# 相同  1  1  或 ’1‘和’1‘
# 相似  1, '1'
# 深信服面试题
#   eval()

# 字符串拼接

# 列表生成器
# L = [i*i for i in range(10) if i%2==1]


# a, *b, c = 1, 2, 3, 4
# print(a, b, c)  # 1 [2, 3] 4
#
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))  # 33, python3.7:35个关键字
#
# a = 10
# # if a is not 10:
# if not a is 10:
#     pass
#
# users = [
#     {'name': '张三', 'age': 30},
#     {'name': '李四', 'age': 20},
#     {'name': '王五', 'age': 50},
#     {'name': '赵六', 'age': 40},
# ]
# def fn(user):
#     return user['age']
# # users.sort(key=lambda user:user['age'])
# users.sort(key=fn)
# print(users)


# string1 = "hello"
# string1 = string1 + ' world'
# print(string1)  # 'hello world'
#
# d = {}
# print(type(d))
#
#
# import random
# print(random.randrange(1, 2))
# print(random.randint(1, 2))


# 不定长参数
def fn(*args, **kwargs):
    print(args)  #
    print(kwargs)  #

# fn(1, 2, 3, a=10, b=20)
ages = [1, 2, 3]
user = {'name': '强东', 'age': 46}
fn(*ages, **user)


# 生成器函数: 函数内部有yied那么就是一个生成器函数
def fn1(n):
    print('n =', n)
    yield n
    print('n =', n+1)
    yield n+1

gen = fn1(10)  # 不会执行函数内部的代码
print(type(gen))  # <class 'generator'>
# print(next(gen))  # 执行函数内部代码，到第1个yield暂停，并返回yield后的值
# print(next(gen))  # 执行函数内部代码，到第2个yield暂停，并返回yield后的值
# print(next(gen))  # StopIteration，报错

# for n in gen:
#     print(n)


# 迭代器：可以用for-in和next使用的就是迭代器
# 可迭代对象: 可以使用for-in的
# 生成器： 是一个特殊的迭代器

# gen = (i for i in range(1,10))
# print(type(gen))  # <class 'generator'>
# print(next(gen))
# print(next(gen))


# 装饰器
# 作用：给函数动态添加功能
# 设计模式：23种
#    单例模式
#    代理模式
#    装饰模式
#     ...


# def fn():
#     print('hello world')
#
# def inner():
#     print('1')
#     fn()
#     print('2')
# inner()

# 闭包

# 装饰器
def outer(fn):  # fn=say
    def inner():
        print(1)
        fn()  # 原始的say
        print(2)
    return inner

@outer
def say():
    print('say')

@outer
def say2():
    pass

# say = outer(say)  # 装饰器原理

# print(say.__name__)

say()  # inner()


# 通用装饰器
# def outer(fn):
#     def inner(*args, **kwargs):
#         print("before")
#         ret = fn(*args, **kwargs)
#         print('after')
#         return ret
#     return inner
#
# @outer
# def say3(a,b,c,name):
#     print(a, b, c)
#     print(name)
#     return "haha"
#
#
# ret = say3(1,2,3, name='宝强')
# print(ret)
# print("*" * 100)


# 带参数装饰器
# def deco(n):
#     def outer(fn):
#         def inner():
#             print('before, n =', n)
#             fn()
#             print('after, n =', n)
#         return inner
#
#     return outer
#
# @deco(10)
# def say4():
#     print('say4')

# say4 = deco(10)(say4) => outer(say4)

# say4()


# 排序
# 冒泡排序，选择排序
# 快速排序
#   L = [8, 2, 3, 6, 5, 4, 1, 9, 7]
#       [2,3,4,1]           [5]    [8,6,9,7]
#       [2,1]    [3] [4]    [5]    [][6] [8,9,7]
#       [1][2][] [3] [4]    [5]    [][6] [8,7]     [9][]
#       [1][2][] [3] [4]    [5]    [][6] [7][8][]  [9][]
#

# def quick_sort(L):
#     if len(L) < 2:
#         return L
#
#     n = L.pop(len(L)//2)
#     left = []
#     right = []
#     for i in L:
#         left.append(i) if i < n else right.append(i)
#
#     return quick_sort(left) + [n] + quick_sort(right)
#
#
# new_L = quick_sort([8, 2, 3, 6, 5, 4, 1, 9, 7])
# print(new_L)


# a, *b, c = 1, 2, 3, 4
# print(a)
# print(b)
# print(c)


# list1 = [1,2,34,5]
# newList = list(reversed(list1))#: 倒序,不改变原列表
# # print(type(newList))
# print(newList)





