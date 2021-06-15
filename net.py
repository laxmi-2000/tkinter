import turtle
loaswindow=turtle.Screen()
turtle.speed(2)

for i in range(50):
    turtle.circle(4*i)
    turtle.circle(-4*i)
    turtle.left(i)

turtle.exitonclick()