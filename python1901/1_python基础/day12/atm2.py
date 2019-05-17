#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
ATM:
属性：所有用户信息
行为：
1.取款
2.存款
3.转账
4.改密
5.登陆
6.开户
7.锁卡
8.解锁
9.退出
'''
import random
from day12.atmdemo.card import Card
from day12.atmdemo.user import User


class ATM:
    userDict = {}

    @staticmethod
    def welcome():
        print('''
    **********************
    *                    *
    *  welcome to bank   *
    *                    *
    **********************
        ''')

    @staticmethod
    def choice():
        print('''
    **********************
    *  1.登陆   2.开户    *
    *  3.查询   4.取款    *
    *  5.存款   6.退出    *
    *  7.锁卡   8.解锁    *
    *  9.转账   0.改密    *
    **********************
        ''')
        num = input("请输入您要选择的项目：")
        return num


    @classmethod
    def getCardNum(cls):
        cardnum = ""
        while True:
            for x in range(6):
                cardnum += str(random.randrange(10))
            if cardnum not in list(cls.userDict):
                return cardnum
            else:
                continue

    @classmethod
    def openUser(cls):
        name = input("请输入您的姓名：")
        idcard = input("请输入您的身份证号：")
        phonenum = input("请输入您的电话号码：")
        money = int(input("请输入您的预存余额："))
        if money>0:
            psd = input("请设置您的密码：")
            psd2 = input("请确认您的密码：")
            if psd == psd2:
                #获取卡号
                cardnum = cls.getCardNum()
                #创建卡对象
                card = Card(cardnum,psd,money)
                #创建用户对象
                user = User(name,idcard,phonenum,card)
                cls.userDict[cardnum] = user
                return cardnum
            else:
                print("两次输入密码不一致，开户失败！！！")
                return
        else:
            print("预存余额有误，开户失败！！")
            return


    @classmethod
    def login(cls):
        cardnum = input("请输入卡号：")
        #判断卡号是否存在
        if cardnum not in list(cls.userDict):
            print("卡号不存在，请查证登陆。。。")
        else:
            #若卡号存在，通过卡号获取到对象
            user = cls.userDict.get(cardnum)
            #判断卡是否已经锁定
            if not user.card.islock:
                #最多输入三次密码
                for x in range(1,4):
                    psd = input("请输入您的密码：")
                    #判断密码是否正确
                    if user.card.password == psd:
                        print("恭喜你登陆成功")
                        #登陆成功的时候返回卡号
                        return cardnum
                    else:
                        #显示剩余的机会
                        print("密码错误，您还剩%d次机会"%(3-x))

                #cls.userDict[cardnum] 获取到的用户
                #.card 获取用户身上的卡对象
                #.islock 获取卡的属性
                cls.userDict[cardnum].card.islock = True
                print("卡已锁定。。。")
                return
            else:
                print("卡已锁定，请解锁后登陆。。。")
                return



    @classmethod
    def search(cls,cardnum):
        print("您当前的余额为%d"%cls.userDict[cardnum].card.money)



    @classmethod
    def transMoney(cls,cardnum):
        cardnum2 = input("请输入对方账户卡号：")
        if cardnum2 not in list(cls.userDict):
            print("此账号不存在，请查证后再转。。。")
            return
        else:
            if cardnum2 == cardnum:
                print("此账户为本人账户无需转账。。。")
                return

            mon = int(input("请输入您要转账的金额："))
            if mon>0:
                if cls.userDict[cardnum].card.money>=mon:
                    # 转账
                    cls.userDict[cardnum].card.money -= mon
                    cls.userDict[cardnum2].card.money += mon
                    print("恭喜你转账成功，当前余额为%d"%cls.userDict[cardnum].card.money)
                else:
                    print("余额不足转账失败。。。")
                    return
            else:
                print("金额非法。。。")
                return