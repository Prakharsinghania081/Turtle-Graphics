import turtle
t = turtle.Turtle()
x = 100

for i in range(2):
    for j in range(5):
        t.fd(x)
        t.lt(72)
    t.rt(130)
    t.fd(14)
    t.lt(130)
    x += 20
#for j in range(5):
   # t.fd(x)
    #t.lt(72)
turtle.done()
