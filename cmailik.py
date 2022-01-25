import turtle

turtle.shape('turtle')
turtle.speed(5)

turtle.up()
turtle.goto(0, -100)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(100)
turtle.end_fill()

turtle.color("red")

turtle.up()
turtle.goto(-67, -40)
turtle.setheading(-60)
turtle.width(5)
turtle.down()
turtle.circle(80, 120)

turtle.color("black")

turtle.up()
turtle.goto(-0, -20)
turtle.setheading(-60)
turtle.width(5)
turtle.down()
turtle.left(150)
turtle.forward(30)


turtle.fillcolor("blue")
turtle.width(1)
for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

turtle.hideturtle()
turtle.done()
