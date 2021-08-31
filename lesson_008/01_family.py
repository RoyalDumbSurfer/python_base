# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dust = 0
        self.animal_food = 50
        self.child_food = 100

    def __str__(self):
        return 'В доме еды - {}, еды для детей - {}, еды для животных - {}, денег - {}, пыли - {}' \
            .format(self.food, self.child_food, self.animal_food, self.money, self.dust)


class Man:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.fullness = 30
        self.happyness = 100
        self.total_food_eaten = 0

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

    def pet_the_cat(self):
        self.happyness += 5
        cprint('{} играл с кошкой'.format(self.name), color='green')

    def act(self):
        if self.fullness <= 10:
            self.eat()
        dice = randint(1, 2)
        if dice == 1:
            self.pet_the_cat()
        else:
            self.eat()


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.total_money_earned = 0
        self.total_money_spend = 0
        self.total_surf_sessions = 0

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

    def animal_food_shopping(self):
        if self.house.money >= 10:
            cprint('{} сходил за едой для зверюшек'.format(self.name, color='green'))
            self.fullness -= 10
            self.house.animal_food += 20
            self.house.money -= 10
            self.total_money_spend += 10
        else:
            cprint('Нэт дэнэг на еду для зверюшек ;(', color='red')
            self.happyness -= 20

    def act(self):
        super().act()
        dice = randint(1, 4)
        if self.house.animal_food <= 10:
            self.animal_food_shopping()
        if self.house.money < 30:
            self.work()
        if self.happyness <= 10:
            self.surfing()
        if dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.animal_food_shopping()
        else:
            self.surfing()


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.total_spa_bought = 0
        self.total_money_spend = 0

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

    def child_food_shopping(self):
        if self.house.money >= 20:
            cprint('{} сходила за едой для детей'.format(self.name, color='green'))
            self.fullness -= 10
            self.house.child_food += 100
            self.house.money -= 100
            self.total_money_spend += 100
        else:
            cprint('Нэт дэнэг на еду для детей;(', color='red')
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

    def snorkeling(self):
        cprint('{} плавала в Океане'.format(self.name, color='green'))
        self.fullness -= 10
        self.happyness += 50

    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name, color='green'))
        self.fullness -= 10
        self.house.dust -= 40

    def act(self):
        super().act()
        dice = randint(1, 5)
        if self.house.child_food <= 20:
            self.child_food_shopping()
        if self.house.dust >= 70:
            self.clean_house()
        if self.house.food <= 30:
            self.shopping()
        if self.happyness <= 10:
            self.buy_all_day_spa()
        if dice == 1:
            self.shopping()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.snorkeling()
        elif dice == 4:
            self.child_food_shopping()
        else:
            self.buy_all_day_spa()


class Child:
    def __init__(self, name):
        self.name = name
        self.house = home
        self.happiness = 100
        self.fullness = 50
        self.total_food_eaten = 0

    def __str__(self):
        return 'Я - {}, счастья - {}, сытость - {}'.format(self.name, self.happiness, self.fullness)

    def sleep(self):
        cprint('{} - поспал'.format(self.name), color='green')
        self.fullness -= 10

    def eat(self):
        if self.fullness <= 30:
            if self.house.child_food >= 10:
                cprint('{} - поел'.format(self.name), color='green')
                self.fullness += 10
                self.house.child_food -= 10
                self.total_food_eaten += 10
            else:
                cprint('Нэт еды для {}'.format(self.name), color='red')
        else:
            cprint('{} не хочет есть'.format(self.name), color='green')

    def act(self):
        dice = randint(1, 3)
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        else:
            self.eat()


