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
        self.total_money_earned = 0
        self.total_surf_sessions = 0
        self.total_food_eaten = 0
        self.fullness = 30
        self.happyness = 100

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}'.format(self.name, self.fullness, self.happyness)

    def eat(self):
        if self.house.food >= 25:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness += 25
            self.house.food -= 25
            self.total_food_eaten += 25
        else:
            cprint('В доме нэт еды;(', color='red')
            self.happyness -= 20

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.house.money += 450
        self.fullness -= 20
        self.total_money_earned += 450

    def gaming(self):
        cprint('{} играл в Deus Ex'.format(self.name), color='magenta')
        self.happyness += 20
        self.fullness -= 10

    def surfing(self):
        cprint('{} серфил в трубах'.format(self.name), color='magenta')
        self.happyness += 30
        self.fullness -= 20
        self.total_surf_sessions += 1

    def act(self):
        dice = randint(1, 4)
        if self.fullness <= 10:
            self.eat()
        if self.house.money < 30:
            self.work()
        if self.happyness <= 10:
            self.surfing()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.gaming()
        else:
            self.surfing()


class Wife:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.total_food_eaten = 0
        self.total_spa_bought = 0
        self.total_money_spend = 0
        self.fullness = 30
        self.happyness = 100

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}'.format(self.name, self.fullness, self.happyness)

    def eat(self):
        if self.house.food >= 25:
            cprint('{} поела'.format(self.name), color='green')
            self.fullness += 25
            self.house.food -= 25
            self.total_food_eaten += 25
        else:
            cprint('В доме нэт еды;(', color='red')
            self.happyness -= 20

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходила за продуктами'.format(self.name, color='green'))
            self.fullness -= 10
            self.house.food += 50
            self.house.money -= 50
            self.total_money_spend += 50
        else:
            cprint('Нэт дэнэг на продукты ;(', color='red')
            self.happyness -= 20

    def buy_all_day_spa(self):
        if self.house.money >= 350:
            cprint('{} сходила в SPA'.format(self.name, color='green'))
            self.fullness -= 10
            self.house.money -= 350
            self.happyness += 60
            self.total_spa_bought += 1
            self.total_money_spend += 350
        else:
            cprint('Нэт дэнэг на SPA;(', color='red')
            self.happyness -= 20

    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name, color='green'))
        self.fullness -= 10
        self.house.dust -= 30

    def act(self):
        dice = randint(1, 4)
        if self.fullness <= 10:
            self.eat()
        if self.house.dust >= 70:
            self.clean_house()
        if self.house.food <= 30:
            self.shopping()
        if self.happyness <= 10:
            self.buy_all_day_spa()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.clean_house()
        else:
            self.buy_all_day_spa()


home = House()
Dean = Husband(name='Дин')
Olusha = Wife(name='Олюша')

for day in range(1, 365):
    if home.dust >= 90:
        Dean.happyness -= 10
        Olusha.happyness -= 10
    if Dean.happyness < 10:
        cprint('{} в депрессии'.format(Dean.name), color='red')
    if Olusha.happyness < 10:
        cprint('{} в депрессии'.format(Olusha.name), color='red')
    if Dean.fullness < 0:
        cprint('{} очень голоден'.format(Dean.name), color='red')
    if Olusha.fullness < 0:
        cprint('{} очень голодна'.format(Olusha.name), color='red')
    cprint('================== День {} =================='.format(day), color='red')
    home.dust += 5
    Dean.act()
    Olusha.act()
    cprint(Dean, color='cyan')
    cprint(Olusha, color='cyan')
    cprint(home, color='cyan')

cprint('Всего денег было заработанно {}'.format(Dean.total_money_earned), color='green')
if Dean.total_money_earned < Olusha.total_money_spend:
    cprint('Всего денег было потраченно {}'.format(Olusha.total_money_spend), color='red')
else:
    cprint('Всего денег было потраченно {}'.format(Olusha.total_money_spend), color='green')
cprint('Всего Олюша съела еды {}'.format(Olusha.total_food_eaten), color='green')
cprint('Всего Дин съел еды {}'.format(Dean.total_food_eaten), color='green')
cprint('Всего Олюша провела сессий в SPA {}'.format(Olusha.total_spa_bought), color='green')
cprint('Всего Дин откатал серф-сессий {}'.format(Dean.total_surf_sessions), color='green')

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
