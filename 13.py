import turtle     #звезды

t = turtle.Pen()
t.shape('turtle')
t.left(35)
n = int(turtle.textinput(u'Введите кол во', 'Введите кол во'))


def den4ik(n):
    t.left(180 - (180 / n))
    t.forward(200)


x = 1
while x <= n:
    den4ik(n)
    x += 1
