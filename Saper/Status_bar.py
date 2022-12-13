import pygame


class StatusBar(pygame.sprite.Sprite):
    def __init__(self, width, height, score, goal, time, font):
        """

        :param width: ширина
        :param height: высота
        :param score: количество флагов, которые поставил игрок
        :param goal: сколько бомб стоит на поле
        :param time: время с начала игры
        :param font: шрифт для вывода текста
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 49))
        self.image.fill((227, 227, 227))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, height)
        self.score = score
        self.start_time = time//1000  # Чтобы время обнулялось, когда игра начинается заново
        self.time = 0  # Время, которое нужно будет выводить
        self.font = font
        self.goal = goal

    def change(self, time, score):
        self.time = time//1000 - self.start_time
        self.score = score

    def update(self):
        timer_width = 64
        counter_height = 36
        counter_width = 42

        pygame.draw.rect(self.image, (0, 0, 0), (self.rect.width//2 - 32, 7, timer_width, counter_height))
        # Черные прямоугольники - поля для вывода информации
        pygame.draw.rect(self.image, (0, 0, 0), (12, 7, counter_width, counter_height))
        pygame.draw.rect(self.image, (0, 0, 0), (self.rect.width - 12 - 42, 7, counter_width, counter_height))

        self.image.blit(self.font.render('{}'.format(self.score), False, (255, 0, 0)), (12 + 2, 7 - 4))
        self.image.blit(self.font.render('{}'.format(self.goal - self.score), False, (255, 0, 0)),
                        (self.rect.width - 12 - 42 + 2, 7 - 4))  # Вывод информации
        self.image.blit(self.font.render('{}'.format(self.time), False, (255, 0, 0)),
                        (self.rect.width // 2 - 32 + 2, 7 - 4))


