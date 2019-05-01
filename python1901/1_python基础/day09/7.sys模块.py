#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

import sys


'''
sys.path

返回python内建规则查找的一个列表
'''
print(sys.path)

'''
sys.platform 
获取当前环境平台的信息
'''
print(sys.platform)

'''
sys.argv
功能：可以从外部往内部传递参数
argv[0] 当前文件的绝对路径
argv[1]  通过外部向内部传递的参数
'''
print(sys.argv)
