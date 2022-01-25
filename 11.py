import turtle          #бабочка

t = turtle.Turtle()
t.shape('turtle')
t.left(90)

size_step = 50
for i in range(20):
    size_step = size_step + i * 3

    t.circle(size_step)
    t.right(180)
    t.circle(size_step)
    t.left(180)
