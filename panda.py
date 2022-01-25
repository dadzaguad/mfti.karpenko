import pygame
from pygame.draw import *

pygame.init()

FPS = 60
screen = pygame.display.set_mode((750, 720))
rect(screen, (243, 178, 136), (0, 0, 1506, 1451))
#БаМбУк ежжи
polygon(screen, (43, 102, 60), [(333,427), (374,427), (374,563), (333,563)])
polygon(screen, (43, 102, 60), [(333,260), (374,260), (374,410), (333,410)])
polygon(screen, (43, 102, 60), [(353,150), (380,158), (353,245), (325,230)])
polygon(screen, (43, 102, 60), [(353,150), (380,158), (353,245), (325,230)])
pi = 3.14
arc(screen, (43, 102, 60), (400, 650, 140, 3), (pi, 2*pi, 1))
# 400 650 140 3
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()