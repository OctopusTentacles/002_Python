# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов: 

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте 
# значение текущей скорости на случайное число от нуля до 200.

class Toyota(object):
    """docstring"""

    def __init__(self, color, price, max_speed, cur_speed):
        """Constructor"""
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.cur_speed = cur_speed