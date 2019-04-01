### 一、上堂回顾

> 默写题目：
>
> ​	1.自定义一个异常，抛出异常对象并捕获
>
> ```Python
> #1.自定义一个类，继承自Exception
> class CustomException(Exception):
>   #2.书写构造函数，调用父类的构造函数
>   def __init__(self,msg):
>     super(CustomException,self).__init__()
>     self.msg = msg
>     
>   #3.重写__str__
>   def __str__(self):
>     return self.msg
>   
>   #4.定义一个成员方法，处理异常
>   def handle(self):
>     pass
>   
> #6.捕获：为了后面的代码正常运行
> try:
>   #5。抛出异常：raise  异常对象
>   raise CustomException("自定义异常")
> except CustomException as e:
>   print(e)
>   e.handle()
> ```
>
> ​	2.实现一个普通.txt文件内容的拷贝
>
> ```Python
> import os
> path1 = ""
> path2  = ""
>
> #1.打开文件
> f1 = open(path1,"r")
> f2 = open(path2,"w")
>
> #2.读取并且写入
> #获取原文件的大小
> size = os.path.getsize(path1)
> #循环读取文件，并将读取到的内容写入到目标文件中
> while size > 0:
>   content = f1.read(1024)
>   f2.write(content)
>   size -= 1024
>   
> #3.关闭文件
> f1.close()
> f2.close()
> ```
>
> ​	3.已知一个非空test.csv文件，读取其中的内容
>
> ```Python
> import csv
>
> path = ""
> #1.打开文件
> with open(path,"r") as f:
>   #2.将文件对象封装成一个可迭代对象
>   reader = csv.reader(f)
>   #3.获取内容
>   for item in reader:
>     print(item)
> ```

### 二、作业讲解

#### 1.邮编查询

> 邮编查询，查到返回对应的城市 否则提示无此邮编
>
> 代码演示：
>
> ```Python
> #邮编
> num = input("请输入邮编：")  #str
>
> path = "youbian.txt"
>
> #读取文件
> f = open(path,"r",encoding="utf-8")
>
> str = f.readline()
>
> while str:
>     newStr = str[1:]
>     if newStr.startswith(num):
>         print(str[9:-4])
>     str = f.readline()	
> ```

#### 2.开房查询

> 开房查询
>
> ​	输入名字，查询其开房记录，如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中
>
> 代码演示：
>
> ```Python
> import  os
> #1.读取文件
> def loadFile(path):
>     f = open(path,"r",encoding="utf-8")
>     #返回值为一个列表
>     list = f.readlines()
>     print(list)
>
>     f.close()
>
>     return list
>
> #2.查询
> def search(list,name):
>     #作用;保存查找到的人的信息
>     subList = []
>
>     #遍历list，获取每一条信息
>     for line in list:
>        infoList =  line.split(",")
>        #查询
>        if name == infoList[0]:
>            #将查询到的信息保存到subList中
>            subList.append(line)
>
>     """
>     如果查询到数据，则返回一个有元素的列表
>     如果未查询到数据，则返回一个空列表
>     """
>     return  subList
>
> if __name__ == "__main__":
>     path = "kaifanglist.txt"
>     #调用读取数据的函数,返回的是所有的信息
>     allList = loadFile(path)
>
>     while True:
>         name = input("请输入要查找的人的姓名【输入q退出】：")
>         if name == "q":
>             break
>         else:
>             #调用查找的函数
>             singleList = search(allList,name)
>
>             if singleList:
>                 #将相关的信息写入到一个新的文件中
>                 print(name + "果然去开房了")
>
>                 #将singleList中的数据写入到一个新的文件中
>                 #newPath = os.path.join("",name)
>                 f = open(name + ".txt","w",encoding="utf-8")
>
>                 #遍历列表，将查询到的数据分条写入
>                 for row in singleList:
>                     f.write(row)
>
>                 #关闭文件
>                 f.close()
>
>                 print("数据提取成功")
>             else:
>                 print("他是个好男人，好好珍惜吧")
> ```

