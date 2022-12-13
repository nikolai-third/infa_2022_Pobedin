import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, img1, img2):
        """

        :param w: ширина кнопки
        :param h: высота кнопки
        :param x: кооридината х
        :param y: координата у
        :param img1: неактивное изображение
        :param img2: активное изображение
        """

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
        """
        Функция проверяет навелся ли пользователь на кнопку, если да, то меняется изображение и возвращается 1, если
        нужно
        :param happen: 1 - означает, что произошло нажатие мыши и нужно проверить попал ли игрок по кнопке
        0 - означает, что на мышку никто не нажимал, надо просто узнать какое изображение (активное или неактивное)
        рисовать
        :return: 1 - игрок попал по кнопке
        """

        mouse = pygame.mouse.get_pos()
        if ((mouse[0] > self.rect.x) and (mouse[0] < self.rect.x + self.width)) and (
                (mouse[1] > self.rect.y) and (mouse[1] < self.rect.y + self.height)):
            if happen == 1:
                return 1

            elif happen == 0:
                self.image = self.img2

        else:
            self.image = self.img1
