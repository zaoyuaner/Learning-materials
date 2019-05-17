#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
属性：name、身份证号码、电话号码、卡
'''
class User:
    def __init__(self,name,idcard,phonenum,card):
        self.name = name
        self.idcard = idcard
        self.phonenum = phonenum
        self.card = card