### 三、枚举类【扩展】

#### 1.概念

> 枚举类型可以看做是一种标签或者一系列常量的集合
>
> 作用：表示某些特定的有限的集合，举例：月份，星期，状态等
>
> 代码演示：
>
> ```Python
> #1.Python中没有原生的数据类型表示枚举
> #a.字典
> COLOR = {
>     "RED":0,
>     "GREEN":1,
>     "BLUE":2,
>     "YELLOW":2
> }
> print(COLOR["GREEN"])
> COLOR["GREEN"] = 10
>
> #b.类
> class Color(object):
>     #类属性
>     RED = 0
>     GREEN = 1
>     BLUE = 2
> print(Color.RED)
> ```

#### 2.使用

> 代码演示：
>
> ```Python
> from enum import Enum,IntEnum,unique
>
> #2.
> """
> enum模块：提供了Enum【类】、IntEnum【类】、unique【装饰器】
> Enum【类】:通过定义一个类，继承自Enum，则该类就是一个枚举类
> IntEnum【类】：通过定义一个类，继承自IntEnum，则该类就是一个枚举类,限定枚举成员只能是整数类型
> unique【装饰器】：修饰一个类，则表示枚举类中的枚举成员只能是唯一的
> """
> #注意1：枚举类的类名一般全部大写
> #注意2:枚举中的成员本质上都是一个单例，不可实例化，不可更改，只能获取
> class COLOR(Enum):
>     #枚举成员/枚举常量
>     RED = 0
>     GREEN = 1
>     BLUE = 2
>
> #注意3：使用unique的装饰器之后，枚举成员的value必须是不可重复的
> @unique
> class WEEKDAY(IntEnum):
>     MON = 0
>     TUS = 1
>     WED = 2
>     #THU = "b"   #ValueError: invalid literal for int() with base 10: 'b'
>     #FRI = 1     #ValueError: duplicate values found in <enum 'WEEKDAY'>: FRI -> TUS
> #print(WEEKDAY.THU)
>
> #访问枚举成员
> #方式一
> print(COLOR.RED)
> print(type(COLOR.RED))
> #方式二
> red = COLOR(0)
> print(red)  #COLOR.RED
>
> #注意4：区别于普通类，枚举类的成员可以相互访问
> print(red.GREEN)   #COLOR.GREEN
> print(red.GREEN.BLUE.RED)  #COLOR.RED
> ```

### 四、高阶函数【掌握】

#### 1.map()

> 代码演示：
>
> ```Python
> """
> map(function,iterable)
> function:函数
> iterable：可迭代对象
> 作用：将传入的函数依次作用于可迭代对象中的每一个元素，并把结果【Iterator】返回
> """
> #需求1：给一个已知列表中的元素求平方
> def square(x):
>     return x ** 2
> list1 = [1,2,3,4,5]
> result1 = map(square,list1)
> #注意:map是一个类，表示一种数据类型，集合或者序列，使用类似于list，tuple，set
> print(result1)   #<map object at 0x000001EE25431DA0>
> print(type(result1))   #<class 'map'>
> print(list(result1))  #[1, 4, 9, 16, 25]
>
> result2 = map(lambda x:x ** 2,list1)
> print(list(result2))
>
> #str = 10
>
> #需求2：将整型元素的列表转换为字符串元素的列表
> #举例：[1,2,3,4]------>["1","2","3","4"]
> #str(1) ---- >字符串1
> #注意：在使用系统函数之前，最好不要出现同名的变量
> result3 = map(str,[1,2,3,4])
> print(list(result3))
>
>
> #需求3：已知两个整型列表，将两个列表中相同位置的元素相加，得到一个新的列表
> def add(x,y):
>     return  x  + y
> l1 = [1,2,3,4,5]
> l2 = [6,7,8,9,10]
>
> result4 = map(add,l1,l2)
> print(list(result4))
> ```

#### 2.reduce()

