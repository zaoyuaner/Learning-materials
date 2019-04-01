# seek  移动文件指针
from io import SEEK_SET      # ( 打出SEEK_SET) 用灯泡出来的

with open("1.txt","r",encoding="utf-8") as fp:

	fp.seek(9,SEEK_SET)    # 第一个参数, 从文件开始处的偏移量(正数); 第二个参数whence是位置,表示文件开头,只能是0
	print(fp.read(3))
	print(fp.tell())           # 文件指针的位置( 整数)

