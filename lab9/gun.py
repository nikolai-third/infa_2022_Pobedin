from Target import Target
from Bullets import Ball
from Class_Gun import Gun
import pygame


FPS = 30

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()  # группа, чтобы сразу обновлять и рисовать все спрайты
balls = pygame.sprite.Group()  # группа, чтобы проверять попал ли какой-нибудь из шаров по цели
targets = pygame.sprite.Group()

points = 0
bullet = 0

f1 = pygame.font.Font('sfns-display-thin.ttf', 36)
f2 = pygame.font.Font('sfns-display-thin.ttf', 20)
text = f1.render('{}'.format(points), True, (0, 0, 0))
description = f2.render('Space - big slow bullet, LMB - small fact bullet', True, (0, 0, 0))

im_name = ['tank2.png', 'tank47.png', 'tank92.png', 'tank137.png', 'tank182.png']
im = []
for i in im_name:
    im.append(pygame.image.load(i))

print(im)
gun = Gun(im)
all_sprite.add(gun)
for i in range(5):
    target = Target()
    targets.add(target)
    all_sprite.add(target)
target_number = 2  # количество мишеней
N = 0  # количество попаданий
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_time = pygame.time.get_ticks()  # время, когда пользователь нажал ЛКМ
        elif event.type == pygame.MOUSEBUTTONUP:
            dt = pygame.time.get_ticks() - click_time  # время, которое пользователь держал ЛКМ зажатой
            data = gun.fire(dt)  # Данные выстрела, для генерирования нового шара
            bullet += 1
            b = Ball(data[0], data[1]/2000, 's', data[2], data[3])  # Новый шар
            balls.add(b)
            all_sprite.add(b)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                click_time = pygame.time.get_ticks()
            elif event.key == pygame.K_d:
                gun.speed('right')
            elif event.key == pygame.K_a:
                gun.speed('left')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                dt = pygame.time.get_ticks() - click_time  # время, которое пользователь держал ЛКМ зажатой
                data = gun.fire(dt)  # Данные выстрела, для генерирования нового шара
                bullet += 1
                b = Ball(data[0], data[1] / 2000, 'b', data[2], data[3])  # Новый шар
                balls.add(b)
                all_sprite.add(b)
            elif event.key == pygame.K_d and gun.direction == 1:
                gun.speed('stop')
            elif event.key == pygame.K_a and gun.direction == -1:
                gun.speed('stop')
        position = pygame.mouse.get_pos()
        gun.get_angle(position[0], position[1])  # Вычисляет куда нужно направить пушку

    for i in targets:
        hits = pygame.sprite.spritecollide(i, balls, False, pygame.sprite.collide_circle)
        if hits and N == 0:  # Проверят попал ли хотя бы один шар по цели условие на N защищает от начислений нескольких
            # очков за одно попадание
            N = 1
            i.kill()
            target = Target()
            points += 1
            text = f1.render('{}'.format(points), True, (0, 0, 0))
            bullet = 0
            targets.add(target)
            all_sprite.add(target)
            N = 0
            break
    pygame.display.update()
    screen.fill((255, 255, 255))

    screen.blit(text, (0, 0))
    screen.blit(description, (30, 10))

    all_sprite.update()
    all_sprite.draw(screen)
    pygame.display.flip()

pygame.quit()