> 代码演示：
>
> ```Python
> from  functools  import  reduce
>
> """
> reduce(function,Iterable)  :通过函数对参数列表中的元素进行累积
> function:函数
> Iterable：可迭代对象，一般使用列表
> 工作原理：用传给reduce的function先作用于list中第一个和第二个元素，用得到的结果和list中第三个元素计算。。。
> reduce(add,[a,b,c,d])
> add(add(add(a,b),c),d)---->递归
> """
>
> #需求1;求一个已知列表中元素的和
> list1 = [1,2,3,4,5]
> def add(x,y):
>     return x + y
> result1 = reduce(add,list1)
> print(result1)
>
> result2 = reduce(lambda x,y:x + y,list1)
> print(result2)
>
> #需求2：将列表[1,3,5,7,9]变换成整数13579
> """
> 分析：
> 13 = 1 * 10 + 3
> 135 = 13 * 10 + 5
> 1357 = 135 * 10 + 7
> 13579 = 1357 * 10 + 9
> """
> list2 = [1,3,5,7,9]
> def fn(x,y):
>     return x * 10 + y
>
> result3 = reduce(fn,list2)
> print(result3)
>
> #需求3：
> #结合map函数，实现一个将str转换为int的函数   int()
>
> #思路：传进来一个字符串，返回一个对应的整数
> def strToInt(s):
>     digits = {"0":0,"1":1,"2":2,"3":3,"4":4}
>     return digits[s]
>
> #"23401"------>23401
> r0 = map(strToInt,"23401")
> print(list(r0))   #[2, 3, 4, 0, 1]
>
> r1 = reduce(fn,map(strToInt,"23401"))
> print(r1)   #23401
> print(type(r1))   #<class 'int'>
> ```

#### 3.filter()

> 代码演示：
>
> ```Python
> """
> filter(function,序列)
> 作用：通过指定的条件过滤列表中的元素
> 工作原理：将传入的函数依次作用于列表中的每一个元素，根据返回的是True还是False决定元素是否需要保留
> """
>
> #需求1：将列表中的偶数筛选出来
> list1 = [1,2,3,4,5,6,7,8,9]
> #作用：定义筛选的规则
> def func(num):
>     if num % 2 == 0:
>         return  True
>     return  False
>
> result1  = filter(func,list1)
> print(result1)
> print(list(result1))  #[2, 4, 6, 8]
> ```

#### 4.sorted()

> 代码演示：
>
> ```Python
> #1.普通排序
> #默认为升序排序，得到了的一个新的列表
> list1 = [4,5,23,3,5,7]
> result1 = sorted(list1)
> print(list1)
> print(result1)  #r[3, 4, 5, 5, 7, 23]
>
> #2.按照绝对值进行排序
> #默认为升序排序，排序的依据是所有元素的绝对值的大小
> list2 = [4,5,-23,3,-5,7]
> result2 = sorted(list2,key=abs)
> print(result2)  #[3, 4, 5, -5, 7, -23]
>
> #3.降序升序
> list3 = [4,5,23,3,5,7]
> result3 = sorted(list3,reverse=True)
> print(result3)
>
> #4.字符也可以实现排序
> list4 = ["f","a","k","z"]
> result4 = sorted(list4)
> print(result4)
>
> #5.自定义排序规则
> #默认为升序排序
> def myFunc(str):
>     return len(str)
> list5 = ["gsg","a","34535","efgg","562875678257fhjawhgj"]
> result5 = sorted(list5,key=myFunc)
> print(result5)
> ```

### 五、发邮件和发短信【扩展】

#### 1.发短信

> 互亿无线
>
> ```
> #发送短信
> #APIID：C11345804
> #APIKEY：735d183ae02189f678c26800ac19b03a
> ```

