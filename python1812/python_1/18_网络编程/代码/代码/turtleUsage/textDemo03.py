#绘制奥运五环

import turtle

turtle.pensize(10)
turtle.speed(10)


l = ["red","yellow","black","blue","green"]

turtle.color(l[0])
turtle.circle(100)

turtle.penup()
turtle.goto(150,0)
turtle.pendown()
turtle.color(l[1])
turtle.circle(100)

turtle.penup()
turtle.goto(300,0)
turtle.pendown()
turtle.color(l[2])
turtle.circle(100)

#下面
turtle.penup()
turtle.goto(75,-130)
turtle.pendown()
turtle.color(l[3])
turtle.circle(100)


turtle.penup()
turtle.goto(225,-130)
turtle.pendown()
turtle.color(l[4])
turtle.circle(100)





turtle.done()
