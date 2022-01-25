import turtle          #паук

t = turtle.Turtle()
t.speed(2)
t.shape('turtle')

size = 100
angle = 30

for n in range(12):
    t.forward(size)
    t.stamp()
    t.goto(0, 0)
    t.right(angle)