> 代码演示：
>
> ```Python
> # 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
> # 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
> # 注意事项：
> # （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。；
> # （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
> # （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
>
> # !/usr/local/bin/python
> # -*- coding:utf-8 -*-
> import http.client
> import urllib
>
> host = "106.ihuyi.com"
> sms_send_uri = "/webservice/sms.php?method=Submit"
>
> # 用户名是登录用户中心->验证码短信->产品总览->APIID
> account = "C11345804"
> # 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
> password = "735d183ae02189f678c26800ac19b03a"
>
> def send_sms(text, mobile):
>     params = urllib.parse.urlencode(
>         {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
>     headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
>     conn = http.client.HTTPConnection(host, port=80, timeout=30)
>     conn.request("POST", sms_send_uri, params, headers)
>     response = conn.getresponse()
>     response_str = response.read()
>     conn.close()
>     return response_str
>
>
> if __name__ == '__main__':
>     #需要接受短信的目标手机号
>     mobile = "18501970795"
>     text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
>
>     print(send_sms(text, mobile))
> ```

#### 2.发邮件

##### 2.1发送纯文本邮件

> 代码演示：
>
> ```Python
> #发送纯文本
> #发邮件的模块
> import  smtplib
> #邮件标题
> from  email.header import Header
> #邮件文本
> from  email.mime.text import MIMEText
>
> """
> user:用户名
> pwd:授权码
> sender：发送方
> receiver：接收方
> content：邮件的正文
> title：邮件的标题
> """
> def sendMail(user,pwd,sender,receiver,content,title):
>     mail_host = "smtp.163.com"   #163的SMTP服务器
>
>     #第一部分：准备工作
>     #1.将邮件的信息打包成一个对象
>     message = MIMEText(content,"plain","utf-8")   #内容，格式，编码
>     #2.设置邮件的发送者
>     message["From"] = sender
>     #3.设置邮件的接收方
>     #message["To"] = receiver
>     #join():通过字符串调用，参数为一个列表
>     message["To"] = ",".join(receiver)
>     #4.设置邮件的标题
>     message["Subject"] = title
>
>     #第二部分：发送邮件
>     #1.启用服务器发送邮件
>     #参数：服务器，端口号
>     smtpObj = smtplib.SMTP_SSL(mail_host,465)
>     #2.登录邮箱进行验证
>     #参数：用户名，授权码
>     smtpObj.login(user,pwd)
>     #3.发送邮件
>     #参数：发送方，接收方，邮件信息
>     smtpObj.sendmail(sender,receiver,message.as_string())
>
>     print("mail send successful!")
>
> if __name__ == "__main__":
>     mail_user = "18501970795@163.com"
>     mail_pwd = "yang0122"
>
>     mail_sender = "18501970795@163.com"
>     mail_receiver = ["1490980468@qq.com"]
>
>     email_content = "人生苦短，我用Python"
>     email_title = "Python1805"
>
>     sendMail(mail_user,mail_pwd,mail_sender,mail_receiver,email_content,email_title)
>
> ```

##### 2.2发送带有附件的邮件

> 代码演示：
>
> ```Python
> #发送带有附件的邮件
>
> import  smtplib
> from  email.mime.text import MIMEText
> from  email.mime.multipart import MIMEMultipart   #附件
> from  email.mime.application import MIMEApplication
>
> username = "18501970795@163.com"
> password = "yang0122"
> sender = username
> recevier = ",".join(["1490980468@qq.com"])
>
> #创建一个关于附件的对象
> msg = MIMEMultipart()
> msg["From"] = sender
> msg["To"] = recevier
> msg["Subject"] = "带有附件的邮件"
>
> #创建一个关于正文的对象
> text = MIMEText("today is a good day")
>
> #将附件和文本做整合
> msg.attach(text)
>
> #设置附件部分
> file = open("dog.jpg","rb")
> imagePart = MIMEApplication(file.read())
> #设置图片的相关信息
> imagePart.add_header("Content-Disposition","attachment",filename="dog.jpg")
> msg.attach(imagePart)
>
> smtpObj = smtplib.SMTP()
> smtpObj.connect("smtp.163.com")
> smtpObj.login(username,password)
> smtpObj.sendmail(sender,recevier,msg.as_string())
>
> #退出服务器
> smtpObj.quit()
> ```