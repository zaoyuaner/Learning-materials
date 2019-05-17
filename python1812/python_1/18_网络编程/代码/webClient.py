# 利用socket编程实现一个简单web请求
import socket

# 1.建立socket对象
# 第一个参数：地址簇，AF_INET ipv4
# 第二个参数:SOCK_STREAM tcp协议使用
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2 建立连接
#（ip或者域名,端口）
address = ('www.163.com',80)
client.connect(address)

# 3.向服务器发起请求
"""
http请求格式：
GET / HTTP/1.1   请求行
Host: www.163.com  请求头
Connection: close
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
请求头结束标志是：\r\n\r\n
"""
# 网络上数据传输都使用的二进制
client.send(b"GET / HTTP/1.1\r\nHost: www.163.com\r\nConnection: close\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36\r\n\r\n")

data = []
while True:
    # 4.接收数据
    # 参数是接收数据的大写，单位是字节
    tmp = client.recv(1024)
    if tmp:  # 如果数据存在
        data.append(tmp)   # 添加到列表
    else:
        break   # 如果接收数据为空，表示接收完毕

# 显示接收到数据
# print(data)
s1 = b''.join(data)
s1 = s1.decode('GBK')
with open('1632.html','w',encoding='GBK') as fp:
    fp.write(s1)
print(s1)
# 5.关闭客户端
client.close()