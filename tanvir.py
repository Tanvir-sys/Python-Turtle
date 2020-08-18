import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("white")
t.pencolor("green")
c=0
while True:
    for i in range(4):
        t.forward(80)
        t.right(90)

    t.right(5)
    c +=1
    if c>=360/5:
        break

t.hideturtle()     