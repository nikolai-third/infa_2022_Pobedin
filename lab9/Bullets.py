import pygame
import random
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


class Ball(pygame.sprite.Sprite):
    def __init__(self, alpha=(math.pi/3), time=0, size='s',  x=10, y=400, ):
        """

        :param alpha: углол под которым должен вылетать мяч
        :param time: время зажать кноки, влияющее на модуль скорости
        :param size: размер шара, s - маленький и быстрый, b - большой и медленный
        :param x: кооридината по х, где должен появится мяч
        :param y: кооридината по у, где должен появится мяч
        """
        pygame.sprite.Sprite.__init__(self)
        if size == 's':
            self.radius = 10  # радиус шара
            self.color = YELLOW
            self.module = 150 * time

        elif size == 'b':
            self.radius = 15
            self.color = CYAN
            self.module = 70 * time
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.set_alpha(255)  # делает поверхность прозрачной
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # координаты шара
        self.rect.centery = y
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)  # круг с обводкой
        pygame.draw.circle(self.image, (0, 0, 0), (self.radius, self.radius), self.radius, 1)
        if alpha < 0:
            alpha += math.pi
        self.vx = int(self.module * math.cos(alpha))  # генерируется скорость
        self.vy = -int(self.module * math.sin(alpha))
        self.time = 0  # время, которое начнет отсчет, когда шар остановится
        self.kill_marker = 0  # 0 - шар двигается и его нельзя kill, 1 - шар стоит на месте, можно kill через 1.5с

    def update(self):
        """
        Обвновляет координаты шаров, учитывая, гравитацию, неупругие отскоки от стен, обеспечивает, чтобы шары
        не проваривались через стены и пол. Если шар лежит без движения 1.5 секунды, то его убираем
        :return:
        """
        self.rect.x += self.vx

        if not (self.rect.bottom == 580):
            self.vy += 2

        if (self.rect.bottom + self.vy) > 580:
            self.vy //= -2
            self.vx //= 1.7
        else:
            self.rect.y += self.vy

        if (self.rect.right + self.vx) > 800:
            self.rect.right = 800
        else:
            self.vx = -self.vx

        if (self.rect.left + self.vx) < 0:
            self.rect.left = 0
        else:
            self.vx = -self.vx

        if (self.rect.top + self.vy) < 0:
            self.vy //= -2
            self.vx //= 1.7
        else:
            self.rect.y += self.vy

        if (self.vy / 1.5) < 1.5 and (578 < self.rect.bottom < 580):
            self.vx = 0
            self.vy = 0
            self.rect.bottom = 580

        if self.vx == 0 and self.vy == 0 and self.kill_marker == 0:
            self.kill_marker = 1
            self.time = pygame.time.get_ticks()

        if (pygame.time.get_ticks() - self.time) > 1500 and self.kill_marker == 1:
            self.kill()
