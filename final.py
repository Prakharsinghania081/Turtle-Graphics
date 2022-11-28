import turtle
t=turtle.Turtle()



def drawSquare(x,y,side,k):
	turtle.penup()
	turtle.setpos(x,y)
	turtle.right(45)
	side_length=side
	for j in range(k):
		give_me_a_square(side_length)
		if(j<(k-1)):
			side_length = ((math.sqrt(2)*side_length))
			turtle.left(45)
			turtle.backward(side_length/2)


def give_me_a_square(side_length):
	for i in range(4):
		turtle.pendown()
		turtle.forward(side_length)
		turtle.right(90)
		turtle.penup()


drawSquare(-10,100,50,8)

turtle.done()

t.setpos(x + (side/2),y + (-(side/2))) #setting up the position of pen at the centre of fractal.(it comes through mdpoint formula of coordinatws)
    t.pendown() #Enable to draw
    for p in range(0,k): #since fibonacci numbers is exponentially increasing loops is the repetitions should be no of fractals*its ratio with startlength/2
        t.circle(((math.sqrt(2*(math.pow(length/2,2)))) + fibonacci(p)), 180) #starting with the smallest side of the fractal and increasing the radius with fibonacci numbers and 180 degree to have a tight bend.



