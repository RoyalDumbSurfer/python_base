# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dust = 0
        self.cat_food = 50

    def __str__(self):
        return 'В доме еды - {}, еды для Фани - {}, денег - {}, пыли - {}'.format(self.food, self.cat_food, self.money, self.dust)


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

    def pet_the_cat(self):
        self.happyness += 5
        cprint('{} играл с Фаней'.format(self.name))

    def act(self):
        dice = randint(1, 5)
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
        elif dice == 4:
            self.pet_the_cat()
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

    def cat_food_shopping(self):
        if self.house.money >= 10:
            cprint('{} сходила за едой для Фани'.format(self.name, color='green'))
            self.fullness -= 10
            self.house.cat_food += 10
            self.house.money -= 10
            self.total_money_spend += 10
        else:
            cprint('Нэт дэнэг на еду для Фани ;(', color='red')
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
        self.house.dust -= 40

    def pet_the_cat(self):
        self.happyness += 5
        cprint('{} играла с Фаней'.format(self.name))

    def act(self):
        dice = randint(1, 6)
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
        elif dice == 4:
            self.pet_the_cat()
        elif dice == 5:
            self.cat_food_shopping()
        else:
            self.buy_all_day_spa()


class Cat:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.fullness = 100
        self.total_cat_food_eaten = 0

    def __str__(self):
        return 'Я - {}, моя сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.fullness < 40:
            if self.house.cat_food >= 10:
                cprint('{} поела'.format(self.name), color='green')
                self.fullness += 40
                self.house.cat_food -= 10
                self.total_cat_food_eaten += 10
            else:
                cprint('В доме нэт кошачьей еды', color='red')
        else:
            cprint('Кот - {} не голоден'.format(self.name), color='green')

    def sleep(self):
        cprint('{} поспала'.format(self.name))
        self.fullness -= 10

    def soil(self):
        cprint('{} драла обои'.format(self.name))
        self.fullness -= 10
        self.house.dust += 5

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 20:
            self.eat()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()


home = House()
Dean = Husband(name='Дин')
Olusha = Wife(name='Олюша')
Fanya = Cat(name='Фаня')

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
    if Fanya.fullness < 0:
        cprint('{} очень голодна'.format(Fanya.name), color='red')
    cprint('================== День {} =================='.format(day), color='red')
    home.dust += 5
    Dean.act()
    Olusha.act()
    Fanya.act()
    cprint(Dean, color='cyan')
    cprint(Olusha, color='cyan')
    cprint(Fanya, color='cyan')
    cprint(home, color='cyan')

cprint('Всего денег было заработанно {}'.format(Dean.total_money_earned), color='green')
if Dean.total_money_earned < Olusha.total_money_spend:
    cprint('Всего денег было потраченно {}'.format(Olusha.total_money_spend), color='red')
else:
    cprint('Всего денег было потраченно {}'.format(Olusha.total_money_spend), color='green')
cprint('Всего Олюша съела еды {}'.format(Olusha.total_food_eaten), color='green')
cprint('Всего Дин съел еды {}'.format(Dean.total_food_eaten), color='green')
cprint('Всего Фаня съела еды {}'.format(Fanya.total_cat_food_eaten), color='green')
cprint('Всего Олюша провела сессий в SPA {}'.format(Olusha.total_spa_bought), color='green')
cprint('Всего Дин откатал серф-сессий {}'.format(Dean.total_surf_sessions), color='green')

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
