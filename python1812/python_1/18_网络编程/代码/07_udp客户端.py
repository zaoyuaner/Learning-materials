# 客户端
# UDP协议不用连接   直接发送到指定IP
import socket
# 创建对象
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 发送
client.sendto("helloworld".encode("utf-8"),("127.0.0.1",9999))
data, address= client.recvfrom(1024)
print(data.decode("utf-8"))
client.close()