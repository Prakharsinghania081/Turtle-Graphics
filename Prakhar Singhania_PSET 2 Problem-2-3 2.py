#NAME- PRAKHAR SINGHANIA
#QUESTION NO. 2-3
#COLLABORATORS: PRABAL AGRAWAL


import turtle  
import math   

t = turtle.Turtle() 

#========================================== 
#==========================================  
#(a) completing the function drawSquare
# Takes three inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the square.

def drawSquare(x, y, side): #specifying thr inputs you require
    t.penup() #lifting the pen to avoid unwanted lines.
    t.setpos(x,y) #setting up the initial position of turtle at the x,y coordinate.
    t.pendown() #Commanding to start using pen and start drawing
    for i in range (4): # to repeat the following steps 4 times
        t.forward(side) #move the pointer to the length of side of square
        t.right(90) #turn 90 degree

#==========================================
#==========================================


# Takes three inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the square.

def drawTiltedSquare(x, y, side):
    t.penup() #lifting the pen to avoid unwanted lines.
    t.setpos(x,y) #setting up the initial position of turtle at the x,y coordinate.
    t.right(45) #tilting turtle 45 degrees.
    t.pendown() #Commanding to start using pen and start drawing
    for i in range (4): # to repeat the following steps 4 times
        t.forward(side) #move the pointer to the length of side of square
        t.right(90) #turn 90 degree
    

#==========================================
#==========================================
# Takes three inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the outer square.
# HINT: Use the previous two functions.



def squareInSquare(x, y, side):
    drawSquare(x, y, side) #calling out function from previous 
    drawTiltedSquare(x+side/2, y, math.sqrt(2*(math.pow(side/2,2)))) \
    #we take x+side/2 because we dont know origin so mid point is from the x coordinate we took
    #Pythagoras theorem to find the side of tilted square inside is the hypotenus of the right angled triangle
    # with sides being half the side of outer square.

#==========================================
#==========================================
# Takes four inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# startSide = length of the first square.
# k = number of times we want the fractal to repeat.
# HINT: Think Functions.


def fractal(x, y, startSide, k):
    t.penup() #Lift up the pen not to draw anything
    t.setpos(x,y) #keep the pen pn the position from where you need to start drawing
    t.pendown() #give command to draw
    
    
    for l in range(2*k): #2*k so that fractals are repeated twice and not just individual square
        for i in range (4): # to repeat the following steps 4 times
            t.pendown()
            t.forward(startSide) #move the pointer to the length of side of square
            t.right(90) #turn 90 degree and outer square is made
           
        t.penup() #Lift up the pen not to draw anything    
        t.forward(startSide/2) #keep the pen pn the position from where you need to start drawing
        t.right(45) #turn 45 and its loop will make inner square
        #after this step the above loop will repeat making a sqaure and so on....
            
        startSide=(math.sqrt(2*(math.pow(startSide/2,2))))#New side of square computes its value using pythpgras on basis of which side of the side of square just before that.  


#==========================================
#==========================================

#Takes four inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# startLength = length of the first move.
# k = number of moves.

def spiralOut(x, y, startlength, k):
    fractal(x, y, startlength*20, k)
    side=startlength*20
    t.setpos(x + (side/2),y + (-(side/2))) #setting up the position of pen at the centre of fractal.(yi side/2 because cursor moves down)
    t.pendown() #Enable to draw
    for p in range(0,startlength*20): #increase one till the max side of the outer square
        result=startlength+p #the result should be initalised to samllest length square
        if result <= ((startlength*22)/(math.sqrt(2))): #max diameter should not exceed the diagonal of the largest square
            t.circle((startlength)+p, 20) 
        else:
            break #the repetitions should be no of fractals*its ratio with startlength
    #the code is not for infinte whorls..it is for number of whorls corresponding to sides

#.......................................................................
#fibonacci spiral out of fractal

def fibonacci(n): #calclution of fibonacci numbers 
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


def spiralOutfibonacci(x, y, startlength, k):
    fractal(x, y, startlength*20, k) 
    side=startlength*20 #defining proportion of side of fractal with respect to startlength of spiral
    t.setpos(x + (side/2),y + (-(side/2))) #setting up the position of pen at the centre of fractal.(it comes through mdpoint formula of coordinatws)
    t.pendown() #Enable to draw
    for p in range(0,startlength*20): #repeating the following steps 20 times the startlength
        result=fibonacci(p) #assigning a variable to fibonaaci numbers
        if result < startlength*30: #marking the max radius of spiral as the length of outermost square(30 in place of 20 because series increases exponentially)
            t.circle((fibonacci(p)), 180) #increasing length of spiral by fibonacci numbers and defining extent as 180 degrees so that semi circles of increasing radii form the spiral
        else:
            break #if the length of spiral exceeds side of outermost square stop the loop


#THE FIBONACCI SPIRAL IS CALLED THE GOLDEN SPIRAL


#some random inuts to test the function
#to reset the turtle so that other codes can follow without overlapping.

drawSquare(-100,100,300)
t.reset()
drawTiltedSquare(-100,100,300)
t.reset()
squareInSquare(-100,100,300)
t.reset()
t.speed(0)
fractal(-100,100,300,5)
t.reset()
t.speed(0)
t.speed(0)
spiralOut(-49,70,15,10)
t.reset()
t.speed(0)
spiralOutfibonacci(-49,100,15,10)


#some random inuts to test the function
#to reset the turtle so that other codes can follow without overlapping.
#==========================================
turtle.done()


