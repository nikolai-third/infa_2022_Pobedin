import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = random.randint(30, 80)
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 800)
        self.rect.y = random.randrange(100, 400)
        pygame.draw.circle(self.image, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
                           (self.radius, self.radius), self.radius)
        self.speedy = random.randrange(-8, 8)
        self.speedx = random.randrange(-8, 8)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0:
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


def strike(xm, ym, C):
    if (xm - C[0])**2 + (ym - C[1])**2 <= C[2]**2:
        return True
    return False