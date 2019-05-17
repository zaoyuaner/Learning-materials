import  socket

#1.创建socket对象
clientSocket = socket.socket()

#2.发起连接请求
#connect(元组)
#（host,port）ip地址和端口号需要和服务端中绑定的ip地址以及端口号保持一致
ip_port = ("10.36.131.32",6666)
clientSocket.connect(ip_port)

#3.发送数据
#sendall(string) ,字节类型的字符串【编码的过程】
clientSocket.sendall(bytes("hello你好啊",encoding="utf-8"))

#4.关闭客户端
clientSocket.close()


