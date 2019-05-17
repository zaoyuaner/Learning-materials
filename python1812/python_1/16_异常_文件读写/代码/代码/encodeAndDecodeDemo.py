path = "file2.txt"

#编码:字符串----》字节
with open(path,"wb") as f1:
    str = "today is a good day 今天是个好天气"
    f1.write(str.encode("utf-8"))

#解码：字节----->字符串
with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))

    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))

