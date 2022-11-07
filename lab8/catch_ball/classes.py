import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = random.randint(30, 80)  # радиус шара
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))  # объект - поверхность - квадрат со стороной 2радиуса
        self.image.set_alpha(255)  # делает поверхность прозрачной
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 800)  # генерация координат шара
        self.rect.y = random.randrange(100, 400)
        pygame.draw.circle(self.image, (random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240)),
                           (self.radius, self.radius), self.radius)  # на поверхности генерируется круг случаного цвета
        self.speedy = random.randrange(-8, 8)  # генерируется случайная скорость
        self.speedx = random.randrange(-8, 8)

    def update(self):
        self.rect.x += self.speedx  # на каждом кадре координаты равны предыдущим + значение скорости
        self.rect.y += self.speedy

        if self.rect.top < 0:  # при столкновении шара со стенкой, то его скорость генерируется случайно
            self.speedx = random.randrange(-8, 8)
            self.speedy = random.randrange(0, 8)

        if self.rect.bottom > 500:
            self.speedx = random.randrange(-8, 8)
            self.speedy = random.randrange(-8, 0)

        if self.rect.right > 900:
            self.speedx = random.randrange(-8, 0)
            self.speedy = random.randrange(-8, 8)

        if self.rect.left < 0:
            self.speedx = random.randrange(0, 8)
            self.speedy = random.randrange(-8, 8)

    def coordinate(self):
        result = (self.rect.centerx, self.rect.centery, self.radius)
        return result


class Square(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.length = random.randint(15, 50)  # половина длины стороны квадрата
        self.image = pygame.Surface((2 * self.length, 2 * self.length))
        self.image.fill((random.randrange(0, 240), random.randrange(0, 240), random.randrange(0, 240)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 800)  # генерация координат квадрата
        self.rect.y = random.randrange(100, 400)
        self.speedy = random.randrange(-8, 8)  # генерируется случайная скорость
        self.speedx = random.randrange(-8, 8)

    def update(self):
        self.rect.x += self.speedx  # на каждом кадре координаты равны предыдущим + значение скорости
        self.rect.y += self.speedy

        if self.rect.top < 0:  # при столкновении шара со стенкой, то происходит упругое столкновение
            self.speedy = -self.speedy

        if self.rect.bottom > 500:
            self.speedy = -self.speedy

        if self.rect.right > 900:
            self.speedx = -self.speedx

        if self.rect.left < 0:
            self.speedx = -self.speedx

    def coordinate(self):
        result = (self.rect.centerx, self.rect.centery, self.length)
        return result


def strike(form, xm, ym, C):
    '''
    вызывается при нажатии левой кнопкой мыши
    проверяет попал ли пользователь по объекту
    :param form: b - шары, s - квадраты
    :param xm: координаты по x клика мыши
    :param ym: координаты по y клика мыши
    :param C: кортеж данных про объект по которому можно проверить попал ли пользователь по объекту
    :return: True если пользователь попал и False если не попал
    '''
    if form == 's':
        if abs((xm - C[0])) < C[2] and abs((ym - C[1])) < C[2]:
            return True
        else:
            return False
    if form == 'b':
        if (xm - C[0])**2 + (ym - C[1])**2 <= C[2]**2:
            return True
        else:
            return False