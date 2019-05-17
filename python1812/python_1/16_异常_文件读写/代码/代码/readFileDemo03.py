#1.
f = open("dog.jpg","rb")

result = f.read()
print(result)

f.close()

#2
with open("dog.jpg","rb") as f1:
    f1.read()

#注意：读取的是二进制文件，读取到的内容为\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x0