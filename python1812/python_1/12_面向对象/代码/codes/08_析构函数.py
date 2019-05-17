# 析构函数__del__: 与构造函数相反,当对象被销毁(释放)时,自动调用
# 构造函数__init__: 当对象创建时,自动调用

import time
class Person():
	def __init__(self):
		print("构造函数被调用")
	def __del__(self):          # 一般用于关闭数据库连接,关闭文件
		print("析构函数被调用")

p = Person()        # 实例化Person时,调构造函数
					# 当模块运行完毕,p对象被释放,自动调用析构函数
# del p             # 对象被手动删除时,也会立刻调析构函数
time.sleep(3)

# 将对象的实例化,放在函数中,那么函数调用结束,对象也会被立刻销毁
def fn():
	p = Person()     # 实例化,生

fn()                 # 死