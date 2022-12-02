import pygame
import random
from Square import Square


class Menu(pygame.sprite.Sprite):
    def __init__(self, width, height, FPS1, field1, field2, field3, but1, imgsL1, XY1, all_sprites1, kl1,
                 bombs1, num1, options1, screen1, img, un_img):
        """
        :param width: ширина
        :param height: высота
        :param FPS1: кадры в секунду
        :param field1: текстовое поле 1
        :param field2: текстовое поле 2
        :param field3: текстовое поле 3
        :param but1: кнопка
        :param imgsL1: изображение клеток
        :param XY1: массив для координат клеток с цифрами
        :param all_sprites1: группы для всех спрайтов
        :param kl1: словарь для клеток с цифрами
        :param bombs1: слоаварь для клток с бомбами
        :param num1: массив для координат клеток с бомбами
        :param options1: группа спрайтов для меню
        :param screen1: экран
        :param img: изображение меню
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 300))
        self.imgsL = imgsL1
        self.un_images = un_img
        self.images = img
        self.image = self.images[0]
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

    def render(self, win_or_lose_marker):
        self.image = self.images[win_or_lose_marker]
        """
        win_or_lose_marker == 0 - нейтральный режим - первый спрайт в массиве
        win_or_lose_marker == 1 - режим победы - второй спрайт в массиве
        win_or_lose_marker == -1 -режим проигрыша - последний спрайт в массиве
        """
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
                    """
                    Если пользователь нажимает на цифры, то проверяется активно ли какое-нибудь текстовое поле, если да
                    то в него надо ввести набранную цифру, если пользователь нажал на backsapce, то нужно удалить одну
                    цифру
                    """
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
                        if self.but1.click(1) == 1:  # Если нажата кнопка, то игра перезапускается
                            if check(self.field1.text, self.field2.text, self.field3.text):
                                restart(self.XY, self.all_sprites, self.kl, self.bombs, self.num,
                                        int(self.field1.text) * self.size + 1, int(self.field2.text) * self.size + 1,
                                        self.imgsL, self.size)

                                self.rect.x = (int(self.field1.text) * self.size + 1 - 300)//2  # меню в центре окна
                                self.rect.y = (int(self.field2.text) * self.size + 1 - 300)//4
                                self.field1.rect.x = self.rect.x + 31  # Новые координаты для всех элементов меню
                                self.field1.rect.y = self.rect.y + 90
                                self.field2.rect.x = self.field1.rect.x + 66 + 20
                                self.field2.rect.y = self.rect.y + 90
                                self.field3.rect.x = self.field2.rect.x + 66 + 20
                                self.field3.rect.y = self.rect.y + 90
                                self.but1.rect.x = self.rect.x + 50
                                self.but1.rect.y = self.rect.y + 220
                                run = False  # Меню убирается
                            else:
                                self.image = self.un_images[win_or_lose_marker]  # Нужно заменить изображение на
                                # изображение с надписью

                        self.field1.state()
                        self.field2.state()
                        self.field3.state()

            self.but1.click(0)
            self.options.update()
            self.options.draw(self.screen)
            pygame.display.flip()


def check(field1_txt, field2_txt, field3_txt):
    """
    фунцкция проверяет можно ли по введенным пользователем значениям в текстовые поля созздать игровое поле
    :return:
    """
    equation = [field1_txt, field2_txt, field3_txt]
    if '' in equation or ' ' in equation or '  ' in equation:  # Если одно из полей пустое, то нельзя
        return False

    for i in range(3):
        equation[i] = int(equation[i])

    if equation[0] * equation[1] < equation[2]:  # Если бомб больше, чем клеток, то нельзя
        return False

    if equation[0] * equation[1] - equation[2] > 1500:  # Если бомб слишком мало, то нельзя
        return False

    if equation[0] < 6 or equation[1] < 6:  # Размер меню 6х6 клеток, так что меньше нельзя
        return False

    return True


def restart(XY1, all_sprites1, kl1, bombs1, num1, w, h, imgsL1, size):
    """
    Функция, которая перезапускает игру, когда игрок нажимает на кнопку. Создает поле нужного размера со всеми пустыми
    кнопками
    :param XY1: массив с координатами клеток с цифрами
    :param all_sprites1: группа спрайтов для всех спрайтов
    :param kl1: словарь с клетками
    :param bombs1: словарь с клетками с бомбами
    :param num1: массив с координатами клеток с бомбами
    :param w: ширина окна
    :param h: высота окна
    :param imgsL1: массив с изображениями
    :param size: размер меню
    :return:
    """
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
            m = [i * size + 1, j * size + 1]
            square = (Square(i * size + 1, j * size + 1, 0, 0, imgsL1, kl1, bombs1, size))
            kl1[str(m)] = square
            all_sprites1.add(square)


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
    # def for counting the number of touches of bombs


def first_click(x0, y0, XY1, all_sprites1, kl1, bombs1, num1, w, h, imgsL1, number1, size):
    """
    Функция вызывается после первого клика, генерирует поле, при этом первая клетка всегда должна быть пустой
    :param x0: х первого клика
    :param y0: у первого клика
    :param XY1: массив со всеми клетками с цифрами
    :param all_sprites1: группа спрайтов для всех клеток
    :param kl1: словарь со всеми клетками: ключ - координаты, значение - спрайт
    :param bombs1: словарь с бомбами
    :param num1: массив с координатами бомб
    :param w: ширина экрана
    :param h: высота экрана
    :param imgsL1: массив с изображениями
    :param number1: количество бомб, которые нужно создать
    :param size: размер клетки
    :return:
    """
    forbidden = []
    forbidden.append([x0, y0])  # чтобы первая была пустая бомб не должно быть в ней и вокруг неё

    for i in touch([x0, y0], size):
        forbidden.append(i)

    for i in range(number1):  # случайным образом расставляет бомбы, так чтобы в forbidden координатах их не было
        m = random.choice(XY1)
        while m in forbidden:
            m = random.choice(XY1)
        num1.append(m)
        XY1.remove(m)

    for i in range((w // size)):  # делает квадраты бомбами или клетками с цифрами
        for j in range((h // size)):
            m = [i * size + 1, j * size + 1]
            if m in num1:
                square = (Square(i * size + 1, j * size + 1, -1, 0, imgsL1, kl1, bombs1, size))
                kl1[str(m)] = square
                bombs1[str(m)] = square
                all_sprites1.add(square)
            else:
                Th = touch(m, size)
                NB = 0  # число, которое будет написано на клетке
                for u in Th:
                    if u in num1:
                        NB += 1
                square = (Square(i * size + 1, j * size + 1, NB, 0, imgsL1, kl1, bombs1, size))
                kl1[str(m)] = square
                all_sprites1.add(square)


