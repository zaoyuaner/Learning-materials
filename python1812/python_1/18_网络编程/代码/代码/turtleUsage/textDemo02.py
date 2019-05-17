import  turtle



turtle.color("pink")   #画笔的颜色
turtle.pensize(10)  #画笔的宽度
turtle.speed(1)

"""#正方形
#从（0,0）位置开始绘制
turtle.goto(0,200)
turtle.goto(200,200)
turtle.goto(200,0)
turtle.goto(0,0)


#从任意点开始绘制
turtle.penup()
turtle.goto(100,100)
turtle.pendown()


turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)


#三角形
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

turtle.goto(100,0)
turtle.goto(-100,0)
turtle.goto(0,200)

#菱形
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

turtle.goto(100,0)
turtle.goto(0,-200)
turtle.goto(-100,0)
turtle.goto(0,200)

"""

#steps表示几边形，数值越大，则越接近于圆
turtle.circle(100,steps=100)


turtle.done()