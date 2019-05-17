#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''

属性：卡号、密码、余额、锁卡状态
'''
class Card:
    def __init__(self,cardnum,password,money,islock=False):
        self.cardnum = cardnum
        self.password = password
        self.money = money
        self.islock = islock