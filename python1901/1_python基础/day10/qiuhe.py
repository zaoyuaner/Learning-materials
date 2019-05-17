#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

'''
偶数和
'''
def func1(n):
    res = 0
    for x  in range(0,n+1,2):
        res += x
    return  res

def jisu(n):
    res = 0
    for x in range(1,n+1,2):
        res += x
    return res


def beihe(n,m):
    res = 0
    for x in range(n+1):
        if x%m == 0:
            res += x
    return res




