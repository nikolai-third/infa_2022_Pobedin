import pygame
from pygame.draw import *
# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

FPS = 30
clock = pygame.time.Clock()
# variable of time

# И создать окно:
screen = pygame.display.set_mode((500, 500))
screen.fill((217, 217, 217))
# здесь будут рисоваться фигуры
# смайлик
circle(screen, (255, 255, 84), (250, 250), 125)
circle(screen, (0, 0, 0), (250, 250), 125, 1)

# левый глаз
circle(screen, (255, 0, 0), (200, 220), 25)
circle(screen, (0, 0, 0), (200, 220), 25, 1)
circle(screen, (0, 0, 0), (200, 220), 10)

# правый глаз
circle(screen, (255, 0, 0), (300, 220), 15)
circle(screen, (0, 0, 0), (300, 220), 15, 1)
circle(screen, (0, 0, 0), (300, 220), 7)

# рот
polygon(screen, (0, 0, 0), [(200, 300), (200, 315), (300, 315), (300, 300), (200, 300)])

# левая и правая брови
polygon(screen, (0, 0, 0), [(236, 204), (231, 211), (150, 152), (155, 144), (236, 204)])
polygon(screen, (0, 0, 0), [(280, 212), (274, 205), (346, 143), (358, 153), (280, 212)])
# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
pygame.quit()