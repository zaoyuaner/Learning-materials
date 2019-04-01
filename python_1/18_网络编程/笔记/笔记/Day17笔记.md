### 一、上堂回顾

> 知识点回顾：
>
> ​	1.枚举类
>
> ​		有限的，特定的
>
> ​	2,.高阶函数
>
> ​		map:
>
> ​		reduce；类似于递归
>
> ​		filter:过滤【True和False】
>
> ​		sorted:默认升序【关键字key】

### 二、网络编程

#### 1.网络编程基础

##### 1.1概念

> 计算机网络：把分布在不同区域的计算机【设备】与专门的一些外部设备通过通信线路相关联，形成一个网络系统，从而使得计算机之间可以共享数据
>
> 网络编程：同一个网络中不同的机器之间的通信

##### 1.2计算机之间需要通信的必要条件

> ip地址，端口，网络协议
>
> 1.>ip地址
>
> ​	互联网协议地址【Internet Protocol Address】，是联网设备和互联网之间的唯一标识，在同一个网段中，ip地址是唯一的
>
> ​	ip地址是数字型，是一个32位的整数，
>
> ​		举例：10.36.131.32：32位的整数，分成4个8位的二进制，将二进制转换为0~255之间的十进制整数
>
> ​	分类：
>
> ​	a.形式分类
>
> ​		ipv4:分为4段
>
> ​		ipv6:分为6段
>
> ​	b.功能分类
>
> ​		A类：保留给政府机构，1.0.0.1~126.255.255.255
>
> ​		B类：分配中型企业，128.。。。。~191.。。
>
> ​		C类：分配个人,192...~223
>
> ​		D类：组播，224~239
>
> ​		E类：实验，240~255
>
> ​	127.0.0.1：回送地址，一般指的是本机的ip，localhost，一般用来进行测试
>
> ​	总结：ip地址可以唯一确定网络上的一个通信实体，但是一个通信实体上可能有很多的应用程序，可以同时提供网络服务，此时还需要借助于端口进行区分
>
> 2>端口
>
> ​	数据的发送和接收都需要通过端口，端口号用于唯一标识通信实体上进行网络通信的程序
>
> ​	注意：同一台机器上的不同的应用程序不能占用同一个端口，端口的范围：0~65535
>
> ​	作用：ip地址结合端口号，就可以唯一的确定一个网络中唯一一台计算机上的一个应用程序
>
> ​	分类：
>
> ​		a.公认端口：0~1023
>
> ​		b.注册端口：1025~49151
>
> ​		c.动态端口或者私有端口:1024~65535
>
> ​	常用端口：
>
> ​	mysql:3306
>
> ​	oracle:1521
>
> ​	tomcat:8080
>
> ​	qq；4000
>
> 3>网络协议
>
> ​	http:被动式协议
>
> ​	tcp
>
> ​	udp
>
> ​	tcp/ip：互联网协议

#### 2.TCP编程

> Transmission Control Protocol，传输控制协议，是一个传输层的通信协议
>
> 客户端/服务端：套接字【socket】，程序通常通过套接字向网络发出请求或者应答网络请求，使得两台设备之间进行通信
>
> 理解;打开了一个网络连接，必须知道ip地址，端口号，协议
>
> ​	特点：
>
> ​	a.安全的【确保接收方完全正确的接收数据】
>
> ​	b.面向连接【数据传输之前必须要建立连接】
>
> ​	c.传输的效率较低【面向连接需要耗时】
>
> ​	d.一旦连接建立，双方可以按照指定的格式发送数据【大小没有限制】
>
> 使用经典三次握手建立连接
>
> ​	a.客户端向服务端发起请求
>
> ​	b.服务端收到请求之后，会给客户端一个响应
>
> ​	c.客户端收到服务端的响应之后，给服务端回复一个确认信息
>
> 总结：使用tcp实现数据的发送和接收需要有发送方和接收方，但是两个通信实体之间没有明确的客户端或者服务端之分，在两个通信实体在建立连接之前，必须有一个通信实体先做出主动姿态，主动发起请求

##### 2.1socket通信流程

