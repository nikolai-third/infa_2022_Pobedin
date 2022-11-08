import pygame
import math

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (105, 105, 105)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Gun(pygame.sprite.Sprite):
    def __init__(self, photo):
        pygame.sprite.Sprite.__init__(self)
        self.image_base = photo  # Изображение - 40 прозрачных пикселей, 40 черных пикселей в длину, 10 в высоту,
        # так как вращение происходит вокруг центра поверхности
        self.image = self.image_base  # Так как мы будем вращать изображение, то в image_base сохраним изначальную п-ть
        self.rect = self.image_base.get_rect()
        self.rect.x = -30
        self.rect.y = 400
        self.angle = 0

    def fire(self, t):
        """
        Выстрел
        :param t: - время зажатия мышки, если больше 2с, то все равно максимальная сила выстрела
        :return: кортеж (угол под которым видно курсор из пушки, корректное время)
        """
        if t > 2000:
            t = 2000
        data = (self.angle, t)
        return data

    def get_angle(self, xm, ym):
        """
        Вычисляет под каким углом видно курсор из пушки
        :param xm: коордианта х курсора
        :param ym: координата у курсора
        :return: None
        """
        x = xm - (self.rect.x + 30)
        y = -(ym - (self.rect.y + 10))
        if x == 0:
            x = 10**(-5)
        self.angle = math.atan(y / x)

    def update(self):
        """
        Поворачивает пушку каждый кадр, чтобы она смотрела на курсор, при этом центр поверхности остается на месте
        :return: None
        """
        new_image = pygame.transform.rotate(self.image_base, self.angle * 180 / math.pi)
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center
