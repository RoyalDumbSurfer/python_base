from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 40
        self.happyness = 50
        self.sixpaks = 65
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}, вес - {}'.format(
            self.name, self.fullness, self.happyness, self.sixpaks)

    def shopping(self):
        if self.house.money > 20:
            if self.house.food < 30:
                cprint('{} закупился хавчиком'.format(self.name), color='green')
                self.sixpaks -= 1
                self.house.food += 40
                self.house.money -= 50
                self.fullness -= 5
                self.happyness += 15
            else:
                cprint('У {} есть хавчик'.format(self.name), color='cyan')
        else:
            cprint('у {} нэт дэнэг'.format(self.name), color='red')

    def eat(self):
        if self.fullness <= 30:
            if self.house.food > 10:
                cprint('{} поел'.format(self.name), color='green')
                self.sixpaks += 5
                self.fullness += 20
                self.happyness += 15
                self.house.food -= 30
            else:
                cprint('{} нет едыы'.format(self.name), color='red')
                self.sixpaks -= 1
        else:
            cprint('{} ссыт'.format(self.name))

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 1
        self.happyness -= 50
        self.sixpaks -= 1

    def play_DeusEx(self):
        cprint('{} играл в Deus EX'.format(self.name), color='magenta')
        self.sixpaks += 5
        self.fullness -= 5
        self.happyness += 20

    def fitness(self):
        cprint('{} посерфил'.format(self.name))
        self.sixpaks -= 30
        self.fullness -= 15
        self.happyness += 20

    def into_the_house(self, house):
        self.house = house
        self.happyness += 10
        self.fullness -= 10
        self.sixpaks -= 2
        cprint('{} заселился на виллу!!!'.format(self.name), color='red')

    def livin_the_dream(self):
        dice = randint(1, 6)
        if self.sixpaks >= 150:
            self.fitness()
        if self.fullness <= 20:
            self.eat()
        if self.house.food <= 30:
            self.shopping()
        if self.house.money < 20:
            self.work()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.shopping()
        else:
            self.play_DeusEx()


class Cat:

    def __init__(self, name):
        self.name = name
        self.happyness = 20
        self.fullness = 50
        self.weight = 5

    def __str__(self):
        return 'Я кошка - {}, счастья - {}, сытость - {}, вес - {}'.format(
            self.name, self.happyness, self.fullness, self.weight)

    def cat_into_the_house(self, house):
        self.house = house
        self.happyness += 20
        self.fullness -= 2
        self.weight -= 0.5
        cprint('Кошка {} заселилась на виллу!!!'.format(self.name), color='red')


class House:

    def __init__(self):
        self.food = 50
        self.money = 30
        self.cat_food = 50

    def __str__(self):
        return 'В доме еды - {}, денег - {}'.format(self.food, self.money)


citizens = [
    Man(name='Тедд'),
    Man(name='Билл'),
    Man(name='Бенджи'),
    Man(name='Бивис'),
    Man(name='Валера'),
    Man(name='Батхед'),
]

my_sweet_villa = House()
for citizen in citizens:
    citizen.into_the_house(house=my_sweet_villa)

for citizen in citizens:
    cprint(citizen, color='yellow')
cprint(my_sweet_villa, color='yellow')

for day in range(1, 366):
    if citizen.happyness <= 0:
        cprint('{} грустный'.format(citizen.name), color='red')
    if citizen.fullness <= 0:
        cprint('{} умер от голода...'.format(citizen.name), color='red')
        break
    if citizen.sixpaks >= 250:
        cprint('{} умер от ожирения...'.format(citizen.name), color='red')
        break
    if citizen.sixpaks <= 35:
        cprint('{} умер от истощения...'.format(citizen.name), color='red')
        break

    print('===============================DAY {} =============================='.format(day))
    for citizen in citizens:
        citizen.livin_the_dream()
    print('===============================END of THE DAY {}=============================='.format(day))
    for citizen in citizens:
        cprint(citizen, color='grey')
    cprint(my_sweet_villa, color='grey')
