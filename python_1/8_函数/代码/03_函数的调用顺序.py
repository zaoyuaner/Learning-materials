
# 栈结构,羽毛球筒,先进后出,后进先出!
def test1():
	print("aaa")
	test2()
	print("over")

def test2():
	print("bbbb")
	test3()
	test4()

def test3():
	print("ccccc")

def test4():
	print("dddd")

test1()    # "aaa"--> (test2-->"bbbb"-->"ccccc"-->"dddd")-->"over"

# 如果子函数中出现死循环,父循环会卡住,后面代码无法执行!
