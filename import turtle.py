import turtle

#==================================================
# Functions
#==================================================
# t     = turtle
# sides = number of sides in my polygon
# len   = length of each side
# vertices = [none for i in range(sides)]
def drawPolygon(t, sides, size):
	# we need to return a list of vertices
	vertices = [None]*sides # vertices = []

	angle = 360.0/sides # play around with this
	for i in range(sides):
		vertices[i] = t.pos() # vertices.append(  t.pos()  )
		t.forward(size)
		t.right(angle)
	# loop ends

	return vertices
	
#==================================================

def main():
	# this code gets executed
	T = turtle.Turtle()

	#==============================================
	# settings
	turtle.tracer(0,0) # turn off animation
	T.hideturtle()
	T.pensize(5)
	T.pencolor("red")
	turtle.bgcolor("black")

	T.penup()
	T.setposition(-50, 200)
	T.pendown()


	#==============================================
	# code!
	n = 200 # number of vertices or sides
	v = drawPolygon(T, n, 20) # 50-sided, with each side = 50 steps long

	used = [False]*n # just a table, saying that no vertex has been used yet

	# go through all the vertices (not starting from 0 - why??)
	for current in range(1, n):

		# start from this vertex, making sure not to leave a trailing line
		T.penup()
		T.setposition( v[current] )
		T.pendown()

		# bounce around the polygon, stopping only when you hit a used vertex
		while used[current] == False:
			used[current] = True # this vertex is now used
			nextVertex = (current * 30)%n # using a different multiplier will change the shape!
			T.setposition( v[nextVertex] )
			current = nextVertex

	#==============================================
	turtle.update()
	#turtle.bye() # use this instead of done to close automatically
	turtle.done()

	# end of main

main()