# Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。
# 在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，
# 对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。
# Socket:套接字，作用：可以发送和接收数据

# 利用socket编程实现一个简单的web请求
import socket

# 1.建立socket对象(客户端)
# 第一个参数: 地址簇,AF_INET(Ipv4)
# 第二个参数: SOCK_STREAM(TCP协议使用)  UDP协议为SOCK_DGRAM
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2.建立链接: (IP地址|域名,端口)  元组
address = ("www.163.com",80)
client.connect(address)


# 3.向服务器发起请求 send
"""
http请求格式
GET / HTTP/1.1  请求行       #  GET /  GET前面没有空格后面有个空格(严格的协议格式).代表请求首页
Host: www.hao123.com  请求头
Connection: close
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
请求结束标识\r\n\r\n
"""
# 网络上数据传输都是用的二进制
client.send(b"GET / HTTP/1.1\r\nHost: www.163.com\r\nConnection: close\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36\r\n\r\n")

# 4.接收数据(分块接收)
data = []
while 1:
	# 接收数据
	# 参数: 接收数据的大小KB
	tmp = client.recv(1024)
	# 当tmp为空时,没有数据就break
	if tmp:
		data.append(tmp)
	else:
		break

# 测试接收到的数据
print(data)
# 拼接解码列表中的数据
s1 = b"".join(data)
s1 = s1.decode("GBK")
with open("163.html","w",encoding="GBK") as fp:
	fp.write(s1)
print(s1)

# 5.关闭客户端
client.close()



