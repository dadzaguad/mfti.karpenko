import turtle            # большк квадратов ver 1


def draw_square(tur, x, y, size):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    for n in range(4):
        tur.forward(size)
        tur.left(90)


t = turtle.Turtle()
t.speed(2)
t.shape('turtle')

size = 100
step = 20
start_x = -size // 2
start_y = -size // 2

for n in range(10):
    draw_square(t, start_x, start_y, size)
    size = size + step
    start_x = -size // 2
    start_y = -size // 2
