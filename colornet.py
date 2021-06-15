import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(260):
    t.pencolor(colors[x%6])
    t.width(x/100+3)
    t.forward(x)
    t.left(59)