from Target_Balls import Target
from Target_square import Target2
from Bullets import Ball
from Tank import Gun
from bombs import Bomb
import pygame


FPS = 30

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()  # группа, чтобы сразу обновлять и рисовать все спрайты
balls = pygame.sprite.Group()  # группа, чтобы проверять попал ли какой-нибудь из шаров по цели
targets = pygame.sprite.Group()  # группа, чтобы проверять проверять каждую цель на столкновение
ufo = pygame.sprite.Group()  # группа для нло, чтобы они стреляли
bombs = pygame.sprite.Group()  # группа для выстрелов нло, чтобы они могли убить игрока


points = 0  # количество очков

f1 = pygame.font.Font('sfns-display-thin.ttf', 36)  # Шрифт для счета
f2 = pygame.font.Font('sfns-display-thin.ttf', 30)  # Шрифт для надпись про проигрыш
text = f1.render('{}'.format(points), True, (0, 0, 0))  # Текст для счета


im_bomb = pygame.image.load('bullet.png')  # Загрузка изображений для игры
im_target_s = pygame.image.load('NLO.png')
im_name = ['tank2.png', 'tank47.png', 'tank92.png', 'tank137.png', 'tank182.png']
im = []
for i in im_name:
    im.append(pygame.image.load(i))

gun = Gun(im)  # Создание спрайтов
all_sprite.add(gun)
for i in range(5):
    target = Target()
    targets.add(target)
    all_sprite.add(target)

for i in range(2):
    target2 = Target2(im_target_s)
    targets.add(target2)
    ufo.add(target2)
    all_sprite.add(target2)

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
            b = Ball(data[0], data[1]/2000, 's', data[2], data[3])  # Новый шар
            balls.add(b)
            all_sprite.add(b)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # На пробел другой тип выстрелов, так что его нужно регистрировать
                click_time = pygame.time.get_ticks()
            elif event.key == pygame.K_d:  # Если зажата d едет вправо
                gun.speed('right')
            elif event.key == pygame.K_a:  # Если зажата a едет влево
                gun.speed('left')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:  # Когда отжимается пробел, вылетает шар, как м ЛКМ, но большой шар
                dt = pygame.time.get_ticks() - click_time  # время, которое пользователь держал ЛКМ зажатой
                data = gun.fire(dt)  # Данные выстрела, для генерирования нового шара
                b = Ball(data[0], data[1] / 2000, 'b', data[2], data[3])  # Новый шар
                balls.add(b)
                all_sprite.add(b)
            elif event.key == pygame.K_d and gun.vx > 0:  # Когда отжимаются кнопки направлений танк останавливает
                gun.speed('stop')
            elif event.key == pygame.K_a and gun.vx < 0:
                gun.speed('stop')
        position = pygame.mouse.get_pos()  # координаты мыши
        gun.get_angle(position[0], position[1])  # Обновляет угол, в который вылетит снаряд

    for i in ufo:  # Когда нло в наивысшей точке (vy == 0), он выстреливает
        if i.vy == 0:
            bomb = Bomb(i.rect.midbottom[0], i.rect.midbottom[1], gun.rect.center[0], gun.rect.center[1], im_bomb)
            bombs.add(bomb)
            all_sprite.add(bomb)

    injury = pygame.sprite.spritecollide(gun, bombs, False, pygame.sprite.collide_mask)
    if injury:  # Проверяет столкнулся ли хотя бы один выстрел нло с танком, если да, то экран меняется на
        screen.fill((255, 255, 255))  # Белый с надписью про счет на 2.5 секунды
        screen.blit(f2.render('Вы проиграли((( Ваш счет: {}'.format(points), True, (200, 0, 0)), (200, 300))
        pygame.display.update()
        pygame.time.wait(2500)

        bombs.empty()  # Очищаем все группы, чтобы игра перезапустилась
        targets.empty()
        balls.empty()
        ufo.empty()
        all_sprite.empty()

        all_sprite.add(gun)  # Создаем заново цели
        for i in range(5):
            target = Target()
            targets.add(target)
            all_sprite.add(target)

        for i in range(2):
            target2 = Target2(im_target_s)
            targets.add(target2)
            ufo.add(target2)
            all_sprite.add(target2)

        points = 0
        text = f1.render('{}'.format(points), True, (0, 0, 0))
        bombs.empty()
        injury = False

    for i in targets:  # Проверяем попал ли хотя бы один патрон в любую цель
        hits = pygame.sprite.spritecollide(i, balls, False)
        if hits:  # Проверям класс уничтоженной цели и создаем новый экземпляр этого класса
            if isinstance(i, Target2):
                target = Target2(im_target_s)
                ufo.add(target)
            else:
                target = Target()
            i.kill()
            points += 1
            text = f1.render('{}'.format(points), True, (0, 0, 0))
            targets.add(target)
            all_sprite.add(target)
            break

    pygame.display.update()  # Обновление и отрисовка всех спрайтов, обновление дисплея и текста
    screen.fill((255, 255, 255))

    screen.blit(text, (0, 0))

    all_sprite.update()
    all_sprite.draw(screen)
    pygame.display.flip()

pygame.quit()
