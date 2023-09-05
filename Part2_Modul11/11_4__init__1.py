# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. 
# На всякий случай вот описание класса.

# Четыре атрибута:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).

# Два метода:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.

# Теперь все четыре атрибута должны инициализироваться при создании 
# экземпляра класса (то есть передаваться в init). 
# Реализуйте такое изменение класса.

import random

class Toyota:

    def __init__(self, color, price, max_speed, cur_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.cur_speed = cur_speed

    def print_info(self):
        print('color: {}\nprice: {}\nmax_speed: {}\n'
              'cur_speed: {}'.format(self.color, self.price, 
                                     self.max_speed, self.cur_speed))
        
    def set_speed(self, speed):
        self.cur_speed = speed
        car_1.print_info()


car_1 = Toyota('red', 1e6, 200, 0)
car_2 = Toyota('red', 1e6, 200, random.randint(0, 200))

car_1.print_info()
car_2.print_info()