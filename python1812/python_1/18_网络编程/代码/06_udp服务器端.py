# 服务器端
import socket

# 1.建立socket对象
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2.绑定地址
server.bind(("127.0.0.1",9999))

print("server start.........")
while True:
	data , address = server.recvfrom(1024)
	print(address)
	print(data.decode("utf-8"))
	server.sendto("西瓜".encode("utf-8"),address)

