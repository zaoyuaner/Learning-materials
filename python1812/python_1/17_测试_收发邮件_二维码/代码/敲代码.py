# from PIL import ImageFont,ImageDraw,Image
# from random import randint
# def randColor():     # 随机颜色
# 	return randint(0,255),randint(0,255),randint(0,255)
#
# # 新建画布
# tmp = Image.new("RGB",(2000,1000),"black")
#
# # 创建画笔
# pen = ImageDraw.Draw(tmp)
#
# # # 画点
# # for i in range(2000):
# # 	x = randint(1,2000)
# # 	y = randint(1,1000)
# # 	pen.point((x,y),fill=randColor())
#
# # 画方形
# pen.rectangle([(500,250),(1500,750)],fill="black",outline="white",width=2)
# # 画线
# pen.line([(0,0),(2000,1000)],fill="white",width=5)
# pen.line([(0,1000),(2000,0)],fill="white",width=5)
#
# # 保存图片
# tmp.save("2.jpg")
# # with open("","r") as fp:
# # 	fp.read()


# coding=utf-8
import turtle   # 小海龟
import time

# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")

turtle.begin_fill()
for _ in range(100):
	turtle.forward(200)  # 调整前进长度
	turtle.left(144)      # 调整转弯幅度120度 三角形  90度正方形 144度五角星
	# turtle.right()
	turtle.end_fill()

turtle.mainloop()


