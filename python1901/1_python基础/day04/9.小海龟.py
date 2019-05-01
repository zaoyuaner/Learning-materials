#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import turtle
#
# for x in range(4):
#     turtle.forward(200)
#     turtle.left(90)

turtle.pencolor("red")
turtle.begin_fill()
turtle.fillcolor("red")
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(100)
turtle.end_fill()

turtle.done()
# 五角星
