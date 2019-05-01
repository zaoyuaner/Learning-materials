# 建立TCP Sever服务器
import socket

# 1.建立socket对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2.绑定地址和端口
server.bind(("127.0.0.1",8001))        # 端口使用1023之后的端口
print(server)
# 3.监听客户端请求  参数是最大连接数(消耗资源)
server.listen(5)

print("server start......")

# 服务器
while True:
	# 接收客户端请求  # 获取客户端socket对象,和ip地址,是一个二元组
	server ,ip = a = server.accept()        # 元组解包
	# print(a)
	# print(server)
	print(server.recv(1024).decode("UTF-8"))
	server.send("欢迎致电10086,请选择你要办理的业务,1:业务咨询,2:话费咨询".encode("UTF-8"))

	while True:
		res = server.recv(1024).decode("utf-8")
		print(res)
		if res == "1":
			server.send("你选择的是业务咨询,办理宽带业务请按1".encode("utf-8"))
		elif res =="2":
			server.send("你剩余的话费是1000元".encode("utf-8"))
		else:
			break
	server.close()



