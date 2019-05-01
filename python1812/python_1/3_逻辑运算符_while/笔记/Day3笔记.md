### 一、上堂回顾

> 1.关键字和标识符
>
> ​	标识符
>
> ​		定义合法标识符的规则和规范
>
> ​		规则：
>
> ​			a.数字，字母，下划线
>
> ​			b.开头不能是数字
>
> ​			c.不能使用关键字
>
> ​			d.严格区分大小写
>
> ​		规范：
>
> ​			a.尽量做到见名知意
>
> ​			b.英文单词全部小写，不同单词之间使用下划线分隔
>
> ​			   驼峰命名法【大驼峰：类的命名，小驼峰：变量名或者函数名】
>
> 2.常量和变量
>
> ​	Python中的数据类型：Number,String,Boolean,None,list,tuple,dict,set
>
> ​	变量：
>
> ​		定义：变量名称  = 初始值
>
> ​		注意：Python中的变量的数据类型并不是一成不变的，进行重新赋值的时候，类型也可以发生改变
>
> ​		作用：存储数据，参与运算
>
> ​		变量在内存中的工作原理【了解】：变量中存储的是地址
>
> ​			栈，堆，方法区中的常量池
>
> ​		删除变量：del 变量名
>
> 3.input和print
>
> ​	input的结果都是字符串
>
> ​		int()    float()
>
> 4.运算符
>
> ​	赋值：+=     等价关系
>
> ​	关系【比较】：得到的结果肯定是布尔值
>
> 5.分支语句中的if语句【掌握】
>
> ​	单分支【要么执行，要么不执行】，双分支【二选一】，多分支【多选一】
>
> ​	嵌套if语句：
>
> 作业讲解：
>
> ```Python
> #导入模块，random表示的随机数
> import random
>
>
> """
> #从控制台输入两个数，输出较大的值
> num1 = int(input("输入第一个数"))
> num2 = int(input("输入第er个数"))
> #定义一个新的变量，用于保存最大值
> max1 = num1
> if num2 > max1:
>     #给max1重新赋值
>     max1 = num2
> print(max1)
>
>
> #从控制台输入三个数，输出较大的值
> num1 = int(input("输入第一个数"))
> num2 = int(input("输入第er个数"))
> num3 = int(input("输入第san个数"))
>
> #max2中保存的是num1和num2中的最大值
> max2 = num1
> if num2 > num1:
>     max2 = num2
> #将 num1和num2中的最大值和num3比较
> if num3 > max2:
>     max2 = num3
>
> print(max2)
> """
>
> #.x 为 0-99 取一个数,y 为 0-199 取一个数,如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y
> #input
> #表示在0~指定范围内获取一个随机数
> x = random.choice(range(99))
> y = random.choice(range(199))
> if x > y:
>     print(x)
> elif x == y:
>     print(x + y)
> else:
>     print(y)
>
> """
> 从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
> 	例如：153=1^3+5^3+3^3
> """
> num = int(input())
> #将该数的个十百位拆分出来
> gw = num % 10
> sw = num % 100 // 10
> bw = num // 100
>
> result = pow(gw,3) +pow(sw,3) + pow(bw,3)
>
> if num == result:
>     print("是水仙花")
> ```

### 二、运算符与表达式【第二部分】

#### 1.逻辑运算符

> 作用：逻辑运算的，每次的运算得到的结果都是布尔值
>
> 使用：一般是结合关系运算符使用
>
> 逻辑运算符：
>
> ​	and【逻辑与】：
>
> ​		表达式1 and 表达式2：只有当表达式1和表达式2同时成立的时候，结果为True
>
> ​	or【逻辑或】
>
> ​		表达式1 or  表达式2:当表达式1和表达式2中至少有一个为真，结果为True
>
> ​	not【逻辑非】
>
> ​		not 表达式：真---》假   假---》真

##### 1.1逻辑与

