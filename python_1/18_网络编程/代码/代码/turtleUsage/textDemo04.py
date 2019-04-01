#绘制五角星
import turtle,time

turtle.pensize(10)
turtle.color("yellow")
turtle.fillcolor("red")
turtle.speed(1)

#开始填充
turtle.begin_fill()

for i in range(5):
    #向前移动
    turtle.forward(200)
    #按照顺时针移动,参数表示移动的角度,left表示逆时针
    turtle.right(144)
    #turtle.left(100)

#结束填充
turtle.end_fill()

time.sleep(2)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("purple")
turtle.write("OVER",font=("宋体",50,"italic"))


turtle.done()
