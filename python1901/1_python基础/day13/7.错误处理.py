#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
try:
    代码块#有可能发生错误的代码块
except 错误 as e：
    #记录错误
    logging.exception(e)
    错误处理
finally：
    无论是否发生错误，都会执行此处的代码

'''
import logging


g = (x for x in range(5))

while True:
    try:
        print(next(g))
    except StopIteration as e:
        print("执行完毕")
        break

def func():
    getRes()


def getRes():
    # try:
        f = None
        f = open("demo22.txt", "r")
        print("hello")
        f.read()
        f.close()
    # except FileNotFoundError as e:
    #     logging.exception(e)
    #     print("此文件不存在")
    #
    # finally:
    #     print("111")
    #     if f:
    #         f.close()


def main():
    func()



if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        logging.exception(e)

    print("hello")