> 代码演示：
>
> ```Python
> """
> 逻辑与
>
> 真  and 真 = 真
> 真  and 假 = 假
> 假  and 真 = 假
> 假  and 假 = 假
>
> 规律：全真为真，一假则假
> """
> num1 = 10
> num2 = 20
> #1.逻辑运算符可以结合算术运算符
> if num1 - 10 and num2:
>     print("成立")
> else:
>     print("不成立")
>
> if num1 and num2:
>     print("成立")
> else:
>     print("不成立")
>
> #2.逻辑运算符结合赋值运算符使用?------不能使用
> #if num1 += 1 and num2 -= 1:
>    # print("fjkagh")
>
> #3.逻辑运算符结合关系运算符使用【使用频率最广】
> if num1 > num2 and num1 == num2:
>     print("ok")
> ```

##### 1.2逻辑或

> 代码演示：
>
> ```Python
> """
> 二、逻辑或
> 真 or 真 = 真
> 真 or 假 = 真
> 假 or 真 = 真
> 假 or 假 = 假
>
> 规律：
> 一真为真，全假则为假
> """
> num3 = 0
> num4 = 1
> if num3 or num4:
>     print("ok")
>
> if num3 > num4 or num4:
>     print("fbhsjfg")
> ```

##### 1.3逻辑非

> 代码演示：
>
> ```Python
> """
> 三、逻辑非
> not 真 = 假
> not 假 = 真
> """
> if not num3:
>     print("*****8")
> else:
>     print("$$$$$")
> ```

1.4短路原则

> 出现的时机：逻辑运算符不止一个的时候，则会出现短路原则
>
> 规律：
>
> ​	a.表达式从左向右进行计算，如果or的左边的逻辑值为True，则整个表达式的值为True，则短路or后面的所有的表达式【不管是and还是or】
>
> ​	b.表达式从左向右进行计算,如果and的左边的逻辑值是False，则整个表达式的值为False，则短路and后面的所有的表达式【不管是and还是or】
>
> ​	c.如果or的左边的逻辑值为False或者and的左边的逻辑值为True，则不再遵循短路原则
>
> 代码演示：
>
> ```Python
> #1.表达式从左向右进行计算,如果and的左边的逻辑值是False，则整个表达式的值为False，则短路and后面的所有的表达式【不管是and还是or】
> def a():
>     print("A")
>     return False
> def b():
>     print("B")
>     return False
> def c():
>     print("C")
>     return True
> def d():
>     print("D")
>     return False
> def e():
>     print("E")
>     return True
>
> #整个表达式的值为False，因为and的左边为False
> #将and后面的所有的表达式短路【不会被执行】
>
> #if False and False and True and False and True    =  False
> if a() and b() and c() and d() and e():
>     print("ok")
>
> print("*************分割线************")
>
> #2.如果and的左边的逻辑值为True，则不再遵循短路原则
> def a():
>     print("A")
>     return True
> def b():
>     print("B")
>     return True
> def c():
>     print("C")
>     return False
> def d():
>     print("D")
>     return False
> def e():
>     print("E")
>     return True
>
> #True and True and False and False and True   --->a b
> #True and False and False and True  ----》c
> #False and False and True---->短路
>
> #整个表达式的值为False，打印的结果为ABC
> if a() and b() and c() and d() and e():
>     print("ok111")
>
> print("*************分割线************")
>
> #3。表达式从左向右进行计算，如果or的左边的逻辑值为True，则整个表达式的值为True，则短路or后面的所有的表达式【不管是and还是or】
> def a():
>     print("A")
>     return True
> def b():
>     print("B")
>     return False
> def c():
>     print("C")
>     return True
> def d():
>     print("D")
>     return False
> def e():
>     print("E")
>     return True
>
>
> #整个表达式的值为True，打印的结果为A
>
> #True or False or True or False or True
> if a() or b() or c() or d() or e():
>     print("ok222")
>
> print("*************分割线************")
>
> #4.如果or的左边的逻辑值为False，则不再遵循短路原则
> def a():
>     print("A")
>     return False
> def b():
>     print("B")
>     return False
> def c():
>     print("C")
>     return True
> def d():
>     print("D")
>     return False
> def e():
>     print("E")
>     return True
>
> #False or False or True or False or True----->a b
> #False or True or False or True----->c
> #True or False or True ----->整个表达式的值为True，d 和e被短路
> if a() or b() or c() or d() or e():
>     print("ok333")
>
> print("*************分割线************")
>
> #5 and和or混合使用
> def a():
>     print("A")
>     return False
> def b():
>     print("B")
>     return False
> def c():
>     print("C")
>     return True
> def d():
>     print("D")
>     return False
> def e():
>     print("E")
>     return True
> def f():
>     print("F")
>     return True
> def g():
>     print("G")
>     return False
> def h():
>     print("H")
>     return True
>
> #False and False and True and False or True and True or False and True----》打印A，短路了BCD
> #False or True and True or False and True---->打印E
> #True and True or False and True ------>打印F
> #True or False and True------》整个表达式的结果为True，G和H被短路
> """
> 实现思路：
> 1.从左往右，第一个表达式为False，则短路后面的表达式，直到遇到or【打印A】
> 2.对获得的新的表达式进行判断，or的左边为False，则不符合短路原则
> 3.and的左边为True，则不符合短路原则
> 4.or的左边为True，符合短路原则
> """
> if a() and b() and c() and d() or e() and f() or g() and h():
>     print("ok4444")
> ```
>
> 注意：在实际开发中，尽量避免短路原则，对不同的条件添加括号

