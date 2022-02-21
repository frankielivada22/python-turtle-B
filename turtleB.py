import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("red")

t = turtle.Turtle()
t.width(5)

t.pendown()

t.forward(17.5)
t.circle(17.5, 180)
t.forward(17.5)
t.right(180)
t.forward(17.5)
t.circle(17.5, 180)
t.forward(17.5)
t.left(90)
t.forward(70)

turtle.done()