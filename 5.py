import turtle        #больше квадратов ver 2

a = 10
turtle.shape('turtle')
x = 1
for j in range(a):
    turtle.pendown()
    for i in range(4):
        turtle.forward(x * 10)
        turtle.right(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.back(10)
    x += 2
