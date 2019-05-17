#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import unittest
from day14.demo import sum1,jiecheng,Person

class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试。。。")

    def tearDown(self):
        print("测试结束自动调用")

    def test_sum1(self):
        self.assertEqual(sum1(1,2),3,"加法有误")

    def test_jiecheng(self):
        self.assertEqual(jiecheng(5),120,"阶乘有误")

    def test_init(self):
        per = Person("lili",19)
        self.assertEqual(per.age,19,"年龄有误")

    def test_getAge(self):
        per = Person("lili", 19)
        self.assertEqual(per.getAge(),19,"获取年龄有误")

if __name__ == "__main__":
    unittest.main()