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
	vertices = []

	angle = 360.0/sides # play around with this
	for i in range(sides):
		vertices.append(  t.pos()  )
		t.forward(size)
		t.right(angle)
	# loop ends

	return vertices

def drawEpicycloid(T, multiplier):

	numVertices = 200 # number of vertices or sides
	sideSize    = 16
	v = drawPolygon(T, numVertices, sideSize)

	#==========================

	used = [False]*numVertices

	#do this for all values of current from 1 to 199
	for current in range(1, 200):
		T.penup()
		T.setposition( v[current] )
		T.pendown()

		while used[current] == False:

			used[current] = True # marking this place as used

			nextVertex = (current * multiplier) % numVertices

			# draws a line from current position to v[nextVertex]
			T.setposition( v[nextVertex] )

			current = nextVertex

#==================================================

def main():
	# this code gets executed
	T = turtle.Turtle()

	#==============================================
	# settings
	turtle.tracer(0,0) # turn off animation
	T.hideturtle()
	T.pensize(2)
	turtle.bgcolor("black")

	#==============================================

	T.penup()
	T.setposition(-100, 500)
	T.pendown()
	T.pencolor("red")
	drawEpicycloid(T, 41)

	T.penup()
	T.setposition(100, 500)
	T.pendown()
	T.pencolor("blue")
	drawEpicycloid(T, 99)

	#==============================================
	turtle.update()

	# end of main

main()
