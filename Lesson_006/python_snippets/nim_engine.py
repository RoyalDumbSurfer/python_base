from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}


def put_stones():
    """расположить камни на игровой поверхности"""
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHES_SIZE)


def take_from_bunch(position, quantity):
    """взять из кучи камни"""
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_bunches():
    """вывести количество камней в кучках"""
    res = []
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res


def is_gameover():
    """конец игры"""
    return sum(_holder.values()) == 0
