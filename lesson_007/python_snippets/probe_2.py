from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.foolness = 40
        self.money = 50
        self.happyness = 50
        self.food = 30
        self.sixpaks = 65

    def __str__(self):
        return 'Я - {}, денег - {}, еды - {} , сытость - {}, счастья в штанах - {}, вес - {}'.format(
            self.name, self.money, self.food, self.foolness, self.happyness, self.sixpaks)

    def shopping(self):
        if self.money > 20:
            if self.food < 30:
                cprint('{} закупился хавчиком'.format(self.name), color='green')
                self.sixpaks -= 1
                self.food += 40
                self.money -= 50
                self.foolness -= 5
                self.happyness += 15
            else:
                cprint('У {} есть хавчик'.format(self.name), color='cyan')
        else:
            cprint('у {} нэт дэнэг'.format(self.name), color='red')

    def eat(self):
        if self.foolness <= 30:
            if self.food > 10:
                cprint('{} поел'.format(self.name), color='green')
                self.sixpaks += 5
                self.foolness += 20
                self.happyness += 15
                self.food -= 30
            else:
                cprint('{} нет едыы'.format(self.name), color='red')
                self.sixpaks -= 1
        else:
            cprint('{} ссыт'.format(self.name))

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.money += 50
        self.foolness -= 1
        self.happyness -= 50
        self.sixpaks -= 1

    def play_DeusEx(self):
        cprint('{} играл в Deus EX'.format(self.name), color='magenta')
        self.sixpaks += 5
        self.foolness -= 5
        self.happyness += 20

    def fitness(self):
        cprint('{} посерфил'.format(Benji.name))
        self.sixpaks -= 30
        self.foolness -= 15
        self.happyness += 20

    def livin_the_dream(self):
        dice = randint(1, 6)
        if self.sixpaks >= 150:
            self.fitness()
        if self.foolness <= 20:
            self.eat()
        if self.food <= 30:
            self.shopping()
        if self.money < 20:
            self.work()
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.shopping()
        else:
            self.play_DeusEx()
        cprint(Benji, color='grey')


Benji = Man(name='Benji')

cprint(Benji, color='yellow')

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
    print('===============================DAY {} =============================='.format(day))
    Benji.livin_the_dream()
