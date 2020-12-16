from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.foolness = 50
        self.money = 50
        self.happyness = 50
        self.food = 50
        self.sixpaks = 65

    def __str__(self):
        return 'Я - {}, денег - {}, еды - {} , сытость - {}, счастья в штанах - {}, вес - {}'.format(
            self.name, self.money, self.food, self.foolness, self.happyness, self.sixpaks)

    def shopping(self):
        if self.money > 20:
            if self.food < 30:
                cprint('{} закупился хавчиком'.format(self.name), color='green')
                self.sixpaks -= 2
                self.food += 50
                self.money -= 50
                self.foolness -= 20
                self.happyness -= 15
            else:
                cprint('У {} есть хавчик'.format(self.name), color='cyan')
        else:
            cprint('у {} нэт дэнэг'.format(self.name), color='red')

    def eat(self):
        if self.foolness <= 30:
            if self.food > 10:
                cprint('{} поел'.format(self.name), color='green')
                self.sixpaks += 2
                self.foolness += 50
                self.happyness += 15
                self.food -= 30
            else:
                cprint('{} нет едыы'.format(self.name), color='red')
                self.sixpaks -= 3
        else:
            cprint('{} ссыт'.format(self.name))

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.money += 50
        self.foolness -= 5
        self.happyness -= 50
        self.sixpaks -= 3

    def play_DeusEx(self):
        cprint('{} играл в Deus EX'.format(self.name), color='magenta')
        self.sixpaks += 2
        self.foolness -= 10
        self.happyness += 20

    def livin_the_dream(self):
        dice = randint(1, 6)
        if self.foolness <= 30:
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
    if Benji.foolness <= 0:
        cprint('{} умер от голода...'.format(Benji.name), color='red')
        break
    if Benji.sixpaks >= 250:
        cprint('{} умер от ожирения...'.format(Benji.name), color='red')
        break
    print('===============================DAY {} =============================='.format(day))
    Benji.livin_the_dream()
