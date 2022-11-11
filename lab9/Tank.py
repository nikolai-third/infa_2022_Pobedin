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
    def __init__(self, photos):
        pygame.sprite.Sprite.__init__(self)
        self.photos = photos
        self.image = self.photos[0]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.bottom = 580
        self.vx = 0
        self.angle = 0
        self.marker = 0  # отвечает за то куда направлена башня, то есть откуда должен вылететь шар
        self.direction = 0  # чтобы двигалось, когда кнопка зажата
        self.mask = pygame.mask.from_surface(self.image)  # Маска для более корректных столкновений

    def fire(self, t):
        """
        Выстрел
        :param t: - время зажатия мышки, если больше 2с, то все равно максимальная сила выстрела
        :return: кортеж (Angle - угол, в который должен вылетать шар, t - время зажатия кнопки,
        x, y - координаты, где должен появится снаряд, чтобы это выглядело корректно)
        """
        if t > 2000:
            t = 2000
        if self.marker == 0:
            x = self.rect.midright[0]
            y = self.rect.midright[1]
        elif self.marker == 1:
            x = self.rect.topright[0]
            y = self.rect.topright[1]
        elif self.marker == 2:
            x = self.rect.midtop[0]
            y = self.rect.midtop[1]
        elif self.marker == 3:
            x = self.rect.topleft[0]
            y = self.rect.topleft[1]
        elif self.marker == 4:
            x = self.rect.midleft[0]
            y = self.rect.midleft[1]

        data = (self.angle, t, x, y)
        return data

    def get_angle(self, xm, ym):
        """
        Вычисляет под каким углом видно курсор из пушки
        :param xm: коордианта х курсора
        :param ym: координата у курсора
        :return: None
        """

        x = xm - self.rect.centerx
        y = -ym + self.rect.centery
        if x == 0:
            x = 10**(-5)
        self.angle = math.atan(y / x)

    def speed(self, direction):
        """
        Изменяет направление скорости, когда игрок нажимает или отжимает кнопки направления
        :param direction: направление скорости
        """
        if direction == 'right':
            self.vx = 7
        elif direction == 'left':
            self.vx = -7
        elif direction == 'stop':
            self.vx = 0

    def update(self):
        """
        Меняет спрайт танка на соотвествующий текущему углу на курсор, а также двигает танк
        :return: None
        """
        if 0 <= self.angle <= math.pi/5:
            self.image = self.photos[0]
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.rect.bottom = 580
            self.marker = 0
        elif math.pi/5 <= self.angle <= 2 * math.pi/5:
            self.image = self.photos[1]
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.rect.bottom = 580
            self.marker = 1
        elif 2 * math.pi/5 <= self.angle <= math.pi/2:
            self.image = self.photos[2]
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.rect.bottom = 580
            self.marker = 2
        elif -math.pi/2 <= self.angle <= -2 * math.pi/5:
            self.image = self.photos[2]
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.rect.bottom = 580
            self.marker = 2
        elif -2 * math.pi/5 <= self.angle <= -math.pi/5:
            self.image = self.photos[3]
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.rect.bottom = 580
            self.marker = 3
        elif -math.pi/5 <= self.angle <= 0:
            self.image = self.photos[4]
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.rect.bottom = 580
            self.marker = 4

        if (self.rect.left + self.vx) < 0:
            self.vx = 0
        if (self.rect.right + self.vx) > 800:
            self.vx = 0
        else:
            self.rect.x += self.vx