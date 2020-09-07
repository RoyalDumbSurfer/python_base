# -*- coding: utf-8 -*-

import random

import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, color=color, radius=radius, width=2)


# for y in range(100, 500, 100):
#     for x in range(100, 1100, 100):

for _ in range(100):
    color = sd.random_color()
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point, step)

sd.pause()

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей!

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг!

# Нарисовать 10 пузырьков в ряд!

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами!
