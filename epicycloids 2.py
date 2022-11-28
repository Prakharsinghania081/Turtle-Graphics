import turtle
t = turtle.Turtle()

def drawpolygon(t, sides, size):
	angle=360/sides
	vertices=[None]*sides
	for i in range(sides):
		vertices[i]=t.setpos
		t.forward(size)
		t.right(angle)

	return vertices

def main():
	T = turtle.Turtle()

	#==============================================
	T.pensize(5)
	T.pencolor("red")
	turtle.bgcolor("black")


	T.penup()
	T.setposition(-30,200)
	T.pendown()
	n=20

	v = drawpolygon(T, n, 100)

	start = 1
	mult = 2

	for i in range(1):
		T.penup()
		T.setposition( v[start] )
		T.pendown()

	for i in range (10):
		nextVertex = (start*mult)%n
		T.setposition([nextVertex])
		start = nextVertex

	turtle.update()


	

main()
