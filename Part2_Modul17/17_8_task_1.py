# Задача 1. Новые списки
# Даны три списка: 

# Напишите код, который создаёт три новых списка. Вот их содержимое:

# Каждое число из списка floats возводится в третью степень и округляется 
# до трёх знаков после запятой.
# Из списка names берутся только имена минимум из пяти букв.
# Из списка numbers берётся произведение всех чисел.


from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1] # 1,101,109,680


def sum_numbers(elem_1: int, elem_2: int) -> int:
    """ Используется с функцией reduce - считает произведение чисел в списке.
    """
    elem_1 *= elem_2
    return elem_1


print(list(map(lambda x: round(x ** 3, 3), floats)))
print(list(filter(lambda x: len(x) >= 5, names)))
print(reduce(sum_numbers, numbers))