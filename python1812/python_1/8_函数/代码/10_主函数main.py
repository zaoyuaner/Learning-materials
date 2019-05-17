# main 主函数
# C语言的主函数  程序运行的入口
# int main()
# {
#
#
# }

# python中 主函数是隐藏的,这整个py文件,就是主函数
if __name__ == "__main__":
	print("这是主函数")

def show():
	if __name__=="__main__":
		print("这是主函数")
	else:
		print("这不是主函数")

show()           # 这是主函数

