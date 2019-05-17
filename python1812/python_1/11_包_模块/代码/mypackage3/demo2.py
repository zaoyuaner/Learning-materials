print("****")

def show():          # 此时show()不能在其他模块使用
	print("666")
# 只允许本模块执行,当本模块被导入其他模块是,不会被执行
if __name__ == "__main__":
	print("hello,world")
	show()