> 代码演示：
>
> server:
>
> ```Python
> #服务端流程描述
> import  socket
>
> #1.创建服务端的socket对象
> serverSocket = socket.socket()
>
> #2.为socket绑定端口和ip地址
> """
> bind(元组)，将端口号和ip地址创建元组，然后传参
> (host,port)
> """
> #查看ip地址：在终端输入ipconfig命令
> ip_port = ("10.36.131.32",6666)
> serverSocket.bind(ip_port)
>
> #3.服务端监听请求，随时准备接受客户端发来的连接
> """
> listen(backlog)
> backlog:在拒绝连接之前，可以挂起的最大连接数量
> 注意：不能无限大
> """
> serverSocket.listen(5)
>
> print("server waiting~~~~~")
>
> #4.服务端接收到客户端的请求，被动打开进行连接
> #accept()；在连接的时候，会处于阻塞状态
> #返回值：conn,address,conn表示连接到的套接字对象，address表示连接到的客户端的地址
> conn,addr = serverSocket.accept()
>
> #5.服务端接收消息
> """
> recv(size)
> 可以一次性接收到多大的数据
> """
> client_data = conn.recv(1024)
> print(str(client_data,"utf-8"))
>
> #6.服务端关闭
> serverSocket.close()
> ```
>
> client:
>
> ```Python
> import  socket
>
> #1.创建socket对象
> clientSocket = socket.socket()
>
> #2.发起连接请求
> #connect(元组)
> #（host,port）ip地址和端口号需要和服务端中绑定的ip地址以及端口号保持一致
> ip_port = ("10.36.131.32",6666)
> clientSocket.connect(ip_port)
>
> #3.发送数据
> #sendall(string) ,字节类型的字符串【编码的过程】
> clientSocket.sendall(bytes("hello你好啊",encoding="utf-8"))
>
> #4.关闭客户端
> clientSocket.close()
> ```

##### 2.2客户端和服务端的数据交互

> 代码演示：
>
> server:
>
> ```Python
> import  socket
>
> server = socket.socket()
>
> server.bind(("10.36.131.32",6666))
>
> server.listen(5)
>
> conn,address = server.accept()
>
> print("连接成功")
>
> while True:
>     clientData = conn.recv(1024)
>     result = clientData.decode("utf-8")
>     print("客户端对服务端说：",result)
>
>     if result == "bye" or result == "再见":
>         break
>
>     sendData = input("请输入要给回复客户端的数据：")
>     conn.send(sendData.encode("utf-8"))
>
> server.close()
> ```
>
> client:
>
> ```Python
> import  socket
>
> client = socket.socket()
>
> client.connect(("10.36.131.32",6666))
>
> while True:
>     sendData = input("请输入要发送给服务端的数据：")
>     client.send(sendData.encode("utf-8"))
>
>     serverData = client.recv(1024)
>     result = serverData.decode("utf-8")
>     print("服务端回复：",result)
>
>     if result == "bye":
>         break
>
> client.close()
> ```

#### 3.UDP编程

> User Datagram Protocol,用户数据包协议
>
> 特点：
>
> ​	a.不安全的
>
> ​	b.无连接
>
> ​	c.效率高，速度快
>
> ​	d.对数据的大小是有限制的，每个被传输的数据包的大小不超过64k

### 三、反射【扩展】

> 通过字符串操作对象中的字段【属性】
>
> 反射机制：一种基于字符串的事件驱动
>
> 代码演示：
>
> ```Python
> #xxxxattr
>
> #1.getattr
> class Person(object):
>     def __init__(self,name,age):
>         self.__name = name
>         self.age = age
>
>     def show(self):
>         print("show")
>
>     @classmethod
>     def func(cls):
>         print("func")
>
>
> #创建一个Person对象
> p = Person("张三",10)
> #print(p.name)
> print(p.age)
>
> #问题：已知字符串"age",获取10
> #方式一
> b = "age"
> if b == "age":
>     print(p.age)
>
> #方式二
> print(p.__dict__)
> str = "age"
> print(p.__dict__[str])
>
> #方式三
> """
> getattr(object,name,default) 获取某个对象的某个属性对应的值
> object：对象
> name：对应属性的字段名，使用字符串表示
> default：如果指定字段不存在，则一个返回一个默认值
> """
> value1 = getattr(p,"age","hello")
> print(value1)
>
> #获取成员方法
> result1 = getattr(p,"show")
> print(result1)
>
> #获取类方法
> result2 = getattr(Person,"func")
> print(result2)
>
>
> #2.hasattr    isxxx:判断一个指定的对象中是否有指定的成员
> print(hasattr(p,"score"))
>
> #3.setattr:给指定字段进行赋值
> setattr(p,"age",30)
>
> #4.delattr:删除指定字段
> #del 变量名
> delattr(p,"age")
> ```
>
> 应用：
>
> ```Python
> import  textDemo
> #from textDemo import  music,image
>
> str = input("请输入对应的操作指令：")
> """
> if str == "home":
>     textDemo.home()
> elif str == "music":
>     textDemo.music()
> elif str == "image":
>     textDemo.image()
> """
>
> #使用反射解决
> #判断模块中是否有对应的功能
> res = hasattr(textDemo,str)
> if res:
>     #获取出来
>     f = getattr(textDemo,str)
>     print(f)
>     print(f())
>
> else:
>     print("没有指定的功能")
> ```

