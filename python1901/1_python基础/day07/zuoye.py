
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.需求：对注册函数，进行数据过滤处理
要求写一个装饰器：用户名长度6~8，由字母数字下划线组成，
密码6位，由0~9数字组成，
若不满足条件打印用户名或者密码不合法
'''
# def outer(func):
#     def inner(user,password):
#         if user.isalpha() and int(user).isdigital() and "_"in user and len(user) >= 6 and len(user) <= 8:
#             if len(password)==6 and password.isdigital():
#                 return func(user, password)
#             else:
#                 print("密码非法")
#                 return None
#         else:
#             print("用户名非法")
#             return None
#     return inner
# @outer
# def func(user,password):
#     print("您的用户名为%s，密码为%s，请牢记密码；"%(user,password))
#
# func("hdqhdh",876798)


'''
2.写一个ATM管理系统：
功能：登陆，开户，查询，存款，取款，退出等

1.首先进入欢迎页面：
**********************
*                    *
*  welcome to bank   *
*                    *
**********************
2.让用户选择要操作：
**********************
*  1.登陆   2.开户    *
*  3.查询   4.取款    *
*  5.存款   6.退出    *
**********************
3.在执行登陆需要输入卡号并且输入密码，当卡号与密码一致的时候
进入系统。

4.当用户名不存在的时候，需要先开户的时候，
输入1.身份证号码 2.用户名  3.电话号码  4.预存款  5.密码  6.重复确认密码
开户成功之后，返回一个卡号，随机的，并且不重复的【6位0~9组成】

5.查询的时候要求先登陆【登陆的时候要保存卡号】
'''
import random
def weclome():
    print('''
    **********************
    *                    *
    *  welcome to bank   *
    *                    *
    **********************
    ''')
def choice():
    print('''
    **********************
    *  1.登陆   2.开户    *
    *  3.查询   4.取款    *
    *  5.存款   6.退出    *
    *  7.转账   8.改密    *
    *  9.锁卡   10.解锁   *
    **********************
    ''')
    num = input("请选择要操作的功能：")
    return num
def getcardnum():
    cardnum = ""
    for i in range(6):
        cardnum += str(random.randrange(10))
    return cardnum
def login(userdict):
    cardnum = input("请输入卡号")
    user = userdict.get(cardnum)
    if user == None:
        print("用户名不存在，请查证后登陆")
        return
    else:
        password = input("请输入您的密码：")
        if password == user.get("password"):
            print("登陆成功")
            return cardnum
        else:
            print("密码错误！！！")
            return
def kaihu():
    idcard = input("请输入身份证号码")
    name = input("请输入用户名")
    phonenum = input("请输入电话号码")
    money = int(input("请输入预存款"))
    if money > 0:
        password = input("请输入密码")
        password2 = input("重复输入密码")
        if password ==password2:
            print("开户成功")
            cardnum = getcardnum()
            print("您的卡号为%s请牢记"%cardnum)
            return{"idcard":idcard,"name":name,"phonenum":phonenum,"money":money,"password":password,"cardnum":cardnum}
        else:
            print("两次密码不一致，开户失败！！！")
            return
    else:
        print("输入预存款不合法")
        return


def chaxun(userdict,cardnum):
    print("您当前的余额为%d"%userdict[cardnum]["money"])

def qukuan(userdict,cardnum):
    while True:
        money = userdict[cardnum]["money"]
        jin = int(input("请输入取款金额"))
        if jin<=money:
            print("您取出的金额为%d"%jin)
            money -= jin
            print("您当前的余额为%d"%money)
            break
        else:
            print("取款金额有误，请重新输入")
    return userdict[cardnum]["money"] == money

def cunkuan(userdict,cardnum):
        money = userdict[cardnum]["money"]
        cun = int(input("请输入存款金额"))
        money += cun
        print("您的余额为%d"%money)




weclome()
userdict = {}
islogin = None
while True:
    num = int(choice())
    if num == 1:
        print("登录")
        islogin = login(userdict)
    elif num == 2:
        print("开户")
        user = kaihu()
        if user != None:
            cardnum = user["cardnum"]
            userdict[cardnum] = user
    elif num ==3:
        if islogin:
            print("查询")
            chaxun(userdict,cardnum)
        else:
            print("未登录，请登录后查询")
    elif num == 4:
        if islogin:
            print("取款")
            qukuan(userdict,cardnum)
        else:
            print("未登录，请登录后取款")
    elif num == 5:
        if islogin:
            print("存款")
            cunkuan(userdict,cardnum)
        else:
            print("未登录，请登录后存款")
    elif num == 6:
        print("退出")
        break
    elif num == 7:
        print("转账")

    else:
        print("输入选项有误，请重新选择")
