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
        self.radius = random.randint(20, 40)  # радиус шара
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.set_alpha(255)  # делает поверхность прозрачной
        self.rect = self.image.get_rect()
        self.rect.x = 600  # координаты шара
        self.rect.y = random.randint(100, 500)
        self.color = (128, 0, 0)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)  # рисует шар с обводкой
        pygame.draw.circle(self.image, (0, 0, 0), (self.radius, self.radius), self.radius, 2)
        self.vy = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

    def update(self):
        self.rect.y += self.vy
        if self.rect.bottom > 500:
            self.vy *= -1
        if self.rect.top < 0:
            self.vy *= -1


