import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(3)

polygon_angle = 3
figure_length = 50
x = 0
y = 0

for n in range(10):
    for angle in range(polygon_angle):
        t.forward(figure_length)
        t.right(360 / polygon_angle)
    t.penup()
    x -= 2
    y += 10
    t.goto(x, y)
    t.pendown()

    polygon_angle += 1
    figure_length += 5
