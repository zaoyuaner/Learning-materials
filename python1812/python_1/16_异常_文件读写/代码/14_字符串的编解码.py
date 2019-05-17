# 字符串类型和字节类型转换过程
#     字符串类型转换为字节类型：编码，encode
#
# ​	  字节类型转换为字符串类型：解码，decode

s1 = b"hello"           # bytes
s2 = "hello"            # str
print( type(s1),type(s2))

# python转字节字符串
res = s2.encode("utf-8")   # 字符转字节
print(type(res),res)

# 字节字符串转python字符串
res = s1.decode("utf-8")
print( type(res),res)      # 字节转字符

# 二进制文件操作
with open("04.txt","wb") as fp:
	fp.write("中国".encode("utf-8"))

with open("04.txt","rb") as fp:
	data = fp.read()
	print(len(data),data)
	print(data.decode('utf-8'))