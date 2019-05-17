### 一、上堂回顾

> 默写题目：
>
> ​	1.举例说明函数的特殊用法【1.变量可以指向函数，2.函数名也是一个变量，3.函数可以作为参数】
>
> ```Python
> def test():
>   pass
>
> #1.变量可以指向函数
> f = test
> #注意：这个变量就可以像函数名一样调用函数
> f()
>
> #2.函数名也是一个变量
> #test = 10
>
> #test()
>
> #3.函数可以作为参数
> def func(f):
>   f()
>   
> func(test)
> ```
>
> ​	2.已知列表list1 = [1,2,3,4,5],使用列表生成式生成一个列表，newList = [3,6,9,12,15]
>
> ```Python
> #[需要生成的列表的元素  for-in  判断条件]
> #注意：生成的仍然是一个list；for-in遍历的一般是已知的列表
> #作用：通过已知的列表生成一个新的列表
>
> list1 = [1,2,3,4,5]
> newList = [element * 3 for element in list1]
>
> #newList1 =  [2,4]
> newList1 = [e  for e in list1 if e % 2 == 0]
> ```
>
> 知识点回顾：
>
> ​	1.函数的特殊用法
>
> ​	2.偏函数【了解】
>
> ​		已知函数，默认参数，根据不同的需求对参数进行一些控制，生成一个新的函数，生成的函数被称为偏函数
>
> ​		functools.partial(已知函数名，默认参数)
>
> ​		newFunc = functools.partial(int，base=2)
>
> ​	3.闭包
>
> ​		在外部函数中定义一个内部函数，并且外部函数的返回值是内部函数的引用【函数名】，构成了闭包【执行过程：内部函数将外面不能直接调用，只能通过调用外部函数调用内部函数】
>
> ​		应用：装饰器
>
> ​	4.变量的作用域
>
> ​		局部作用域，函数作用域，全局作用域，内置作用域【就近原则，变量重名】
>
> ​		全局变量和局部变量
>
> ​			函数，模块，类
>
> ​		global和nonlocal:修改变量的作用域
>
> ​	5.列表生成式，生成器
>
> ​		[] :list
>
> ​		():generator
>
> ​			for
>
> ​			next()   StopIteration  停止迭代
>
> ​			yield：让步   next()

### 二、迭代器【掌握】

#### 1.可迭代对象

> 可迭代对象【实体】：可以直接作用于for循环的实体【Iterable】
>
> 可以直接作用于for循环的数据类型：
>
> ​	a.list,tuple,dict,set,string	
>
> ​	b.generator【() 和yield】
>
> isinstance:判断一个实体是否是可迭代的对象	
>
> 代码演示：
>
> ```Python
> #一、可迭代对象
>
> #1.导入
> from  collections  import  Iterable
>
> #2.使用isinstance(数据，Iterable)
> print(isinstance([],Iterable))
> print(isinstance((),Iterable))
> print(isinstance({},Iterable))
> print(isinstance((x for x in range(10)),Iterable))
> print(isinstance("hello",Iterable))
>
> print(isinstance(10,Iterable))   #False
> print(isinstance(True,Iterable))  #False
>
> print("****88")
> ```

#### 2.迭代器

> 不但可以作用于for循环，还可以被next函数遍历【不断调用并返回一个元素，直到最后一个元素被遍历完成，则出现StopIteration】
>
> 目前为止，只有生成器才是迭代器【Iterator】
>
> 结论：迭代器肯定是可迭代对象，但是，可迭代对象不一定是迭代器
>
> isinstance:判断一个实体是否是迭代器
>
> 代码演示：
>
> ```Python
> #二、迭代器
> from  collections  import  Iterator
>
> print(isinstance([],Iterator))
> print(isinstance((),Iterator))
> print(isinstance({},Iterator))
> print(isinstance("hello",Iterator))
> print(isinstance((x for x in range(10)),Iterator))   #True
>
> print("****88")
> ```

#### 3.可迭代对象和迭代器之间的转换

> 可以将可迭代对象转换为迭代器：iter()
>
> 代码演示：
>
> ```Python
> #三、虽然list、tuple、dict、set、string都不是迭代器
> #iter():将list、tuple、dict、set、string的  Iterable转换为Iterator
> print(isinstance(iter([]),Iterator))
> print(isinstance(iter(()),Iterator))
> print(isinstance(iter({}),Iterator))
> print(isinstance(iter("hello"),Iterator))
> ```
>
> 总结：
>
> ​	a.凡是可以作用于for循环的对象都是Iterable类型
>
> ​	b.凡是可以作用于next函数的对象都是Iterator类型
>
> ​	c.list/tuple/dict/set/string都不是Iterator，可以通过iter()获得一个Iterator对象
>
> 【面试题】
>
> 区分可迭代对象和迭代器

