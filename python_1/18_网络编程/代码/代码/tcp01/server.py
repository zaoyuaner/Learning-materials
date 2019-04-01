#服务端流程描述
import  socket

#1.创建服务端的socket对象
serverSocket = socket.socket()

#2.为socket绑定端口和ip地址
"""
bind(元组)，将端口号和ip地址创建元组，然后传参
(host,port)
"""
#查看ip地址：在终端输入ipconfig命令
ip_port = ("10.36.131.32",6666)
serverSocket.bind(ip_port)

#3.服务端监听请求，随时准备接受客户端发来的连接
"""
listen(backlog)
backlog:在拒绝连接之前，可以挂起的最大连接数量
注意：不能无限大
"""
serverSocket.listen(5)

print("server waiting~~~~~")

#4.服务端接收到客户端的请求，被动打开进行连接
#accept()；在连接的时候，会处于阻塞状态
#返回值：conn,address,conn表示连接到的套接字对象，address表示连接到的客户端的地址
conn,addr = serverSocket.accept()

#5.服务端接收消息
"""
recv(size)
可以一次性接收到多大的数据
"""
client_data = conn.recv(1024)
print(str(client_data,"utf-8"))

#6.服务端关闭
serverSocket.close()


