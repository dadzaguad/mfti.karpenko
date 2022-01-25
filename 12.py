import turtle       #спиралька

t = turtle.Pen()
t.shape('turtle')
t.speed(5)
t.left(90)
x = 1
while x <= 6:
    t.circle(-50, 180)
    t.circle(-20, 180)
    x += 1
