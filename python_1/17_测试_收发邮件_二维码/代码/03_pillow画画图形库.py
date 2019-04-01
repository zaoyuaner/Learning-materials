# pillow画画图形库

from PIL import Image,ImageDraw,ImageFont
from random import randint
from PIL.ImageQt import rgb
def randColor():     # 随机颜色
	return randint(0,255),randint(0,255),randint(0,255)
# 1.创建画布
# 第一个参数:颜色模式 RGB.RGBA
# 第二个参数size: 画布大小,是一个元组(宽,高)
# 第三个参数color: 三种表示方式"red". "#ff0000"(#rrggbb)". "(red,green,blue)"
im = Image.new("RGB",(1000,500),"black")

# 2.创建画笔
# 参数是画布
pen = ImageDraw.Draw(im)

# 3.画点
for i in range(1000):
	x = randint(1,999)
	y = randint(1,499)
	# 第一个参数是点的坐标, 第二个参数是点的颜色
	pen.point((x,y),fill=randColor())

# 4.画线
# 第一个参数是线的坐标([起点坐标,终点坐标])
# 第二个参数是线的颜色
# 第三个参数是线宽
pen.line([(0,0),(999,499)],fill="white",width=4)

# 5.画长方形
# 第一个参数是长方形坐标:[(左上角坐标),(右下角坐标)]
# outline 是边的颜色
pen.rectangle([(100,100),(300,300)],fill = "red",outline = "white", width = 3)

# 6.画字
# 第一个参数是字体文件名,字体要求后缀TTF
# size 字体大小
# 编译
myFont = ImageFont.truetype("MSYH.TTF",size=55,encoding="utf-8")

pen.text((300,100),"易志康",fill="white",font=myFont)

# 保存图片
im.save("1.png","png")