### 三、装饰器【掌握】

#### 1.案例

> 代码演示：
>
> ```Python
> def test():
>     print("拼搏到无能为力，坚持到感动自己")
>
>
> f = test()  #变量可以指向指向函数，函数名也是一个变量，所以变量可以当做函数调用
> f()
>
>
> #思考问题：test增加功能，但是不能修改test函数内部----->装饰器
> ```
>
> 在代码运行期间，可以动态增加函数功能的方式，被称为装饰器【Decorator】
>
> 也就是说，在不修改原函数的基础上，给原函数增加功能
>
> 好处：在团队开发中，如果两个或者两个以上的程序员会用到相同的功能，但是功能又有细微的差别，采用装饰器：相互不影响，代码简化

#### 2.使用

##### 2.1简单装饰器

> 代码演示：
>
> ```Python
> #1.简单的装饰器
> def test():
>     print("拼搏到无能为力，坚持到感动自己")
>
> #a.书写闭包
> #b.给外部函数设置参数,fun表示的是原函数
> def outer(fun):
>     def inner():
>         # d.给原函数增加功能
>         print("hello")
>
>         #c.调用原函数
>         fun()
>
>     return inner
>
> #e.使用闭包
> f = outer(test)   #f = inner
> f()   #inner()
>
> #注意：增加的功能可以写在原函数调用的前面或者后面
> #注意：outer函数就被称为装饰器
>
>
> #练习：给下面的函数添加功能，打印九九乘法表
> def show():
>     for i in range(10):
>         print(i)
>
> def outer1(fun):
>     def inner1():
>         fun()
>         for i in range(1,10):
>             for j in range(1,i + 1):
>                 print("%dx%d=%d"%(j,i,i * j),end=" ")
>             print("")
>     return  inner1
>
> f1 = outer1(show)
> f1()
> ```

##### 2.2有参数的装饰器

> 代码演示：
>
> ```Python
> #2.原函数有参数的装饰器
> def getAge(age):
>     print(age)
>
> getAge(10)
> getAge(-5)
>
> print("************")
>
> #需求：在不修改原函数的基础上，进行数据的过滤：当用户输入age为负数的时候，则置为0
> def wrapper(fun):
>     #注意：当原函数有参数，装饰器的作用是为了操作原函数中的参数，给inner设置参数
>     def inner(num):
>         #增加新功能：过滤负数
>         if num < 0:
>             num = 0
>
>         #调用原函数
>         fun(num)  #age = num
>     return  inner
>
> f = wrapper(getAge)
> f(10)   #num = 10
> f(-5)
> ```

##### 2.3系统的简写

> 代码演示：
>
> ```Python
> #3.简化demo2中的操作：@装饰器的名称  应用到原函数中
>
> #需求：在不修改原函数的基础上，进行数据的过滤：当用户输入age为负数的时候，则置为0
> def wrapper(fun):
>     #注意：当原函数有参数，装饰器的作用是为了操作原函数中的参数，给inner设置参数
>     def inner(num):
>         #增加新功能：过滤负数
>         if num < 0:
>             num = 0
>
>         #调用原函数
>         fun(num)  #age = num
>     return  inner
>
> #将wrapper装饰器应用在了getAge函数上，
> @wrapper
> def getAge(age):
>     print(age)
>
> getAge(10)
> getAge(-5)
>
> """
> @wrapper
>
> 等价于
>
> f = wrapper(getAge)
> f(10)   #num = 10
>
> #注意;当使用@的时候，在同一个文件中，装饰器必须出现的原函数的前面
>
> """
> ```

##### 2.4不定长参数的装饰器

> 代码演示：
>
> ```Python
> #4.不定长参数的装饰器
>
> #应用场景：当同一个装饰器作用于不同函数的时候，这些函数的参数的个数是不相同的
> def wrapper(fun):
>     def inner(*args):
>         print("hello")
>
>         fun(*args)   #a = args[0]   b = args[1]
>
>     return  inner
>
> @wrapper
> def fun1(a,b):
>     print(a + b)
>
> @wrapper
> def fun2(a,b,c,d):
>     print(a,b,c,d)
>
> fun1(10,20)   #args = (10,20)
> fun2(1,2,3,4)
> ```

