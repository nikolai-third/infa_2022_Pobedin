import pygame
from classes import Ball, strike
import os

os.chdir("/Users/nort/Desktop/infa_2022_Pobedin/lab8/catch_ball")

pygame.init()

FPS = 45
screen = pygame.display.set_mode((900, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = pygame.sprite.Group()
for i in range(10):
    b = Ball()
    balls.add(b)

points = 0

u = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                data = []
                for i in balls:
                    if strike(event.pos[0], event.pos[1], i.coordinate()):
                        i.kill()
                        points += 1
                        b = Ball()
                        balls.add(b)

    balls.update()
    pygame.display.update()
    screen.fill(BLACK)
    balls.draw(screen)
    pygame.display.flip()

print(points)
file = open('leaderboard2.txt', 'a')
file.write('{} \n'.format(points))
file.close()
pygame.quit()
