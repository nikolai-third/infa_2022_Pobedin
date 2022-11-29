import pygame


class TextField(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, img1, img2, f11, text):
        """

        :param w: ширина поля
        :param h: высота поля
        :param x: координата по х
        :param y: координата по у
        :param img1: изображние неактивного поля
        :param img2: изображение активного поля
        :param f11: шрифт для текста
        """
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
        self.text = text
        self.f1 = f11
        self.station = 0
        self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
        self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
        self.img2.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
        self.img1.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))

    def texts(self, txt):
        """
        Функция, которая пишет текст в поле или стирает его если, txt = '-1'
        Стираение - рисование на изображении такого же числа, но белого цвета, что для пользователя будет выглядеть,
        как будто текст стерли.
        :param txt: текст, который нужно написать или '-1', если нужно удалить символ
        :return:
        """
        if self.station == 1:
            if txt == '-1':
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.text = self.text[:len(self.text) - 1]
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
            elif len(self.text) <= 2:  # Чтобы в ячейку нельзя было написать больше 3 цифр
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
                self.text += txt
                self.img2.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
                self.img1.blit(self.f1.render('{}'.format(self.text), False, (0, 0, 0)), (5, 5))
            else:
                print('fads')

    # def clear(self):
    #     self.img2.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
    #     self.img1.blit(self.f1.render('{}'.format(self.text), False, (255, 255, 255)), (5, 5))
    #     self.text = ''

    def state(self):
        """
        функция делает поле активным или неактивным
        :return:
        """
        mouse = pygame.mouse.get_pos()
        if ((mouse[0] > self.rect.x) and (mouse[0] < self.rect.x + self.width)) and (
                (mouse[1] > self.rect.y) and (mouse[1] < self.rect.y + self.height)):
            self.image = self.img2
            self.station = 1
        else:
            self.image = self.img1
            self.station = 0
