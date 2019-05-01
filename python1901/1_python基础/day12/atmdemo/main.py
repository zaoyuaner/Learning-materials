#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

from day12.atmdemo.atm import ATM


'''
*  1.登陆   2.开户    *
*  3.查询   4.取款    *
*  5.存款   6.退出    *
'''
if __name__ == "__main__":
    ATM.welcome()
    islogin = None
    while True:
        num = ATM.choice()
        if num == "1":
            print("登陆")
            islogin = ATM.login()
        elif num == "2":
            print("开户")
            cardnum = ATM.openUser()
            if cardnum != None:
                print("恭喜你开户成功，您的卡号为%s,请牢记。。。"%cardnum)
        elif num == "3":
            print("查询")
            if islogin:
                ATM.search(islogin)
            else:
                print("请登录后查询。。。")
        elif num == "4":
            print("取款")

        elif num == "5":
            print("存款")

        elif num == "6":
            print("退出")
            break
        elif num == "9":
            print("转账")
            if islogin:
                ATM.transMoney(islogin)
            else:
                print("请登陆后转账。。。")
        else:
            print("选项有误，请重新选择。。。")