#### 2.成员运算符

> 注意;在list
>
> in:如果在指定列表中找到值，返回True，否则返回False
>
> not in:如果在指定列表中未找到值，返回True，否则返回False

#### 3.身份运算符

> is:判断两个标识符是否是引用自同一个实体【对象】
>
> is not:判断两个标识符是否是引用自不同的实体【对象】
>
> 代码演示：
>
> ```Python
> a = 10
> b = 10
> #判断两个标识符是否是引用自同一个实体
> if a is b:
>     print("Yes")
> else:
>     print("no")
>
> if a is not b:
>     print("Yes")
> else:
>     print("no")
>
> if a == b:
>     print("hello")
>
> if id(a) == id(b):
>     print("id")
>
> print("8888888888")
>
> b = 20
> if a is b:
>     print("Yes")
> else:
>     print("no")
>
> if a is not b:
>     print("Yes")
> else:
>     print("no")
>
> if a == b:
>     print("hello~~~")
>
> #id():获取指定实体的地址
> if id(a) == id(b):
>     print("id~~~~~")
>
>
> str1 = "abc"
> str2 = "abc"
> print(str1 == str2)
> print(str1 is str2)
> print(id(str1) == id(str2))
> ```
>
> 总结：
>
> is和id()：比较的是变量的地址
>
> ==：比较的是变量中存储的值

#### 4.运算符的优先级

> 注意：
>
> ​	1.加括号
>
> ​	2.分步骤进行操作

### 三、循环结构中的while语句

#### 1.什么是循环

> 一个现象周期性的出现
>
> 在编程语言中，在满足条件的情况下，反复执行某一段代码，这种现象被称为循环，这段被重复执行的代码被称为循环体
>
> 问题：当反复执行循环体的时候，需要在合适的时机将条件改为假，从而结束循环，否则会形成一个死循环
>
> Python中的循环语句：while语句，for语句
>
> 举例：打印10000遍hello world

#### 2.while语句

##### 2.1使用

> 语法：
>
> if 条件表达式:
>
> ​	语句
>
> while 条件表达式:
>
> ​	循环体
>
> 说明：当条件表达式成立的时候，if语句只会被执行一次，但是，while语句会被多次执行，具体执行多少次取决于条件表达式
>
> while工作原理：当程序从上往下依次执行的过程中，遇到了while语句，首先计算条件表达式的值，如果条件表达式的值为假，则直接跳过整个while语句继续执行后面的代码;如果条件表达式的值为真，则执行循环体，然后再次继续判断条件表达式的值，如果还为真，则继续执行循环体。。。。。如此循环往复，最终当条件表达式的值为假，表示循环结束
>
> 代码演示：
>
> ```Python
> #使用while语句解决
> """
> while True:
>     print("hello world")
> """
>
> #问题：相办法控制循环的次数
> #1.定义一个变量，用于记录循环的次数
> num = 0
> #2.判断num和一个指定值的大小，条件表达式用来控制循环的次数
> while num < 10:
>     print("hello world")
>     #3.控制次数，在适当的时机结束循环
>     num += 1    #num = num + 1
>
> #初始化表达式
> num = 100
> #条件表达式
> while num > 90:
>     #循环体
>     print("hello world")
>     #循环之后的操作表达式
>     num -= 1
> ```

