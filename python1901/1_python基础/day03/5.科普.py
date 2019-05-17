#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

a = ""  #0 False None ""  []  {} ()
#
if a:
    print("真")
else:
    print("假")

'''
在判断的过程中，取值为假的：0、False、None、"",[],{},()
'''

print(False and 8)
print(6 and True and 7)
print(8 and 6)
print(0 and False)