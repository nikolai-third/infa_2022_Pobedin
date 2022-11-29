import pygame
import random


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, nb, active, imgsL1, kl1, bombs, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((49, 49))
        self.NB = nb
        self.act = active
        self.image = imgsL1[9]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.imgsL = imgsL1
        self.kl = kl1
        self.bombs = bombs
        self.size = size

    def chislo(self):
        if self.act == 0:
            if self.NB == 0:
                self.image = self.imgsL[0]
                self.act = 1
                th1 = touch([self.rect.x, self.rect.y], self.size)
                for i in th1:
                    if str(i) in self.kl:
                        self.kl[str(i)].chislo()
            elif self.NB > 0:
                self.image = self.imgsL[self.NB]
                self.act = 1
            elif self.NB == -1:
                for i in self.bombs:
                    self.kl[str(i)].BOOM()
                self.image = self.imgsL[13]
    # what happen after click

    def flag(self):
        if self.act == 0:
            self.image = self.imgsL[10]
            self.act = 2

        elif self.act == 2:
            self.image = self.imgsL[9]
            self.act = 0
    # def for make a flag

    def BOOM(self):
        if self.act == 2:
            self.image = self.imgsL[12]
        if self.act == 0:
            self.image = self.imgsL[11]
# def for detonate all bombs


class Menu(pygame.sprite.Sprite):
    def __init__(self, width, height, FPS1, field1, field2, field3, but1, imgsL1, imgsM1, XY1, all_sprites1, kl1,
                 bombs1, num1, options1, screen1, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 300))
        self.imgsL = imgsL1
        self.imgsM = imgsM1
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (width-300)//2
        self.rect.y = (height-300)//4
        self.clock = pygame.time.Clock()
        self.FPS = FPS1
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.but1 = but1
        self.XY = XY1
        self.all_sprites = all_sprites1
        self.kl = kl1
        self.bombs = bombs1
        self.num = num1
        self.options = options1
        self.screen = screen1
        self.size = 50

    def render(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            for eventMenu in pygame.event.get():
                if eventMenu.type == pygame.QUIT:
                    run = False
                if eventMenu.type == pygame.KEYUP:
                    if eventMenu.key == pygame.K_ESCAPE:
                        run = False
                if eventMenu.type == pygame.KEYDOWN:
                    if 48 <= eventMenu.key <= 57:
                        if self.field1.station == 1:
                            self.field1.texts('{}'.format(eventMenu.key-48))
                        elif self.field2.station == 1:
                            self.field2.texts('{}'.format(eventMenu.key - 48))
                        elif self.field3.station == 1:
                            self.field3.texts('{}'.format(eventMenu.key - 48))
                    if eventMenu.key == pygame.K_BACKSPACE:
                        self.field1.texts('-1')
                        self.field2.texts('-1')
                        self.field3.texts('-1')

                if eventMenu.type == pygame.MOUSEBUTTONDOWN:
                    if eventMenu.button == 1:
                        if self.but1.click(1) == 1:
                            if (int(self.field1.text) >= 6 and int(self.field2.text) >= 6 and self.field3.text != '' and
                                    int(self.field3.text) <= int(self.field2.text) * int(self.field1.text)):
                                restart(self.XY, self.all_sprites, self.kl, self.bombs, self.num,
                                        int(self.field1.text) * self.size + 1, int(self.field2.text) * self.size + 1,
                                        self.imgsL, int(self.field3.text), self.size)

                                self.rect.x = (int(self.field1.text) * self.size + 1 - 300)//2
                                self.rect.y = (int(self.field2.text) * self.size + 1 - 300)//4
                                self.field1.rect.x = self.rect.x + 31
                                self.field1.rect.y = self.rect.y + 90
                                self.field2.rect.x = self.field1.rect.x + 66 + 20
                                self.field2.rect.y = self.rect.y + 90
                                self.field3.rect.x = self.field2.rect.x + 66 + 20
                                self.field3.rect.y = self.rect.y + 90
                                self.but1.rect.x = self.rect.x + 50
                                self.but1.rect.y = self.rect.y + 220
                                run = False
                            else:
                                print('BAN')
                        self.field1.state()
                        self.field2.state()
                        self.field3.state()
            self.but1.click(0)
            self.options.draw(self.screen)
            pygame.display.flip()


class Button(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, img1, img2):
        pygame.sprite.Sprite.__init__(self)
        self.width = w
        self.height = h
        self.image = pygame.Surface((self.width, self.height))
        self.img1 = img1
        self.img2 = img2
        self.image = self.img1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self, happen):
        mouse = pygame.mouse.get_pos()
        if ((mouse[0] > self.rect.x) and (mouse[0] < self.rect.x + self.width)) and (
                (mouse[1] > self.rect.y) and (mouse[1] < self.rect.y + self.height)):
            if happen == 1:
                return 1
            elif happen == 0:
                self.image = self.img2

        else:
            self.image = self.img1


class TextField(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, img1, img2, f11):
        pygame.sprite.Sprite.__init__(self)
        self.width = w
        self.height = h
        self.image = pygame.Surface((self.width, self.height))
        self.img1 = img1
        self.img2 = img2
        self.image = img1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = ''
        self.f1 = f11
        self.station = 0

    def texts(self, txt):
        if self.station == 1:
            if txt == '-1':
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.text = self.text[:len(self.text) - 1]
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
            else:
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.text += txt
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))

    # def clear(self):
    #     self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
    #     self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
    #     self.text = ''

    def state(self):
        mouse = pygame.mouse.get_pos()
        if ((mouse[0] > self.rect.x) and (mouse[0] < self.rect.x + self.width)) and (
                (mouse[1] > self.rect.y) and (mouse[1] < self.rect.y + self.height)):
            self.image = self.img2
            self.station = 1
        else:
            self.image = self.img1
            self.station = 0


def touch(m, size1):
    th = [[m[0], m[1] - size1], [m[0] + size1, m[1] - size1], [m[0] + size1, m[1]], [m[0] + size1, m[1] + size1],
          [m[0], m[1] + size1], [m[0] - size1, m[1] + size1], [m[0] - size1, m[1]], [m[0] - size1, m[1] - size1]]
    return th
# def for counting the number of touches of bombs


def restart(XY1, all_sprites1, kl1, bombs1, num1, w, h, imgsL1, number1, size):
    pygame.display.set_mode((w, h))
    pygame.display.flip()
    bombs1.clear()
    XY1.clear()
    kl1.clear()
    all_sprites1.empty()
    num1.clear()
    for i in range(w // size):
        for j in range(h // size):
            XY1.append([i * size + 1, j * size + 1])

    for i in range(number1):
        m = random.choice(XY1)
        num1.append(m)
        XY1.remove(m)
    # create bomb's coordinates

    for i in range((w // size)):
        for j in range((h // size)):
            m = [i * size + 1, j * size + 1]
            if m in num1:
                square = (Square(i * size + 1, j * size + 1, -1, 0, imgsL1, kl1, bombs1, size))
                kl1[str(m)] = square
                bombs1[str(m)] = square
                all_sprites1.add(square)
            else:
                Th = touch(m, size)
                NB = 0
                for u in Th:
                    if u in num1:
                        NB += 1
                square = (Square(i * size + 1, j * size + 1, NB, 0, imgsL1, kl1, bombs1, size))
                kl1[str(m)] = square
                all_sprites1.add(square)