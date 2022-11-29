import pygame
import os
from Menu import Menu
from Menu import first_click
from Button import Button
from TextField import TextField


FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x = 500
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
# variable of time

sizes = pygame.display.Info()
ScreenWidth = sizes.current_w
ScreenHeight = sizes.current_h
# screen size

WIDTH = 300
HEIGHT = 300
# window size

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сапер")
# create window


all_sprites = pygame.sprite.Group()


num = []  # Координаты верхних левых углов клеток с бомбами
XY = []  # Координты верхних левых углов клеток с цифрами
bombs = {}  # Словарь для взаимодейсвия с бомбами
kl = {}  # Словарь для взаимодействия с клетками

names_squareL = ['zeroL.png', 'oneL.png', 'twoL.png', 'threeL.png', 'fourL.png', 'fiveL.png', 'sixL.png', 'sevenL.png',
                 'eightL.png', 'closeL.png', 'flagL.png', 'bombL.png', 'detected_bombL.png', 'exploding_bombL.png']

names_menu = ['menu.png', 'button1.png', 'button2.png', 'TextField.png', 'TextFieldActive.png', 'TextField.png',
              'TextFieldActive.png', 'TextField.png', 'TextFieldActive.png']

imgsL = []  # Массив для больших изображений клеток, бомб и флага
imgs_menu = []  # Массив для изображений меню, текстовых полей и кнопки

game_folder = os.path.dirname(os.path.abspath(__file__))
img_folder = os.path.join(game_folder, 'img')
for i in range(len(names_squareL)):
    imgsL.append(pygame.image.load(os.path.join(img_folder, names_squareL[i])))

for i in range(len(names_menu)):
    imgs_menu.append(pygame.image.load(os.path.join(img_folder, names_menu[i])))

f1 = pygame.font.Font('/{}/ofont.ru_Times New Roman.ttf'.format(img_folder), 36)  # Шрифт для цифр

options = pygame.sprite.Group()  # Группа спрайтов, связанных с меню (настройками)

but1 = Button(200, 50, (WIDTH-300)//2 + 50, (HEIGHT-300)//4 + 220, imgs_menu[1], imgs_menu[2])
field1 = TextField(66, 50, (WIDTH-300)//2 + 31, (HEIGHT-300)//4 + 90, imgs_menu[3], imgs_menu[4], f1, '15')
field2 = TextField(66, 50, field1.rect.x + 66 + 20, (HEIGHT-300)//4 + 90, imgs_menu[5], imgs_menu[6], f1, '15')
field3 = TextField(66, 50, field2.rect.x + 66 + 20, (HEIGHT-300)//4 + 90, imgs_menu[7], imgs_menu[8], f1, '40')
menu = Menu(WIDTH, HEIGHT, FPS, field1, field2, field3, but1, imgsL, XY, all_sprites, kl, bombs, num, options,
            screen, imgs_menu[0])  # Создание всех элементов меню, а потом самого меню вместе с ними

options.add(menu)
options.add(but1)
options.add(field1)
options.add(field2)
options.add(field3)
menu.render()
# star the game
size = menu.size
# Цикл игры
running = True
score = 0

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    clock.tick(FPS)
    # Ввод процесса (события)
    size = menu.size
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            xy = list(event.pos)
            xy[0] = ((xy[0] - 1) // size) * size + 1
            xy[1] = ((xy[1] - 1) // size) * size + 1
            if event.button == 1:  # Левая кнопка мыши открывает клетку
                if not num:
                    W = int(field1.text) * size + 1
                    H = int(field2.text) * size + 1
                    first_click(xy[0], xy[1], XY, all_sprites, kl, bombs, num, W, H, imgsL, int(field3.text), size)
                kl[str(xy)].chislo()
            if event.button == 3:  # Правая кнопка мыши ставит флаг на клетку
                kl[str(xy)].flag()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                menu.render()
    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()
