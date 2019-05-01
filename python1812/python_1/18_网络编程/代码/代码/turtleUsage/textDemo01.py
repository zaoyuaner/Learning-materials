import  turtle

#设置屏幕大小
turtle.screensize(800,600,"pink")
#按照比例缩放画布的大小
turtle.setup(width=0.6,height=0.5)

#设置画笔的颜色
turtle.pencolor("red")
#设置画笔的粗细
turtle.pensize(10)

#向着箭头的方向前进100px
turtle.forward(100)
#设置
turtle.speed(0.1)
#前进到某个点
turtle.goto(-100,-200)

#画圆
turtle.circle(50)


#启动窗口【画布】
turtle.done()

