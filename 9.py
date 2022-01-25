import turtle    #квадратная спираль

t = turtle.Turtle()
t.shape('turtle')

for i in range(40):
    t.forward(i * 10)
    t.right(90)