##### 2.5多个装饰器作用于同一个函数 

> 代码演示：
>
> ```Python
> #5.将多个装饰器应用到同一个函数上
> def wrapper1(fun):
>     def inner1():
>         print("1~~~~")
>         fun()
>
>     return inner1
>
> def wrapper2(fun):
>     def inner2():
>         print("2~~~~")
>         fun()
>
>     return inner2
>
> @wrapper1
> @wrapper2
> def show():
>     print("hello")
>
> show()
>
> """
> 1~~~~
> 2~~~~
> hello
> """
>
> #结论：多个装饰器作用于同一个函数的时候，从第一个装饰器开始，从上往下依次执行，但是，原函数只会被执行一次
> ```

### 四、函数递归【了解】

#### 1.概念

> 递归函数：一个会调用自身的函数【在一个函数的内部，自己调用自己】
>
> 递归调用
>
> 递归中包含了一种隐式的循环，他会重复指定某段代码【函数体】，但这种循环不需要条件控制
>
> 使用递归解决问题思路：
>
> ​	a.找到一个临界条件【临界值】
>
> ​	b.找到相邻两次循环之间的关系
>
> ​	c.一般情况下，会找到一个规律【公式】

#### 2.使用

> 代码演示：
>
> ```Python
> #案例一
> """
>                1 2 3 4 5 6 7  8  9 10  11.。。。
> 斐波那契数列：1,1,2,3,5,8,13,21,34,55,89.....
>
> 解决问题：报一个数，输出数列中对应的数
>
> 规律：
> a.第一个位置和第二个位置上数是固定的，都是1
> b.第n个位置上的数：第 n - 1 的数  +   第 n - 2 的数
>
> r1 = func1(1)  ------>1
> r2 = func1(2)  ------>1
> r3 = fun1(3) ------>func1(1) + func1(2)----->1 + 1 = 2
> r4 = fun1(4)------->fun1(3) + fun1(2) ----->func1(1) + func1(2) +  fun1(2) ---->1  + 1 + 1 = 3
> r5 = fun1(5) ----->fun1(4) + fun1(3) ----->fun1(3) + fun1(2) + func1(1) + func1(2)--->func1(1) + func1(2) ++ fun1(2) + func1(1) + func1(2)--->5
> .....
> rn = fun1(n) ----->fun1(n- 1) + fun1(n - 2)
> """
>
> def func1(num):
>     #临界值
>     if num == 1 or num == 2:
>         return 1
>     else:
>         #print("~~~~",num)
>         result = func1(num- 1) + func1(num - 2)    #result = func1(1) + func1(2)  --->1 + 1 =2
>         return result
>
> print(func1(10))
>
> #练习;使用递归计算1~某个数之间的和
> """
> add(1) = 1   :临界值
> add(2) = add(1) + 2
> add(3) = add(2) + 3 ---->add(1) + 2 + 3 = 1 + 2 + 3
> add(4) = add(3) + 4---->add(2) + 3 + 4 ---->add(1) + 2 + 3 + 4---->1 + 2 + 3 + 4
> ....
> add(n) = add(n - 1) + n
> """
> def add(num):
>
>     """
>     n = 1
>     sum = 0
>     while n <= 100:
>         sum += n
>         n += 1
>
>     return sum
>
>     sum1 = 0
>     for i in range(1,num + 1):
>         sum1 += i
>     return  sum1
>     """
>     #使用递归实现
>     if num == 1:
>         return 1
>     else:
>         return add(num - 1) + num
>
> print(add(100))
> ```
>
> 注意：以后在实际项目中尽量少用递归，如果隐式循环的次数太多，会导致内存泄漏【栈溢出】
>
> 优点：简化代码，逻辑清晰

### 五、栈和队列【了解】

> 用于存储数据的线性表
>
>

#### 1.栈

> Stack
>
> 开口向上的容器：先进后出，后进先出
>
> 代码演示：
>
> ```Python
> #list的底层维护了一个栈的线性表
>
> myStack = []
>
> #插入数据
> #数据入栈【压栈】
> myStack.append(1)
> print(myStack)
> myStack.append(2)
> print(myStack)
> myStack.append(3)
> print(myStack)
> myStack.append(4)
> print(myStack)   #[1,2,3,4]
>
> #出栈
> myStack.pop()
> print(myStack)
> myStack.pop()
> print(myStack)
> myStack.pop()
> print(myStack)
> myStack.pop()
> print(myStack)
> ```

