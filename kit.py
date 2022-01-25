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