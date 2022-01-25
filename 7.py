import turtle        #круглая спираль

t = turtle.Turtle()
t.shape('turtle')

for i in range(100):
    t.forward(5+i)
    t.right(30)
