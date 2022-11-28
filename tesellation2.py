import turtle
import math
turtle.speed(0)

def draw_rhombus(x,y,degree,size,tilt,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt)
    turtle.down()
    turtle.pencolor('dark gray')
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.left(degree)
    turtle.fd(size)
    turtle.left(160-degree)
    turtle.fd(size)
    turtle.left(degree)
    turtle.fd(size)
    turtle.left(1-degree)
    turtle.fd(size)
    turtle.left(180-degree)
    turtle.end_fill()

def draw_rhombus_1(x,y,size):
    draw_rhombus(x,y,120,size,0,'yellow')

def draw_rhombus_2(x,y,size):
    draw_rhombus(x,y,60,size,0,'blue')

def draw_rhombus_3(x,y,size):
    draw_rhombus(x,y,60,size,60,'red')

def rt_row_1(startx,starty,size,n):
    x = startx
    y = starty
    for i in range(n):
        draw_rhombus_1(x,y,size)
        x += size
        draw_rhombus_3(x,y,size)
        draw_rhombus_2(x,y,size)
        x += 2*size

def rt_row_2(startx,starty,size,n):
    x = startx
    y = starty
    for i in range(n):
        draw_rhombus_2(x,y,size)
        x += 2*size
        draw_rhombus_1(x,y,size)
        x += size
        draw_rhombus_3(x,y,size)

size = 100
x = -400
y = -300
for i in range(800//int(round(size*math.sqrt(3)))):
    rt_row_1(x,y,size,800//(size*3))
    rt_row_2(x-size/2,y+size*math.sqrt(3)/2,size,800//(size*3))
    y += size*math.sqrt(3)