import pytest
import turtle
import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.draw import *

# Тест 1: Проверка последовательности перемещений черепахи
def test_turtle_path():
    # Создаём нового черепаху
    t = turtle.Turtle()
    t.shape('turtle')
    # Начинаем с координаты (0,0)
    t.forward(50)     # (50, 0)
    t.left(90)
    t.forward(50)     # (50, 50)
    t.left(90)
    t.forward(50)     # (0, 50)
    t.right(90)
    t.forward(50)     # (0, 100)
    t.right(90)
    t.forward(50)     # (50, 100)
    pos = t.position()
    # Ожидаем конечную точку (50, 100)
    expected = (50.0, 100.0)
    assert abs(pos[0] - expected[0]) < 1e-5 and abs(pos[1] - expected[1]) < 1e-5
    turtle.bye()

# Тест 2: Вычисление выражения с использованием numpy
def test_numpy_calculation():
    x = np.array([1, 10, 1000])
    result = (np.log((1 / np.exp(np.sin(x) + 1)) / ((5 / 4) + 1 / x  15))) / np.log(1 + x  2)
    # Проверяем, что результат имеет нужную форму и все значения конечны
    assert result.shape == (3,)
    assert np.all(np.isfinite(result))

# Тест 3: Рисование квадрата с помощью turtle
def test_turtle_square():
    t = turtle.Turtle()
    t.shape('turtle')
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    pos = t.position()
    # После рисования квадрата черепаха должна вернуться к исходной точке (с точностью до погрешности)
    expected = (0.0, 0.0)
    assert abs(pos[0] - expected[0]) < 1e-5 and abs(pos[1] - expected[1]) < 1e-5
    turtle.bye()

# Тест 4: Проверка построения графика с matplotlib
def test_matplotlib_plot():
    fig, ax = plt.subplots()
    x = np.linspace(-20, 20, 100)
    y = x * x - x - 6
    ax.plot(x, y)
    ax.set_title('y(x) = x*x - x - 6')
    # Проверяем, что заголовок и данные линии соответствуют ожиданиям
    assert ax.get_title() == 'y(x) = x*x - x - 6'
    lines = ax.get_lines()
    assert len(lines) == 1
    np.testing.assert_allclose(lines[0].get_ydata()[0], (-20)*(-20) - (-20) - 6)
    np.testing.assert_allclose(lines[0].get_ydata()[-1], (20)*(20) - (20) - 6)
    plt.close(fig)

# Тест 5: Рисование вложенных квадратов (функция draw_square)
def test_draw_square_function():
    def draw_square(tur, x, y, size):
        tur.penup()
        tur.goto(x, y)
        tur.pendown()
        for n in range(4):
            tur.forward(size)
            tur.left(90)
    t = turtle.Turtle()
    t.speed(2)
    t.shape('turtle')
    size = 100
    step = 20
    start_x = -size // 2
    start_y = -size // 2
    for n in range(10):
        draw_square(t, start_x, start_y, size)
        size += step
        start_x = -size // 2
        start_y = -size // 2
    # Если функция завершилась без ошибок, тест считается успешным.
    turtle.bye()

# Тест 6: Рисование нескольких квадратов с изменяющимися размерами
def test_turtle_nested_squares():
    a = 10
    t = turtle.Turtle()
    t.shape('turtle')
    x = 1
    for j in range(a):
        t.pendown()
        for i in range(4):
            t.forward(x * 10)
            t.right(90)
        t.penup()
        t.left(90)
        t.forward(10)
        t.right(90)
        t.backward(10)
        x += 2
    turtle.bye()

# Тест 7: Рисование многоугольников с изменением параметров
def test_turtle_polygons():
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(3)
    polygon_angle = 3
    figure_length = 50
    x, y = 0, 0
    for n in range(10):
        for angle in range(polygon_angle):
            t.forward(figure_length)
            t.right(360 / polygon_angle)
        t.penup()
        x -= 2
        y += 10
        t.goto(x, y)
        t.pendown()
        polygon_angle += 1
        figure_length += 5
    turtle.bye()

