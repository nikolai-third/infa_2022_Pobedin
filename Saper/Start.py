import pygame


class StartText(pygame.sprite.Sprite):
    def __init__(self, img, screen, button):
        """

        :param img: изображение стартового экрана
        :param screen: поверхность на которой нужно будет все это разместить
        :param button: кнопка, для закрывания стартового экрана
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 600))
        self.image = img
        self.rect = self.image.get_rect()
        self.screen = screen
        self.button = button
        self.group = pygame.sprite.Group()
        self.group.add(self)
        self.group.add(self.button)

    def render(self):
        pygame.display.set_mode((300, 600))
        FPS = 30
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button.click(1) == 1:  # Если нажата кнопка, то стартовый экран убирается
                            running = False

            self.button.click(0)  # Проверяем не навел ли игрок курсор на кнопку
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()
