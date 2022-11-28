
import turtle
import math
t=turtle.Turtle()

#Takes three inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the outer square.
# HINT: Use the previous two functions.

def fractal(x, y, side):
    turtle.penup() #Lift up the pen not to draw anything
    turtle.setpos(x,y) #keep the pen pn the position from where you need to start drawing
    turtle.pendown() #give command to draw
    for i in range (4): # to repeat the following steps 4 times
        turtle.forward(side) #move the pointer to the length of side of square
        turtle.right(90) #turn 90 degree

    for i in range(4):
        turtle.penup() #Lift up the pen not to draw anything
    turtle.setx(x+side/2) #keep the pen pn the position from where you need to start drawing
    turtle.right(45)
    turtle.pendown() #give command to draw

    for i in range (4): # to repeat the following steps 4 times
        turtle.forward(math.sqrt(2*(math.pow(side/2,2))))# using pythagoras theorem 
        turtle.right(90)

fractal(-10,0,100)





turtle.done()