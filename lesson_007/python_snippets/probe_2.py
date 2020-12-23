from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.foolness = 40
        self.happyness = 50
        self.sixpaks = 65
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}, вес - {}'.format(
            self.name, self.foolness, self.happyness, self.sixpaks)

    def shopping(self):
        if self.house.money > 20:
            if self.house.food < 30:
                cprint('{} закупился хавчиком'.format(self.name), color='green')
                self.sixpaks -= 1
                self.house.food += 40
                self.house.money -= 50
                self.foolness -= 5
                self.happyness += 15
            else:
                cprint('У {} есть хавчик'.format(self.name), color='cyan')
        else:
            cprint('у {} нэт дэнэг'.format(self.name), color='red')

    def eat(self):
        if self.foolness <= 30:
            if self.house.food > 10:
                cprint('{} поел'.format(self.name), color='green')
                self.sixpaks += 5
                self.foolness += 20
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
        self.foolness -= 1
        self.happyness -= 50
        self.sixpaks -= 1

    def play_DeusEx(self):
        cprint('{} играл в Deus EX'.format(self.name), color='magenta')
        self.sixpaks += 5
        self.foolness -= 5
        self.happyness += 20

    def fitness(self):
        cprint('{} посерфил'.format(self.name))
        self.sixpaks -= 30
        self.foolness -= 15
        self.happyness += 20

    def into_the_house(self, house):
        self.house = house
        self.foolness -= 10
        self.sixpaks -= 2
        self.house.money -= 15
        cprint('{} заселился на виллу!!!'.format(self.name), color='yellow')

    def livin_the_dream(self):
        dice = randint(1, 6)
        if self.sixpaks >= 150:
            self.fitness()
        if self.foolness <= 20:
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


class House:
    def __ini__(self):
        self.food = 35
        self.money = 50
    def __str__(self):
        return 'Я - {}, сытость - {}, счастья в штанах - {}, вес - {}'.format(
            self.name, self.foolness, self.happyness, self.sixpaks)


Benji = Man(name='Бенджи')
Beavis = Man(name='Бивис')
Butthead = Man(name='Батхед')

cprint(Benji, color='yellow')
cprint(Beavis, color='yellow')
cprint(Butthead, color='yellow')

for day in range(1, 366):
    if Benji.happyness <= 0:
        cprint('{} грустный'.format(Benji.name), color='red')
    if Benji.foolness <= 0:
        cprint('{} умер от голода...'.format(Benji.name), color='red')
        break
    if Benji.sixpaks >= 250:
        cprint('{} умер от ожирения...'.format(Benji.name), color='red')
        break
    if Benji.sixpaks <= 35:
        cprint('{} умер от истощения...'.format(Benji.name), color='red')
        break
    if Butthead.happyness <= 0:
        cprint('{} грустный'.format(Butthead.name), color='red')
    if Butthead.foolness <= 0:
        cprint('{} умер от голода...'.format(Butthead.name), color='red')
        break
    if Butthead.sixpaks >= 250:
        cprint('{} умер от ожирения...'.format(Butthead.name), color='red')
        break
    if Butthead.sixpaks <= 35:
        cprint('{} умер от истощения...'.format(Butthead.name), color='red')
        break
    if Beavis.happyness <= 0:
        cprint('{} грустный'.format(Beavis.name), color='red')
    if Beavis.foolness <= 0:
        cprint('{} умер от голода...'.format(Beavis.name), color='red')
        break
    if Beavis.sixpaks >= 250:
        cprint('{} умер от ожирения...'.format(Beavis.name), color='red')
        break
    if Beavis.sixpaks <= 35:
        cprint('{} умер от истощения...'.format(Beavis.name), color='red')
        break

    print('===============================DAY {} =============================='.format(day))
    Benji.livin_the_dream()
    Butthead.livin_the_dream()
    Beavis.livin_the_dream()
    cprint(Benji, color='grey')
    cprint(Beavis, color='grey')
    cprint(Butthead, color='grey')
