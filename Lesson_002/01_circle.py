#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
from pprint import pprint

# Выведите на консоль значение площади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

radius = 42
pi = 3.1415926

circle_area = (pi * radius)**2
print(round(circle_area, 4))


# Далее, пусть есть координаты точки
# где 23 - координата х, 34 - координата у
# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

point = (23, 34)
origin_point = (0, 0)

origin_to_point = ((point[0] - origin_point[0])**2 + (point[1] - origin_point[1])**2) ** 0.5

pprint(round(origin_to_point, 4))

result = 0 < origin_to_point < 42

pprint(result)

#Аналогично для другой точки
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

point_2 = (30, 30)

origin_to_point_2 = ((point_2[0] - origin_point[0])**2 + (point_2[1] - origin_point[1])**2) ** 0.5

pprint(round(origin_to_point_2, 4))

result_2 = 0 < origin_to_point_2 < 42

pprint(result_2)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


