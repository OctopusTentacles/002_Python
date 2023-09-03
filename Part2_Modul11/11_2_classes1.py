# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов: 

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте 
# значение текущей скорости на случайное число от нуля до 200.


import random


# класс Toyota
class Toyota:

# состоящий из четырёх статических атрибутов:
    color = 'red'
    price = 1e6
    max_speed = 200
    cur_speed = 0

# экземпляр класса:
toyota_1 = Toyota()
toyota_2 = Toyota()
toyota_3 = Toyota()

toyota_1.cur_speed = random.randint(0, 200)
toyota_2.cur_speed = random.randint(0, 200)
toyota_3.cur_speed = random.randint(0, 200)

print(toyota_1.cur_speed, toyota_2.cur_speed, toyota_3.cur_speed)