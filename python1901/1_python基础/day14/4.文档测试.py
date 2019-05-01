#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import doctest
'''
文档测试：可以提取函数中注释，并且执行，
注意：注释应该按照严格python交互模式的格式书写。
'''

def sum1(a,b):
    '''
    :param a:
    :param b:
    :return: a+b
    >>> print(sum1(1,2))
    4
    '''
    return a+b
print(sum1(1,2))
doctest.testmod()


