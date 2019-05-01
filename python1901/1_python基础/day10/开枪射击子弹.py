#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
需求：人开枪射击子弹
人：
特征：名字、枪
行为：开枪

枪：
特征：型号 弹夹
行为：射击

弹夹：
特征：子弹个数
行为：装弹  减弹
'''
class DanJia():
    def __init__(self,num=7):
        self.num = num

    def zhaungdan(self):
        self.num = 7

    def jiandan(self):
        if self.num>0:
            self.num -= 1
            print("biu！！！")
        else:
            print("没有子弹啦！！")

class Gun():
    def __init__(self,xinghao,danjia):
        self.xinghao = xinghao
        self.danjia = danjia

    def sheji(self):
        self.danjia.jiandan()

    # def shangtang(self):
    #     self.danjia.zhaungdan()

class Person():
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun

    def fire(self):
        self.gun.sheji()

    def fill(self):
        self.gun.danjia.zhaungdan()



if __name__ == "__main__":
    danjia = DanJia()
    gun = Gun("M416",danjia)
    per = Person("小明",gun)
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fill()
    per.fire()
    per.fire()
    per.fire()