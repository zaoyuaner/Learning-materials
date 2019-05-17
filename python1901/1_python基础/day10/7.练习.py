#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
需求：同桌买了一部华为mateX跟你炫耀.（17000）
人类：
属性：name，age、手机，money
行为：炫耀

手机类：
属性：品牌、型号、价格
行为：折叠、双面拍照
'''
class Phone():
    def __init__(self,pinpai,xinghao,price):
        self.pinpai = pinpai
        self.xinghao = xinghao
        self.price = price

    def zhedie(self):
        print("%s%s屏幕可180度折叠哦。。。"%(self.pinpai,self.xinghao))

    def paizhao(self):
        print("拍照可以双面成像哦")

class Person():
    def  __init__(self,name,age,phone,money):
        self.name = name
        self.age = age
        self.phone = phone
        self.money = money

    def xuanyao(self):
        print("瞧瞧我的新手机哦，手机的新功能给你演示一下哦！！")
        self.phone.zhedie()
        self.phone.paizhao()



if __name__ == "__main__":
    phone = Phone("华为","mateX",17000)
    per = Person("小明",23,phone,100000000)
    per.xuanyao()

