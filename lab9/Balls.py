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
    def __init__(self, alpha=(math.pi/3), module=30):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 10  # радиус шара
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.set_alpha(255)  # делает поверхность прозрачной
        self.rect = self.image.get_rect()
        self.rect.x = 10  # координаты шара
        self.rect.y = 400
        self.color = random.choice(GAME_COLORS)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)  # круг с обводкой
        pygame.draw.circle(self.image, (0, 0, 0), (self.radius, self.radius), self.radius, 1)
        self.vx = int(module * math.cos(alpha))  # генерируется скорость
        self.vy = -int(module * math.sin(alpha))
        self.time = 0  # время, которое начнет отсчет, когда шар остановится
        self.kill_marker = 0  # 0 - шар двигается и его нельзя kill, 1 - шар стоит на месте, можно kill через 1.5с

    def update(self):
        """
        Обвновляет координаты шаров, учитывая, гравитацию, неупругие отскоки от стен, обеспечивает, чтобы шары
        не проваривались через стены и пол
        :return:
        """
        self.rect.x += self.vx

        if not (self.rect.bottom == 550):
            self.vy += 2

        if (self.rect.bottom + self.vy) > 550:
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

        if (self.vy / 1.5) < 1.5 and (548 < self.rect.bottom < 550):
            self.vx = 0
            self.vy = 0
            self.rect.bottom = 550

        if self.vx == 0 and self.vy == 0 and self.kill_marker == 0:
            self.kill_marker = 1
            self.time = pygame.time.get_ticks()

        if (pygame.time.get_ticks() - self.time) > 1500 and self.kill_marker == 1:
            self.kill()
