#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

def qiuhe(n):
    res = 0
    for x in range(1,n+1):
        res += x
    return res


def qiujiecheng(n):
    jie=1
    for x in range(1,n+1):
        jie *= x

    return jie


def jiechenghe(n):
    res = 0
    jie = 1
    for x in range(1,n+1):
        jie *= x
        res += jie
    return res

