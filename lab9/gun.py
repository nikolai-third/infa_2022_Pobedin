from Target import Target
from Balls import Ball
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
f2 = pygame.font.Font('sfns-display-thin.ttf', 24)
text = f1.render('{}'.format(points), True, (0, 0, 0))
win_text = f2.render('Вы уничтожили цель за {} выстрелов'.format(bullet), True, (0, 0, 0))
win_time = 0

im = pygame.image.load('pushka.png')
gun = Gun(im)
all_sprite.add(gun)
for i in range(2):
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
        if target_number == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_time = pygame.time.get_ticks()  # время, когда пользователь нажал ЛКМ
            elif event.type == pygame.MOUSEBUTTONUP:
                dt = pygame.time.get_ticks() - click_time  # время, которое пользователь держал ЛКМ зажатой
                data = gun.fire(dt)  # Данные выстрела, для генерирования нового шара
                bullet += 1
                b = Ball(data[0], 150 * data[1]/2000)  # Новый шар
                balls.add(b)
                all_sprite.add(b)
        position = pygame.mouse.get_pos()
        gun.get_angle(position[0], position[1])  # Вычисляет куда нужно направить пушку
    for i in targets:
        hits = pygame.sprite.spritecollide(i, balls, False, pygame.sprite.collide_circle)
        if hits and N == 0:  # Проверят попал ли хотя бы один шар по цели условие на N защищает от начислений нескольких
            # очков за одно попадание
            N = 1
            i.kill()
            target = Target()
            target_number -= 1
            points += 1
            text = f1.render('{}'.format(points), True, (0, 0, 0))
            win_text = f2.render('Вы уничтожили цель за {} выстрелов'.format(bullet), True, (0, 0, 0))
            win_time = pygame.time.get_ticks()
            break
    pygame.display.update()
    screen.fill((255, 255, 255))

    if win_time != 0 and target_number != 2:  # показывает надпись про количество выстрелов
        if pygame.time.get_ticks() - win_time < 2500:
            screen.blit(win_text, (200, 250))
        else:
            bullet = 0
            targets.add(target)
            all_sprite.add(target)
            target_number += 1
            N = 0
    screen.blit(text, (0, 0))

    all_sprite.update()
    all_sprite.draw(screen)
    pygame.display.flip()

pygame.quit()
