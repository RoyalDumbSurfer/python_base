# MAX_BUNCHES = 5
from random import randint

_holder = []


def put_stones():
    """расположить камни на игровой поверхности"""
    global _holder
    _holder = []
    for i in range(7):
        _holder.append(randint(1, 20))


def take_from_bunch(position, quantity):
    """взять из кучи камни"""
    if 1 <= position <= len(_holder):
        _holder[position-1] -= quantity


def get_bunches():
    """вывести количество камней в кучках"""
    return _holder


def is_gameover():
    """конец игры"""
    return sum(_holder) == 0
