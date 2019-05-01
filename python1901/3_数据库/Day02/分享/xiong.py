import turtle


#米老鼠
screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(800, 600)

#创建画笔
pen = turtle.Turtle()
#设置画笔的形状
pen.shape("turtle")
#设置画笔的颜色
pen.pencolor("yellow")
#设置线宽
pen.pensize(3)
#设置一下填充颜色
pen.fillcolor("yellow")

#头部
pen.begin_fill()
pen.circle(100)
pen.end_fill()

#左耳
pen.penup()
pen.goto(-100, 140)
pen.pendown()
pen.circle(50, 360)

#右耳
pen.penup()
pen.goto(100, 140)
pen.pendown()
pen.circle(50, 360)

#左眼白
pen.pencolor("white")
pen.penup()
pen.goto(-50, 100)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(20, 360)
pen.end_fill()

#左眼黑
pen.pencolor("black")
pen.penup()
pen.goto(-40, 100)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(10, 360)
pen.end_fill()

#右眼白
pen.pencolor("white")
pen.penup()
pen.goto(50, 100)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(20, 360)
pen.end_fill()

#右眼黑
pen.pencolor("black")
pen.penup()
pen.goto(40, 100)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(10, 360)
pen.end_fill()

#鼻子
pen.pencolor("black")
pen.penup()
pen.goto(0, 60)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(10, 360)
pen.end_fill()


pen.hideturtle()
screen.exitonclick()