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
    

drawSquare(-100,100,300) #some random inputs to test the function
t.reset() # #to reset the turtle so that other codes can follow without overlapping.
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
    

drawTiltedSquare(-100,100,300) #some random inputs to test the function

t.reset() #to reset the turtle so that other codes can follow without overlapping.
#==========================================
#==========================================
# Takes three inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the outer square.
# HINT: Use the previous two functions.



def squareInSquare(x, y, side):
    t.penup() #Lift up the pen to stop drawing and avoid unwanted lines.
    t.setpos(x,y) #setting up the initial position of turtle at the x,y coordinate.
    t.pendown() #Commanding to start using pen and start drawing
    for i in range (4): # to repeat the following steps 4 times
        t.forward(side) #move turtle forawrd by the length of side of square as in input 
        t.right(90) #turn 90 degree

    
    t.penup() #Lift up the pen to stop drawing and avoid unwanted lines.
    t.forward(side/2) #positioning the pen in middle of the side. 
    t.right(45) #turn 45 degree to tilt the pen
    t.pendown() #give command to draw

    for i in range (4): # to repeat the following steps 4 times
        t.forward(math.sqrt(2*(math.pow(side/2,2))))#Pythagoras theorem to find the side of tilted square inside is the hypotenus of the right angled triangle with sides being half the side of outer square.
        t.right(90)

squareInSquare(-100,100,300) #some random inputs to test the function
t.reset() #to reset the turtle so that other codes can follow without overlapping.
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
    
    
    for l in range(2*k): 
        for i in range (4): # to repeat the following steps 4 times
            t.pendown()
            t.forward(startSide) #move the pointer to the length of side of square
            t.right(90) #turn 90 degree and outer square is made
            
        t.penup() #Lift up the pen not to draw anything    
        t.forward(startSide/2) #keep the pen pn the position from where you need to start drawing
        t.right(45) #turn 45 and its loop will make inner square
        #after this step the above loop will repeat making a sqaure and so on....
            
        startSide=(math.sqrt(2*(math.pow(startSide/2,2))))#New side of square computes its value using pythpgras on basis of which side of the side of square just before that.  

    


fractal(-100,100,300,2) #some random inputs to test the function
t.reset() #to reset the turtle so that other codes can follow without overlapping.

#==========================================
#==========================================
# Takes four inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# startLength = length of the first move.
# k = number of moves.
#Takes four inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# startLength = length of the first move.
# k = number of moves.

t.speed(0)

def spiralOut(x, y, startlength, k):
    fractal(x, y, startlength*20, k)
    
    t.setpos(x + ((startlength*20)/2),y + (-(startlength*20))) #setting up the position of pen at the centre of fractal.(it comes through mdpoint formula of coordinatws)
    t.pendown() #Enable to draw
    for p in range(0,k*20): #the repetitions should be no of fractals*its ratio with startlength
        t.circle((math.sqrt(2*(math.pow((startlength)/2,2))))+p, 20) #starting with the smallest side of the fractal and increasing the whorls with p increasing radius each time and making a spiral with 20 degrees being the extent.

spiralOut(-49,70,15,8) #some random inputs to test the function
t.reset() #to reset the turtle so that other codes can follow without overlapping.



#.......................................................................
#fibonacci
t.speed(0)

def fibonacci(n): #calclution of fibonacci numbers 
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


def spiralOutfibonacci(x, y, startlength, k):
    t.penup() #Lift up the pen to stop drawing and avoid unwanted lines.
    side = startlength*20 #defining proportion of side of fractal with respect to startlength of spiral
    t.setpos(x,y)  #set the position of pen at x,y coordinate
    length = side
    for l in range(2*k):  
        for i in range(4):   #repeat it four times as it requires 4 sides
          t.pendown() # command to start drawing
          t.forward(length) #forward with lenght, which is the side. Its value is defined below
          t.right(90)    #turn 90 degrees right
          t.penup()

        t.forward(length/2)  # to reach mid point of outer square.
        t.right(45)  #tilt the pen 45 degree to start a tilted square
        length = (math.sqrt(2*(math.pow(length/2,2)))) #using pythagoras theorem. The side of inner square is the hypotenus of the right angled triangle with sides being half the side of outer square.
        #the above loop will repeat to make a fractal
    
    t.setpos(x + (side/2),y + (-(side/2))) #setting up the position of pen at the centre of fractal.(it comes through mdpoint formula of coordinatws)
    t.pendown() #Enable to draw
    for p in range(0,k*5):
        t.circle(((math.sqrt(2*(math.pow(length/2,2)))) + fibonacci(p)), 180) #starting with the smallest side of the fractal and increasing the radius with fibonacci numbers and 180 degree to have a tight bend.



#THE FIBONACCI SPIRAL IS CALLED THE GOLDEN SPIRAL


spiralOutfibonacci(-49,70,15,4)

#==========================================
turtle.done()

