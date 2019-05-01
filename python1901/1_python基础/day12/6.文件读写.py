#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
系统封装的读写文件的语句
with open(path,mode,encoding,errors) as f：
    #f.read()
    #f.write()
'''

with open("atm2.py",encoding="utf-8") as f:
    print(f.read())