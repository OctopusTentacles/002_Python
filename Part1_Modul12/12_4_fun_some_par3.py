# Задача 3. GPS-навигатор 2.0

# Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку.
# Теперь пользователь может не только смотреть расстояние от себя до объекта,
# но и задавать в навигаторе две произвольные точки,
# после чего на экран ему выводится расстояние между ними.
# Для этого пользователь вводит четыре действительных числа
# x1, y1, x2, y2 — это как раз координаты этих двух точек.

# Напишите программу, где у пользователя спрашивается,
# чего он хочет — найти расстояние от себя до точки или
# найти расстояние между двумя произвольными точками,
# после чего запрашиваются необходимые координаты
# точек и выводится ответ на экран.

import math


def to_dot(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print('расстояние от себя до точки =', distance)


def between(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print('расстояние между точками =', distance)


choise = int(input(
    'Найти расстояние от себя до точки (1) или расстояние между двумя произвольными точками (2): '))
if choise == 1:
    x = float(input('Введите координату Х точки: '))
    y = float(input('Введите координату Y точки: '))
    to_dot(x, y)
elif choise == 2:
    x1 = float(input('Введите координату Х точки 1: '))
    y1 = float(input('Введите координату Y точки 1: '))
    x2 = float(input('Введите координату Х точки 2: '))
    y2 = float(input('Введите координату Y точки 2: '))
    between(x1, y1, x2, y2)
else:
    print('Ввод неверный')