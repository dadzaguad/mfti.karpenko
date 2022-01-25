from random import randint
from pygame.draw import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 900))

FPS = 0.5
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def click(event, x, y, r):
    print(x, y, r, event.pos)
    d2 = (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2
    if d2 < r ** 2:
        return 1
    else:
        return 0


score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

#balls = []
'''основной цикл игры'''
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                x = ball[0]
                y = ball[1]
                r = ball[2]
                score += click(event, x, y, r)
            print(score)

    balls = [[randint(100, 1100), randint(100, 900), randint(10, 100)] for i in range(0, 2)]
    for ball in balls:
        color = COLORS[randint(0, 5)]
        circle(screen, color, (ball[0], ball[1]), ball[2])

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()