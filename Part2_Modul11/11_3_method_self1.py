# Задача 1. Машина 2
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
 
# Добавьте два метода класса:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

import random

class Toyota:
    color = 'red'
    price = 1e6
    max_speed = 200
    cur_speed = 0

    def print_info(self):
        print('color: {}\nprice: {}\nmax_speed: {}\n'
              'cur_speed: {}'.format(self.color, self.price,
                                     self.max_speed, self.cur_speed))
    
    def set_speed(self, speed):
        self.cur_speed = speed
        car_1.print_info()
        

car_1 = Toyota()
car_1.print_info()
car_1.set_speed(random.randint(0, 200))
print(Toyota.cur_speed)
# обратите внимание, что скорость внутри Класса осталась той же, 
# её изменения не коснулись