#### 2.队列

> queue
>
> 水平放置的水管：先进先出，后进后出
>
> 代码演示：
>
> ```Python
> import  collections   #数据结构的集合
>
> queue  = collections.deque([1,2,3,4])
> print(queue)
>
> #入队【存储数据】
> queue.append(5)
> print(queue)
> queue.append(6)
> print(queue)
>
> #出队【获取数据】
> queue.popleft()
> print(queue)
> queue.popleft()
> print(queue)
> queue.popleft()
> print(queue)
> ```

### 六、目录遍历【了解】

> os  用于获取系统的功能，主要用于操作文件或者文件夹
>
> 代码演示：
>
> ```Python
> import  os
>
> path = r"C:\Users\Administrator\Desktop\SZ-Python1805\Day10"
>
> #获取指定目录下所有的文件以及文件夹，返回值为一个列表
> filesList = os.listdir(path)
> print(filesList)
>
> #C:\Users\Administrator\Desktop\SZ-Python1805\Day10\作业
> #通过初始路径拼接子文件或者子文件夹形成新的路径
> filePath = os.path.join(path,"作业")
> print(filePath)
>
> #判断指定的路径是否是文件夹【目录】
> result = os.path.isdir(filePath)
> print(result)
> ```

#### 1.使用递归遍历目录

> 代码演示：
>
> ```Python
> #1.递归
> import os
>
>
> def getAll(path):
>     #1.获取当前目录下所有的文件以及文件夹
>     fileList = os.listdir(path)
>     print(fileList)
>
>     #2.遍历列表
>     for i in fileList:
>         #3.拼接路径
>         filePath = os.path.join(path,i)
>
>         #4.判断filePath是否是文件夹
>         if os.path.isdir(filePath):
>             #文件夹:递归
>             getAll(filePath)
>         else:
>             #文件
>             print("文件：",i)
>
> getAll(r"C:\Users\Administrator\Desktop\SZ-Python1805")
> ```

#### 2.栈模拟递归遍历目录

> 深度遍历
>
> 代码演示：
>
> ```Python
> #栈
> #append   pop
> import  os
>
>
> def getAll(path):
>     #初始状态下，栈是空的
>     stack = []
>
>     #将初始路径添加到栈中
>     stack.append(path)
>
>     #处理栈，当栈为空的时候说明其中的内容为空，循环停止
>     while len(stack) != 0:
>         #从栈中取出数据
>         dirPath = stack.pop()
>
>         #获取指定路径下的所有的文件以及文件夹
>         filesList = os.listdir(dirPath)
>
>         #遍历列表‘
>         for fileName in filesList:
>             filePath  = os.path.join(dirPath,fileName)
>
>             if os.path.isdir(filePath):
>                 print("文件夹；",fileName)
>
>                 #如果是目录，将路径添加到栈中
>                 stack.append(filePath)
>
>                 print(stack)
>             else:
>                 print("文件：",fileName)
>
> getAll(r"C:\Users\Administrator\Desktop\SZ-Python1805")
> ```

#### 3.队列模拟递归遍历目录

> 广度遍历
>
> 代码演示：
>
> ```Python
> #栈
> #append   popleft
> import  os
> import  collections
>
>
> def getAll(path):
>     #初始状态下，队列是空的
>     queue = collections.deque()
>
>     #将初始路径添加到队列中
>     queue.append(path)
>
>     #处理栈，当栈为空的时候说明其中的内容为空，循环停止
>     while len(queue) != 0:
>         #从栈中取出数据
>         dirPath = queue.popleft()
>
>         #获取指定路径下的所有的文件以及文件夹
>         filesList = os.listdir(dirPath)
>
>         #遍历列表‘
>         for fileName in filesList:
>             #拼接路径
>             filePath  = os.path.join(dirPath,fileName)
>
>             if os.path.isdir(filePath):
>                 print("文件夹；",fileName)
>
>                 #如果是目录，将路径添加到队列中
>                 queue.append(filePath)
>
>             else:
>                 print("文件：",fileName)
>
> getAll(r"C:\Users\Administrator\Desktop\SZ-Python1805")
> ```



