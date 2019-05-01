#一、打开文件
"""
open(path,flag[,encoding,errors])
path:指定文件的路径【绝对路径和相对路径】
flag:打开文件的方式
    r:只读、
    rb:read binary,以二进制的方式打开，只读【图片，视频，音频等】
    r+:读写

    w:只能写入
    wb:以二进制的方式打开，只能写入【图片，视频，音频等】
    w+:读写

    a:append,如果一个文件不为空，当写入的时候不会覆盖掉原来的内容
encoding：编码格式：gbk,utf-8
errors:错误处理
"""
path = r"C:\Users\Administrator\Desktop\SZ-Python1805\Day15\笔记\致橡树.txt"
#调用open函数，得到了文件对象
f = open(path,"r",encoding="gbk")

"""
注意：
a.以r的方式打开文件时，encoding是不是必须出现
    如果文件格式为gbk,可以不加encoding="gbk"
    如果文件格式为utf-8,必须添加encoding="utf-8"
b。如果打开的文件是图片，音频或者视频等，打开方式采用rb,但是，此时，不能添加encoding="xxx"
"""

#二、读取文件内容
#1.读取全部内容   ***********
#str = f.read()
#print(str)

#2.读取指定的字符数
#注意：如果每一行的结尾有个"\n",也被识别成字符
"""
str1 = f.read(2)
print(str1)
str1 = f.read(2)
print(str1)
str1 = f.read(2)
print(str1)


#3.读取整行，不管该行有多少个字符    *********
str2 = f.readline()
print(str2)
str2 = f.readline()
print(str2)
"""

#4.读取一行中的指定的字符
#str3 = f.readline(3)
#print(str3)

#5.读取全部的内容，返回的结果为一个列表，每一行数据为一个元素
#注意：如果指明参数，则表示读取指定个数的字符
str4 = f.readlines()
print(str4)

#三、关闭文件
f.close()