class Animal:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.fullness = 100
        self.total_food_eaten = 0

    def __str__(self):
        return 'Я - {}, моя сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.fullness < 40:
            if self.house.animal_food >= 10:
                cprint('{} поела'.format(self.name), color='green')
                self.fullness += 40
                self.house.animal_food -= 10
                self.total_food_eaten += 10
            else:
                cprint('В доме нэт еды для зверюшек', color='red')
        else:
            cprint('{} не голоден'.format(self.name), color='green')

    def sleep(self):
        cprint('{} поспала'.format(self.name), color='green')
        self.fullness -= 10

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        if dice == 1:
            self.eat()
        else:
            self.sleep()


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name=name)

    def soil(self):
        cprint('{} драла обои'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dust += 5

    def hunting(self):
        cprint('{} охотилась'.format(self.name), color='green')
        self.fullness -= 10

    def act(self):
        super().act()
        dice = randint(1, 2)
        if dice == 1:
            self.soil()
        else:
            self.hunting()


class Humster(Animal):
    def __init__(self, name):
        super().__init__(name=name)


home = House()
Dean = Husband(name='Дин')
Olusha = Wife(name='Олюша')

kids = [
    Child(name='Анна'),
    Child(name='Иван'),
    Child(name='Дина')
]

Fanya = Cat(name='Фаня')
Gadya = Humster(name='Гадя')

cprint(home, color='yellow')

cprint(Dean, color='yellow')

cprint(Olusha, color='yellow')

for kid in kids:
    cprint(kid, color='yellow')

cprint(Fanya, color='yellow')
cprint(Gadya, color='yellow')

for day in range(1, 365):
    if home.dust >= 90:
        Dean.happyness -= 10
        Olusha.happyness -= 10
    if Dean.happyness < 10:
        cprint('{} в депрессии'.format(Dean.name), color='red')
    if Olusha.happyness < 10:
        cprint('{} в депрессии'.format(Olusha.name), color='red')
    if Dean.fullness <= 0:
        cprint('{} очень голоден'.format(Dean.name), color='red')
    if Olusha.fullness <= 0:
        cprint('{} очень голодна'.format(Olusha.name), color='red')
    if kid.fullness <= 0:
        cprint('{} очень голоден'.format(kid.name), color='red')
    if Fanya.fullness <= 0:
        cprint('{} очень голодна'.format(Fanya.name), color='red')
    if Gadya.fullness <= 0:
        cprint('{} очень голодна'.format(Gadya.name), color='red')

    cprint('================== День {} =================='.format(day), color='red')
    home.dust += 5
    Dean.act()
    Olusha.act()
    for kid in kids:
        kid.act()
    Fanya.act()
    Gadya.act()
    cprint(Dean, color='cyan')
    cprint(Olusha, color='cyan')
    for kid in kids:
        cprint(kid, color='cyan')
    cprint(Fanya, color='cyan')
    cprint(Gadya, color='cyan')
    cprint(home, color='cyan')

cprint('Всего денег было заработанно {}'.format(Dean.total_money_earned), color='green')
if Dean.total_money_earned < Olusha.total_money_spend + Dean.total_money_spend:
    cprint('Всего денег было потраченно {}'.format(Olusha.total_money_spend + Dean.total_money_spend), color='red')
else:
    cprint('Всего денег было потраченно {}'.format(Olusha.total_money_spend + Dean.total_money_spend), color='green')
cprint('Всего Олюша съела еды {}'.format(Olusha.total_food_eaten), color='green')
cprint('Всего Дин съел еды {}'.format(Dean.total_food_eaten), color='green')
for kid in kids:
    cprint('Всего ребенок {} съел еды {}'.format(kid.name, kid.total_food_eaten), color='green')
cprint('Всего Фаня съела еды {}'.format(Fanya.total_food_eaten), color='green')
cprint('Всего Гадя съела еды {}'.format(Gadya.total_food_eaten), color='green')
cprint('Всего Олюша провела сессий в SPA {}'.format(Olusha.total_spa_bought), color='green')
cprint('Всего Дин откатал серф-сессий {}'.format(Dean.total_surf_sessions), color='green')
