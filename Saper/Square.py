import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, nb, active, imgsL1, kl1, bombs, size):
        """

        :param x: координата х
        :param y: координата у
        :param nb: количество соприкасающихся с клеткой бомб (число, которое будет написано при открытии) -1, если это
        бомба
        :param active: 0 - закрытая клетка 1 - открытая клетка 2 - клетка с флангом
        :param imgsL1: массив изображений клеток
        :param kl1: клетки без бомб
        :param bombs: клетки с бомбами
        :param size: размер клетки
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((49, 49))
        self.NB = nb  # NB - NumBer
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
        """
        Функция вызывается, когда игрок кликнул на клетку левой кнопкой мыши, если она с бомбой, то вызывает детонацию
        всех остальных бомб, если клетка с числом, то проверяет все соприкосающиеся клетки на их пустоту,
        если какая-нибудь клетка пустая, то её тоже нужно открыть и так далее
        :return:
        """

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
                return False

        return True

    def flag(self):
        """
        меняет спрайт на спрайт с флагом если self.act == 0
        и убирает флаг, если self.act == 2
        :return:
        """

        answer = [False, 0]  # answer[0] = True, если флаг поставлен на бомбу
        if self.NB == -1:
            answer[0] = [True]

        else:
            answer[0] = [False]

        if self.act == 0:
            self.image = self.imgsL[10]
            self.act = 2
            answer[1] = 1

        elif self.act == 2:
            self.image = self.imgsL[9]
            self.act = 0
            answer[1] = -1
        return answer

    def BOOM(self):
        """
        Функция для детонации всех бомб при проигрыше
        :return:
        """

        if self.act == 2:
            self.image = self.imgsL[12]

        if self.act == 0:
            self.image = self.imgsL[11]


def touch(m, size1):
    """
        выдает координаты клеток, которые соприкасаются с данной
        :param m:
        :param size1:
        :return:
        """

    th = [[m[0], m[1] - size1], [m[0] + size1, m[1] - size1], [m[0] + size1, m[1]], [m[0] + size1, m[1] + size1],
          [m[0], m[1] + size1], [m[0] - size1, m[1] + size1], [m[0] - size1, m[1]], [m[0] - size1, m[1] - size1]]

    return th
