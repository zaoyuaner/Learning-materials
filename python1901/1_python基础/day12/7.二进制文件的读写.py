#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
读取二进制文件的时候，mode：rb

'''
'''
完成一张图片的复制。
'''
with open("demo.txt","rb") as f:
    print(f.read().decode("utf-8"))

with open("demo.txt","wb") as f2:
    f2.write("中国".encode("utf-8"))


def copyimg(img1,img2):
    with open(img1,"rb") as f1:
        with open(img2,"wb") as f2:
            str1 = f1.read(1024)
            while str1 != b"":
                f2.write(str1)
                str1 = f1.read(1024)

copyimg("img.jpg","img2.jpg")

