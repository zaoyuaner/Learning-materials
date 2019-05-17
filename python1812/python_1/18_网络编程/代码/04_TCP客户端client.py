import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8001))     # 本机地址
client.send("你好".encode("utf-8"))
while True:
	tmp = client.recv(1024)
	print(tmp.decode("utf-8"))
	num = input("请输入你的选择:")
	client.send(num.encode("utf-8"))
	if num == "n":
		break

client.close()

