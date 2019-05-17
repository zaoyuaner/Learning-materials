# 编解码
# 因为python对中文支持不是特别好,所以需要进行编解码来处理中文

# .encode() 编码 默认UTF-8
str1 = "你好 hello 千峰"
print(str1.encode())      # b'\xe4\xbd\xa0\xe5\xa5\xbd hello \xe5\x8d\x83\xe5\xb3\xb0'
# 返回一个二进制的字节对象
print(str1.encode("UTF-8"))
print(str1.encode("gbk"))      # 使用特定的编码格式编码

# .decode()  解码操作,默认utf-8   由byte转成字符串对象
print(b'\xe4\xbd\xa0\xe5\xa5\xbd hello \xe5\x8d\x83\xe5\xb3\xb0'.decode())

# b' byte 字节对象,计算机底层会转成字节型传输

# 获取字符的ASCII码
# ord()  由字符串转为ASCII码        大小写转换相差32,小写字母较大
print(ord("A"))     # 65          大写字母ASCII码的阈值  [65,65+26-1(90)]
print(ord("0"))     # 48          数字ASCII码的阈值     [48,57]
print(ord("a"))     # 97          小写字母ASCII码的阈值  [97,97+26-1(122)]

# chr() 由ASCII码转为字符串
print(chr(65))      # A
print(chr(48))      # "0" != 0
print(chr(97))      # a

