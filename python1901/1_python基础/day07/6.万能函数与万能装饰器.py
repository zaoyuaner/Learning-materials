#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

def outer(f):
    def inner(*args,**kwargs):
        pass
        return f(args,kwargs)
    return inner


@outer
def func(*args,**kwargs):
    pass
    return

