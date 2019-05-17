# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try.finally来实现：
try:
	fp = open('1.txt', 'r', encoding='utf-8')
	print(fp.readlines())
except Exception as a:
	print(a)
finally:
	fp.close()

# 可以简写为： 上下文管理
# with语句会自动调用close方法关闭文件
with open('1.txt', 'r', encoding='utf-8') as fp:
	print(fp.readline())
