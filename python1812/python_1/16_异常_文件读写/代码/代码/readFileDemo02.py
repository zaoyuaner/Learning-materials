#1.读取文件的简写形式
#with open()  as 变量

#好处：可以自动关闭文件，避免忘记关闭文件导致的资源浪费
path = "致橡树.txt"
with open(path,"r",encoding="gbk") as f:
    result = f.read()
    print(result)

#2.
try:
    f1 = open(path,"r",encoding="gbk")
    print(f1.read())
except FileNotFoundError as e:
    print("文件路径错误",e)
except LookupError as e:
    print("未知的编码格式",e)
except UnicodeDecodeError as e:
    print("读取文件解码错误",e)
finally:
    if f1:
        f1.close()