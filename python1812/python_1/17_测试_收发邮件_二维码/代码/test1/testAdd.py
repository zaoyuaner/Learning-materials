# 测试Add.py中的add函数

import unittest
from Add import add

class Test(unittest.TestCase):       # 测试类, 继承测试用例 TestCase
	def setUp(self):
		print("开始测试")

	def tearDown(self):
		print("测试结束")

	# 写自己的测试函数,函数名的规则: test_你的函数名
	def test_add(self):
		self.assertEqual(add(1,2),3,"加法错误")   # 断言.根据需求选择函数,此为等于. 3为预期值


if __name__ == "__main__":
	unittest.main()           # PASSED (successes=1)
