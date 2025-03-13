import turtle
import matplotlib.pyplot as plt
#test1

turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

#test2

import numpy as np

x = np.array([1, 10, 1000])
print((np.log((1 / np.e ** (np.sin(x) + 1)) / ((5 / 4) + 1 / x ** 15))) / np.log(1 + x ** 2))


#test3

turtle.shape('turtle')
turtle.forward(120)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)

#test4

x = np.linspace(-20, 20, 100)
plt.title('y(x) = x*x - x - 6')
plt.plot(x, x * x - x - 6)
plt.show()

#test5

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


#test6

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


#test7

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

#test8

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))


rect(screen, (217, 217, 217), (0, 0, 500, 500))

def angrysmile():

    circle(screen, (255, 255, 0), (250, 250), 100)
    circle(screen, (0, 0, 0), (250, 250), 100, 1)


    circle(screen, (255, 0, 0), (200, 235), 25)
    circle(screen, (0, 0, 0), (200, 235), 25, 1)
    circle(screen, (0, 0, 0), (200, 235), 10)

    polygon(screen, (0, 0, 0), [(230, 230), (235, 223), (152, 180), (147, 187)])
    aalines(screen, (0, 0, 0), True, [(230, 230), (235, 223), (152, 180), (147, 187)], 1000)

    circle(screen, (255, 0, 0), (300, 235), 15)
    circle(screen, (0, 0, 0), (300, 235), 15, 1)
    circle(screen, (0, 0, 0), (300, 235), 8)

    polygon(screen, (0, 0, 0), [(280, 230), (275, 223), (347, 190), (350, 197)])
    aalines(screen, (0, 0, 0), True, [(280, 230), (275, 223), (347, 190), (350, 197)], 1000)


    polygon(screen, (0, 0, 0), [(200, 310), (200, 290), (300, 290), (300, 310)])


angrysmile()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

#test9

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


#test10

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

# задний фон
rect(screen, (0, 255, 255), (0, 0, 600, 400))
rect(screen, (0, 255, 0), (0, 400, 600, 400))
# sun
circle(screen, (255, 232, 36), (550, 70), 110)

# ствол дерева
rect(screen, (255, 255, 255), (100, 400, 40, 200))
# крона (3 элипса)
ellipse(screen, (0, 102, 0), (30, 120, 200, 210))
ellipse(screen, (0, 102, 0), (-20, 230, 300, 200))
ellipse(screen, (0, 102, 0), (35, 370, 180, 140))

# яблоки 1, 2, 3, 4
ellipse(screen, (255, 204, 204), (140, 160, 50, 45))
ellipse(screen, (255, 204, 204), (-20, 310, 50, 45))
ellipse(screen, (255, 204, 204), (210, 310, 50, 45))
ellipse(screen, (255, 204, 204), (150, 450, 45, 45))

# хвост
for i in range(7):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (255, 238, 170), (220 - 10 * i, 590 + dy, 65, 30))
for i in range(5):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (244, 215, 227), (220 - 5 * i, 620 + dy, 55, 25))
for i in range(4):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (221, 175, 233), (220 - 5 * i, 610 + dy, 45, 22))
for i in range(2):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (175, 233, 221), (180 - 5 * i, 670 + dy, 45, 22))

# тело
ellipse(screen, (255, 255, 255), (260, 550, 230, 120))
# нога 1
rect(screen, (255, 255, 255), (280, 615, 20, 120))
# нога 2
rect(screen, (255, 255, 255), (325, 605, 23, 120))
# нога 3
rect(screen, (255, 255, 255), (400, 615, 20, 120))
# нога 4
rect(screen, (255, 255, 255), (450, 590, 17, 130))

# шея
polygon(screen, (255, 255, 255), [(351, 557), (461, 453), (480, 453), (480, 585)])
# рог
polygon(screen, (255, 102, 255), [(480, 316), (450, 436), (472, 436)])
# голова
ellipse(screen, (255, 255, 255), (440, 440, 90, 45))
ellipse(screen, (255, 255, 255), (430, 430, 70, 50))
# глаза
ellipse(screen, (229, 128, 255), (465, 450, 20, 20))
ellipse(screen, (0, 0, 0), (475, 455, 10, 10))

# грива
for i in range(8):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (255, 229, 204), (400 - 10 * i, 425 + dy, 60, 25))
for i in range(5):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (233, 175, 175), (408 - 10 * i, 455 + dy, 40, 25))
for i in range(2):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (229, 255, 128), (408 - 10 * i, 455 + dy, 40, 25))
for i in range(3):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (229, 255, 128), (340 - 10 * i, 530 + dy, 50, 20))
for i in range(3):
    dy = int(round((i) ** 1.2)) * 10
    ellipse(screen, (175, 233, 221), (310 - 10 * i, 530 + dy, 50, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

