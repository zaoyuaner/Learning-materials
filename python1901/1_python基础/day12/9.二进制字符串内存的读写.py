#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
from io import BytesIO

#在内存中读取二进制文件/字符串
bio = BytesIO()
bio.write("中国".encode("utf-8"))
print(bio.getvalue())


bio2 = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(bio2.read().decode("utf-8"))

with open("img.jpg","rb") as f:
    str1 = f.read()

bio3 = BytesIO(str1)
print(bio3.read())