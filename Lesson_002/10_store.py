#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# Вариант_1
# лампы, столы, диваны

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print('Лампа -', store[goods['Лампа']][0]['quantity'], 'шт.', 'Стоимость -', lamps_cost, 'руб.' )

table_cost_1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table_cost_2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print('Стол_1 -', store[goods['Стол']][0]['quantity'], 'шт.', 'Стоимость -',  table_cost_1, 'руб.')
print('Стол_2 -', store[goods['Стол']][1]['quantity'], 'шт.', 'Стоимость -',  table_cost_2, 'руб.')

sofa_cost_1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofa_cost_2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
print('Диван_1 -', store[goods['Диван']][0]['quantity'], 'шт.', 'Стоимость -',  sofa_cost_1, 'руб.')
print('Диван_2 -', store[goods['Диван']][1]['quantity'], 'шт.', 'Стоимость -',  sofa_cost_2, 'руб.')

# Вариант_2
# стулья

cost_code = goods['Стул']

chair_item_1 = store[cost_code][0]
chair_item_2 = store[cost_code][1]
chair_item_3 = store[cost_code][2]

chair_quantity_1 = chair_item_1['quantity']
chair_quantity_2 = chair_item_2['quantity']
chair_quantity_3 = chair_item_3['quantity']

chair_price_1 = chair_item_1['price']
chair_price_2 = chair_item_2['price']
chair_price_3 = chair_item_3['price']

chair_cost_1 = chair_item_1['quantity'] * chair_item_1['price']
chair_cost_2 = chair_item_2['quantity'] * chair_item_2['price']
chair_cost_3 = chair_item_3['quantity'] * chair_item_3['price']

print('Стул_1 -', chair_quantity_1, 'шт.', 'Стоимость -',  chair_cost_1, 'руб.')
print('Стул_2 -', chair_quantity_2, 'шт.', 'Стоимость -',  chair_cost_2, 'руб.')
print('Стул_3 -', chair_quantity_3, 'шт.', 'Стоимость -',  chair_cost_3, 'руб.')


# пример
#lamp_code = goods['Лампа']
#lamps_item = store[lamp_code][0]
#lamps_quantity = lamps_item['quantity']
#lamps_price = lamps_item['price']
#lamps_cost = lamps_quantity * lamps_price
#print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.



##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






