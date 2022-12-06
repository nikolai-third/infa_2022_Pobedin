import pygame
import os
from Menu import Menu
from Menu import first_click
from Button import Button
from TextField import TextField
from Status_bar import StatusBar
from Start import StartText


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
              'TextFieldActive.png', 'TextField.png', 'TextFieldActive.png', 'win_menu.png', 'lose_menu.png',
              'un_menu.png', 'un_win_menu.png', 'un_lose_menu.png', 'start_text.png']

imgsL = []  # Массив для больших изображений клеток, бомб и флага
imgs_menu = []  # Массив для изображений меню, текстовых полей и кнопки

game_folder = os.path.dirname(os.path.abspath(__file__))
img_folder = os.path.join(game_folder, 'img')

start_button = Button(170, 20, 65, 540, pygame.image.load(os.path.join(img_folder, 'start_button1.png')),
                      pygame.image.load(os.path.join(img_folder, 'start_button2.png')))
st = StartText(pygame.image.load(os.path.join(img_folder, 'start_text.png')), screen, start_button)

st.render()

for i in range(len(names_squareL)):
    imgsL.append(pygame.image.load(os.path.join(img_folder, names_squareL[i])))

for i in range(len(names_menu)):
    imgs_menu.append(pygame.image.load(os.path.join(img_folder, names_menu[i])))

f1 = pygame.font.Font('/{}/ofont.ru_Times New Roman.ttf'.format(img_folder), 36)  # Шрифт для цифр в текстовых полях
f2 = pygame.font.Font('/{}/digitalicg.ttf'.format(img_folder), 35)  # Шрифт для статус бара

options = pygame.sprite.Group()  # Группа спрайтов, связанных с меню (настройками)

menu_width_height = 300
but1 = Button(200, 50, (WIDTH - menu_width_height) // 2 + 50, (HEIGHT - menu_width_height) // 4 + 220, imgs_menu[1],
              imgs_menu[2])
field1 = TextField(66, 50, (WIDTH - menu_width_height) // 2 + 31, (HEIGHT - menu_width_height)//4 + 90, imgs_menu[3],
                   imgs_menu[4], f1, '15')
field2 = TextField(66, 50, field1.rect.x + 66 + 20, (HEIGHT - menu_width_height) // 4 + 90, imgs_menu[5],
                   imgs_menu[6], f1, '15')
field3 = TextField(66, 50, field2.rect.x + 66 + 20, (HEIGHT-menu_width_height) // 4 + 90, imgs_menu[7], imgs_menu[8],
                   f1, '40')
menu = Menu(WIDTH, HEIGHT, FPS, field1, field2, field3, but1, imgsL, XY, all_sprites, kl, bombs, num, options,
            screen, [imgs_menu[0], imgs_menu[9], imgs_menu[10]], [imgs_menu[11], imgs_menu[12], imgs_menu[13]])
# Создание всех элементов меню, а потом самого меню вместе с ними

options.add(menu)
options.add(but1)
options.add(field1)
options.add(field2)
options.add(field3)

pygame.display.set_mode((300, 300))
menu.render(0)

status_bar = StatusBar(int(field1.text) * 50, int(field2.text) * 50, 0, int(field3.text), pygame.time.get_ticks(), f2)
all_sprites.add(status_bar)
kl['SB'] = status_bar

# star the game
size = menu.size
# Цикл игры
running = True
score = 0  # количество флагов установленных на бомбах
n_flags = 0  # количество флагов
lose_marker = 0
time = 0

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    size = menu.size
    n_bombs = int(field3.text)
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
                    first_click(xy[0], xy[1], XY, all_sprites, kl, bombs, num, W, H, imgsL, n_bombs, size)
                if str(xy) in kl:  # Чтобы не происходило ошибок, когда игрок нажимает на статус бар
                    if not(kl[str(xy)].chislo()):  # если попал по бомбе, то проиграл(
                        lose_marker = -1

            if event.button == 3:  # Правая кнопка мыши ставит флаг на клетку
                if str(xy) in kl:
                    m = kl[str(xy)].flag()
                    if m[0]:  # Считаем количество флагов и сколько из них попали на бомбы
                        score += m[1]
                    n_flags += m[1]

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                menu.render(0)

    # Обновление
    all_sprites.update()
    if not num:  # Массив с координатми бомб пустой - маркер того, что игра началась заново, значит надо обнулить счет
        n_flags = 0
        score = 0
    kl['SB'].change(time + pygame.time.get_ticks() - time, n_flags)  # обновление значение в статус баре

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    if score == n_bombs:  # Проверка не выиграл ли случайно игрок
        score = 0
        menu.render(1)

    if lose_marker == -1:  # Проверка не проиграли ли случайно игрок
        lose_marker = 0
        score = 0
        menu.render(-1)


pygame.quit()
