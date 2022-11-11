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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, xplayer, yplayer, photo):
        pygame.sprite.Sprite.__init__(self)
        angle = math.asin((xplayer - x) / (math.sqrt((xplayer - x) ** 2 + (y - yplayer) ** 2)))
        self.image = pygame.transform.rotate(photo, angle * 180 / math.pi)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.vy = 10 * math.cos(angle)
        self.vx = 10 * math.sin(angle)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):

        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > 800:
            self.kill()
