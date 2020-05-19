#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#preaty print выводит на консоль инфу в более удобном для восприятия виде
from pprint import pprint

# Есть словарь координат городов. Слварь tuple с координатами x и y

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

#пустой словарь distances

distances = dict()

#инициализируем переменные. Ссылки на кортежи в словаре.

london = cities['London']
moscow = cities['Moscow']
paris = cities['Paris']

#фомула рассчета расстояния. **0,5 - это корень из

moscow_london = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2) ** 0.5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2) ** 0.5
paris_london = ((paris[0] - london[0])**2 + (paris[1] - london[1])**2) ** 0.5

#заносим данные в словарь

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris


distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = paris_london

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_paris
distances['Paris']['London'] = paris_london

pprint(distances)

#print(distances['Moscow']['Paris'])


