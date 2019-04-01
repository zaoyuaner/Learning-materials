#邮编
num = input("请输入邮编：")  #str

path = "youbian.txt"

#读取文件
f = open(path,"r",encoding="utf-8")

str = f.readline()

while str:
    newStr = str[1:]
    if newStr.startswith(num):
        print(str[9:-4])
    str = f.readline()
