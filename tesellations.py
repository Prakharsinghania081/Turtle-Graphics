import turtle
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.left(120)
t2.left(240)
for i in (t, t1, t2):
    i.speed(0)

t1.fillcolor('blue')

def hex():
    for b in (t, t1, t2):
        for i in range(6):
             b.forward(100)
             b.right(60)


for i in range(3):
    t.left(120)
hex()
def rep():   
    for i in range(5):
        for a in (t, t1, t2):
            a.forward(100)
            a.right(60)
            for i in range(6):
                a.forward(100)
                a.left(60)
rep()

def rep2():
    for a in (t, t1, t2):
        for i in range(3):
            a.left(120)
            a.forward(100)
            a.right(60)
            rep()

    a.right(120)
    a.forward(100)
    a.right(60)
    rep()
rep2()