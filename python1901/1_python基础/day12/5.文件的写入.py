#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
f = open(path,"w")
mode:w写入  a：追加
使用w模式，若文件不存在则创建文件，若文件存在的时候，覆盖之前文件之前的内容。
使用a模式，若文件不存在，则创建文件，若文件存在，则在原有文件的基础上追加新的内容。


注意：写入完毕之后必须调用close的方法
因为当我们执行写入的时候，操作系统并没有直接把我们的数据写入到磁盘，
而是放在内存中缓存起来，等cpu空闲的时候写入，当我们调用close方法
的时候，操作系统才保证将我们的数据全部写入到磁盘中，若忘记close的方法
有可能发生数据丢失的情况
'''
dict1 = {"1":1,"2":2}
f = open("demo1.txt","a")
# f.write("hello world2")
list1 = ["hello","good","nice"]
for line in list1:
    f.write(line+"\t")
f.close()

'''
需求：打开一个文件读取这个文件的内容，并且写入到新的文件中。
'''

def copyfile(path1,path2):
    f1 = open(path1,"r",encoding="utf-8")
    f2 = open(path2,"w",encoding="utf-8")
    line = f1.readline()
    while line !="":
        f2.write(line)
        line = f1.readline()
    f1.close()
    f2.close()

path1 = r"E:\python\python1901\day12\atmdemo\atm.py"
copyfile(path1,"atm2.py")