# Тест 8: Рисование "злого смайлика" с использованием pygame
def test_angry_smile_pygame():
    pygame.init()
    FPS = 30
    screen = pygame.display.set_mode((500, 500))
    rect(screen, (217, 217, 217), (0, 0, 500, 500))
    def angrysmile():
        circle(screen, (255, 255, 0), (250, 250), 100)
        circle(screen, (0, 0, 0), (250, 250), 100, 1)
        circle(screen, (255, 0, 0), (200, 235), 25)
        circle(screen, (0, 0, 0), (200, 235), 25, 1)
        circle(screen, (0, 0, 0), (200, 235), 10)
        polygon(screen, (0, 0, 0), [(230, 230), (235, 223), (152, 180), (147, 187)])
        aalines(screen, (0, 0, 0), True, [(230, 230), (235, 223), (152, 180), (147, 187)], 1000)
        circle(screen, (255, 0, 0), (300, 235), 15)
        circle(screen, (0, 0, 0), (300, 235), 15, 1)
        circle(screen, (0, 0, 0), (300, 235), 8)
        polygon(screen, (0, 0, 0), [(280, 230), (275, 223), (347, 190), (350, 197)])
        aalines(screen, (0, 0, 0), True, [(280, 230), (275, 223), (347, 190), (350, 197)], 1000)
        polygon(screen, (0, 0, 0), [(200, 310), (200, 290), (300, 290), (300, 310)])
    angrysmile()
    pygame.display.update()
    # Кратковременная задержка для визуального эффекта (не блокирующая тест)
    pygame.time.delay(100)
    pygame.quit()

# Тест 9: Рисование смайлика с использованием turtle
def test_turtle_smiley():
    t = turtle.Turtle()
    t.speed(5)
    t.up()
    t.goto(0, -100)
    t.down()
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(100)
    t.end_fill()
    t.color("red")
    t.up()
    t.goto(-67, -40)
    t.setheading(-60)
    t.width(5)
    t.down()
    t.circle(80, 120)
    t.color("black")
    t.up()
    t.goto(0, -20)
    t.setheading(-60)
    t.width(5)
    t.down()
    t.left(150)
    t.forward(30)
    t.fillcolor("blue")
    t.width(1)
    for i in range(-35, 105, 70):
        t.up()
        t.goto(i, 35)
        t.setheading(0)
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    turtle.bye()

# Тест 10: Рисование сложной сцены с использованием pygame
def test_complex_scene_pygame():
    pygame.init()
    FPS = 30
    screen = pygame.display.set_mode((600, 800))
    # Задний фон
    rect(screen, (0, 255, 255), (0, 0, 600, 400))
    rect(screen, (0, 255, 0), (0, 400, 600, 400))
    # Солнце
    circle(screen, (255, 232, 36), (550, 70), 110)
    # Ствол дерева
    rect(screen, (255, 255, 255), (100, 400, 40, 200))
    # Крона
    ellipse(screen, (0, 102, 0), (30, 120, 200, 210))
    ellipse(screen, (0, 102, 0), (-20, 230, 300, 200))
    ellipse(screen, (0, 102, 0), (35, 370, 180, 140))
    # Яблоки
    ellipse(screen, (255, 204, 204), (140, 160, 50, 45))
    ellipse(screen, (255, 204, 204), (-20, 310, 50, 45))
    ellipse(screen, (255, 204, 204), (210, 310, 50, 45))
    ellipse(screen, (255, 204, 204), (150, 450, 45, 45))
    # Хвост
    for i in range(7):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (255, 238, 170), (220 - 10 * i, 590 + dy, 65, 30))
    for i in range(5):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (244, 215, 227), (220 - 5 * i, 620 + dy, 55, 25))
    for i in range(4):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (221, 175, 233), (220 - 5 * i, 610 + dy, 45, 22))
    for i in range(2):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (175, 233, 221), (180 - 5 * i, 670 + dy, 45, 22))
    # Тело и ноги
    ellipse(screen, (255, 255, 255), (260, 550, 230, 120))
    rect(screen, (255, 255, 255), (280, 615, 20, 120))
    rect(screen, (255, 255, 255), (325, 605, 23, 120))
    rect(screen, (255, 255, 255), (400, 615, 20, 120))
    rect(screen, (255, 255, 255), (450, 590, 17, 130))
    # Шея и рог
    polygon(screen, (255, 255, 255), [(351, 557), (461, 453), (480, 453), (480, 585)])
    polygon(screen, (255, 102, 255), [(480, 316), (450, 436), (472, 436)])
    # Голова и глаза
    ellipse(screen, (255, 255, 255), (440, 440, 90, 45))
    ellipse(screen, (255, 255, 255), (430, 430, 70, 50))
    ellipse(screen, (229, 128, 255), (465, 450, 20, 20))

ellipse(screen, (0, 0, 0), (475, 455, 10, 10))
    # Грива
    for i in range(8):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (255, 229, 204), (400 - 10 * i, 425 + dy, 60, 25))
    for i in range(5):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (233, 175, 175), (408 - 10 * i, 455 + dy, 40, 25))
    for i in range(2):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (229, 255, 128), (408 - 10 * i, 455 + dy, 40, 25))
    for i in range(3):
        dy = int(round(i  1.2)) * 10
        ellipse(screen, (229, 255, 128), (340 - 10 * i, 530 + dy, 50, 20))
    for i in range(3):
        dy = int(round(i ** 1.2)) * 10
        ellipse(screen, (175, 233, 221), (310 - 10 * i, 530 + dy, 50, 20))
    pygame.display.update()
    pygame.time.delay(100)
    pygame.quit()