##### 2.2死循环

> 在循环语句中，表达式永远为真的循环
>
> 代码演示：
>
> ```Python
> #常见的死循环的写法：
> while True:
> 	#xxx
> while 1:
> 	#xxxxx
> ```

##### 2.3else分支

> 语法：
>
> if 条件表达式:
>
> ​	语句
>
> else:
>
> ​	语句
>
> while 条件表达式:
>
> ​	循环体
>
> else:
>
> ​	语句
>
> 说明：
>
> ​	a.在if-else中，当条件表达式为假的时候，才会执行else分支
>
> ​	b.在while-else中，
>
> ​		当条件表达式为真，先执行完循环，最后才执行else
>
> ​		当条件表达式为假，直接执行else
>
> 代码演示：
>
> ```Python
> num = 0
> while num > 10:
>     print("abc")
>     num += 1
> else:
>     print("ok")
>     
> num = 0
> while num < 10:
>     print("abc")
>     num += 1
> else:
>     print("ok")
> ```

> 课堂练习：
>
> ```Python
> #1.求1~100之间所有偶数的和
> num = 1
> sum = 0
> while num <= 100:
>     #print(num)
>     sum += num    #sum = sum + num
>     num += 1
> #100之间所有整数由奇数和偶数组成，偶数之间递增2
> num1 = 0
> sum1 = 0
> while num1 <= 100:
>     #print(num)
>     sum1 += num1
>     num1 += 2
> 
> # if语句
> num2 = 0
> sum2 = 0
> while num2 <= 100:
>     #print(num)
>     if num2 % 2 == 0:
>         sum2 += num2
>     num2 += 1
> 
> #2.统计100~1000之间能被6整数的数的个数
> n1 = 100
> #定义一个变量，用于统计符合条件的数的个数
> count = 0
> while n1 <= 1000:
>     if n1 % 6 == 0:
>         count += 1
>     n1 += 1
> 
> print(count)
> 
> #3.计算10的阶乘
> #1*2*3*4....*10
> n = 1
> total = 1
> while n <= 10:
>     total *= n
>     n += 1
> ```

##### 2.4嵌套while循环

> 类似于if的嵌套
>
> 语法：
>
> while 表达式1：
>
> ​	while 表达式2：
>
> ​		循环体
>
> 代码演示：
>
> ```Python
> """
> while 表达式1：
>
> 	while 表达式2：
>
> 		循环体
>
> """
> num1 = 0
> while num1 < 3:
>     num2 = 0
>     while num2 < 5:
>         print(num1,num2)
>         num2 += 1
>
>     num1 += 1
>
> #注意：
> #1.嵌套while循环总共的循环次数：外层循环的次数*内层循环的次数
> #2.外层循环必须等待内层循环执行完成之后才能继续下一次循环
>
>
> #打印九九乘法表
> """
>                                                         行           列
> 1x1=1                                                   1             1
> 1x2=2 2x2=4                                             2             2
> 1x3=3 2x3=6 3x3=9                                       3             3
> .....
>
> 1x9=9 2x9=18 3x9=27  ........   8x9=72  9x9=81          9             9
>
> 规律：
> 行的取值范围：1~9
> 列的取值范围：1~行数
>
> 列随着行的变化而变化的
> 列的最大值和行数相等
>
> """
> #嵌套循环
> #外层循环：控制行
> line = 1
> while line <= 9:
>     #循环体
>     #内层循环：控制列
>     colum = 1
>     while colum <= line:
>         #列x行
>         #占位符:%d表示整数
>         #print默认情况下可以换行,可以采用end=""阻止换行
>         print("%dx%d=%d"%(colum,line,colum*line),end=" ")
>         colum += 1
>     #换行
>     print("")
>     line += 1
>
>
> """
> *
> **
> ***
> ****
> *****
> """
> i = 1
> while i <= 5:
>     j = 1
>     while j <= i:
>         print("*",end="")
>         j += 1
>     print("")
>     i += 1
> ```