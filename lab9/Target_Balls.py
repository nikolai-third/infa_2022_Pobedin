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


class Target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = random.randint(20, 30)  # радиус шара
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.set_alpha(255)  # делает поверхность прозрачной
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 600)  # координаты шара
        self.rect.y = random.randint(100, 400)
        self.color = (128, 0, 0)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)  # рисует шар с обводкой
        pygame.draw.circle(self.image, (0, 0, 0), (self.radius, self.radius), self.radius, 2)
        self.vx = random.randint(-8, 8)
        if self.vx == 0:
            self.vx = random.choice([-1, 1])
        self.vy = random.randint(-8, 8)
        if self.vy == 0:
            self.vy = random.choice([-1, 1])

    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.bottom > 530:
            self.vy *= -1
        if self.rect.top < 0:
            self.vy *= -1
        if self.rect.right > 800:
            self.vx *= -1
        if self.rect.left < 0:
            self.vx *= -1
