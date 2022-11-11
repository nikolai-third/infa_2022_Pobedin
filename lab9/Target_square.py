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


class Target2(pygame.sprite.Sprite):
    def __init__(self, photo):
        pygame.sprite.Sprite.__init__(self)
        self.image = photo
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 600)  # координаты шара
        self.rect.y = random.randint(100, 400)
        self.color = (255, 0, 0)
        self.vx = random.choice([-6, -5, -4, 4, 5, 6])
        self.vy = random.choice([-8, -7, -6, 6, 7, 8])
        self.ratio = 0

    def update(self):

        self.rect.x += self.vx
        self.vy += 1

        if (self.rect.bottom + 2 * self.vy) > 530:
            self.vy //= -1.07
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

        if (self.vy / 1.5) < 1.5 and (528 < self.rect.bottom < 530):
            self.vx = 0
            self.vy = 0
            self.rect.bottom = 580
