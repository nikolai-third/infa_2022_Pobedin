import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((900, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """рисует новый шарик"""
    global x, y, r
    x = randint(100, 900)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def strike(xm, ym):
    """Проверяет попал ли пользователь кликом по шару"""
    print(xm, ym)
    if ((x-xm)**2 + (y-ym)**2) <= r**2:
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if strike(event.pos[0], event.pos[1]):
                    print('BOOM')
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
