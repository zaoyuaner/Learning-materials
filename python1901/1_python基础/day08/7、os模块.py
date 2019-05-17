#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
os模块操作我们的文件，以及文件路径的。
'''
import os

'''
os.getcwd()
功能：获取当前文件所在的目录的绝对路径

绝对路径：
window：以磁盘开头E:、C: ，以\\开头的
mac：以/开头的
相对路径：文件开头、以.开头或者..开头的

os.listdir(path)
功能：列举目录下所有的文件，以列表的方式返回，【只返回文件名】，
若没指定path，则列举当前目录下所有的文件
注意：path路径一定存在，若不存在则报错

os.path.abspath(path)
注意：此方法没有判断文件是否存在，只做了一个路径拼接，
若path是相对路径，则使用当前目录所在的路径拼接上指定path即可
若path是绝对路径，则使用直接path路径。

os.path.split(path)
功能:将文件路径分割成文件夹与文件名，以元组的方式返回.
本质：以path最后的一个“\”进行分割，只分割1次返回。

os.path.join(path,paths)
功能:对指定的路径进行拼接，返回拼接后的结果。
注意：当paths中出现绝对路径的时候，它会删除拼接的结果，只返回绝对路径的结果。

os.path.dirname(path)
功能:只返回目录的部分

os.path.basename(path)
功能:只返回文件的部分【只返回了文件名】

os.path.getsize(path)
功能:获取指定文件的大小，单位字节。目录的获取不了【但是不会报错】

os.path.isdir(path)
功能：判断指定文件是否为目录，若是则返回True，否则返回False

os.path.isfile(path)
功能:判断指定路径是否为文件，若是返回True，否则返回False

os.path.exists(path)
功能：判断指定路径是否存在，若存在返回True，否则返回False。
'''
# print(os.getcwd())
# path =r"D:\python new project\python1901\day19zuoye"
# print(os.listdir(path))
# print(os.path.split(path))
# path = r"E:\python\python1901"
'''
使用递归遍历目录：
1.列举出指定目录下所有的文件
2.进行路径拼接，判断该文件是否为目录
3.若为目录继续列举，若不为目录则打印文件名
'''

# print(os.listdir(path))

# print(os.path.abspath("demo.py"))
# print(os.path.abspath(".\demo.py"))
# print(os.path.abspath("..\demo.py"))
# print(os.path.abspath("\demo.py"))
# print(os.path.abspath("c:\demo.py"))

path3 = r"E:\python\python1901\day08\\"
path4 = r"E:\python\python1901\day08"
path5 = r"E:\python\python1901\day08\demo.py"
path6 = r"."
path7 = r"E:\python\python1901\\demo.py"

print(os.path.basename(path3))
print(os.path.basename(path4))
print(os.path.basename(path5))
print(os.path.basename(path6))
print(os.path.basename(path7))

# print(os.path.dirname(path3))
# print(os.path.dirname(path4))
# print(os.path.dirname(path5))
#
# print(os.path.basename(path3))
# print(os.path.basename(path4))
# print(os.path.basename(path5))
# print(os.path.basename(path6))
#
# print(os.path.split(path3))
# print(os.path.split(path4))
# print(os.path.split(path5))
# print(os.path.split(path6))

# path4 = r"E:\python\python1901\day08\1.作业.py"
# # path5 = r"E:\python\python1901\day08\demo.py"
# # path6 = r"E:\python\python1901\day07"
# # path7 = r"E:\python\python1901\day09"


# print(os.path.getsize(path4))
# print(os.path.getsize(path5))
# print(os.path.getsize(path6))
# print(os.path.getsize(path7))

# print(os.path.exists(path4))
# print(os.path.exists(path5))
# print(os.path.exists(path7))

# print(os.path.isdir(path4))
# print(os.path.isdir(path6))
# print(os.path.isdir(path7))
#
# print(os.path.isfile(path7))
# print(os.path.join(path4,"demo.py"))
# print(os.path.join(path4,"demo.py","demo2.txt"))
# print(os.path.join(path4,"demo.py","\demo2.txt"))

