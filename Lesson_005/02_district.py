# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from central_street.house1 import room1

print('На районе живут: ')
print(', '.join(room1.folks))

from central_street.house1 import room2

print(', '.join(room2.folks))

from central_street.house2 import room1

print(', '.join(room1.folks))
from central_street.house2 import room2

print(', '.join(room2.folks))
from soviet_street.house1 import room1

print(', '.join(room1.folks))
from soviet_street.house1 import room2

print(', '.join(room2.folks))
from soviet_street.house2 import room1

print(', '.join(room1.folks))
from soviet_street.house2 import room2

print(', '.join(room2.folks))


def find_list(pakage, list_name):
    if list_name in pakage:
        return print(', '.join(list_name))
    for key, sub_pakage in pakage.items():
        if isinstance(sub_pakage, list):
            result = find_list(pakage=sub_pakage, list_name=list_name)
            if result:
                break
    else:
        result = None
    return result


res = find_list(pakage='soviet_street.house2', list_name=list)
print(res)
