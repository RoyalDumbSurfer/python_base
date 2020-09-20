# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from central_street.house1 import room1

print(room1.folks)
from central_street.house1 import room2

print(room2.folks)

from central_street.house2 import room1

print(room1.folks)
from central_street.house2 import room2

print(room2.folks)

from soviet_street.house1 import room1

print(room1.folks)
from soviet_street.house1 import room2

print(room2.folks)

from soviet_street.house2 import room1

print(room1.folks)
from soviet_street.house2 import room2

print(room2.folks)
