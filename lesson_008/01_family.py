# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dust = 0

    def __str__(self):
        return 'В доме еды - {}, денег - {}, пыли - {}'.format(self.food, self.money, self.dust)


class Husband:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.fullness = 30
        self.happyness = 100

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}'.format(self.name, self.fullness, self.happyness)

    def eat(self):
        cprint('{} поел'.format(self.name), color='green')
        self.fullness += 15
        self.house.food -= 15

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        cprint('{} играл в WoT'.format(self.name), color='magenta')
        self.happyness += 20
        self.fullness -= 10

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        if self.house.money < 20:
            self.work()
        if self.happyness <= 10:
            self.gaming()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        else:
            self.gaming()


class Wife:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.fullness = 30
        self.happyness = 100

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}'.format(self.name, self.fullness, self.happyness)

    def eat(self):
        cprint('{} поел'.format(self.name), color='green')
        self.fullness += 15
        self.house.food -= 15

    def shopping(self):
        cprint('{} сходила за продуктами'.format(self.name, color='green'))
        self.fullness -= 10
        self.house.food += 50
        self.house.money -= 50

    def buy_fur_coat(self):
        cprint('{} слетала в Италию за шубой'.format(self.name, color='green'))
        self.fullness -= 10
        self.house.money -= 350
        self.happyness += 60

    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name, color='green'))
        self.fullness -= 10
        self.house.dust -= 50

    def act(self):
        dice = randint(1, 4)
        if self.fullness <= 10:
            self.eat()
        if self.house.dust >= 70:
            self.clean_house()
        if self.house.food <= 30:
            self.shopping()
        if self.happyness <= 10:
            self.buy_fur_coat()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.clean_house()
        else:
            self.buy_fur_coat()


home = House()
Serge = Husband(name='Сережа')
Masha = Wife(name='Маша')

for day in range(1, 7):
    if home.dust >= 90:
        Serge.happyness -= 10
        Masha.happyness -= 10
    if Serge.happyness < 10:
        cprint('{} в депрессии'.format(Serge.name), color='red')
    if Masha.happyness < 10:
        cprint('{} в депрессии'.format(Masha.name), color='red')
    if Serge.fullness < 0:
        cprint('{} очень голоден'.format(Serge.name), color='red')
    if Masha.fullness < 0:
        cprint('{} очень голодна'.format(Masha.name), color='red')
    cprint('================== День {} =================='.format(day), color='red')
    home.dust += 5
    Serge.act()
    Masha.act()
    cprint(Serge, color='cyan')
    cprint(Masha, color='cyan')
    cprint(home, color='cyan')

# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#
#
#
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
#
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
