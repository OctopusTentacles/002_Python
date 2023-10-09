# Задача 2. Карма
# Что нужно сделать
# Один буддист-программист решил создать свой симулятор жизни, 
# в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления. 

# Каждый день вызывается специальная функция one_day(), 
# которая возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть 
# одно из исключений:

# KillError,
# DrunkError,
# CarCrashError,
# GluttonyError,
# DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)

# Напишите такую программу. Функцию оберните в бесконечный цикл, 
# выход из которого возможен только при накоплении кармы до уровня константы. 
# Исключения обработайте и запишите в отдельный лог karma.log.

# По итогу у вас может быть примерно такая структура программы:

# открываем файл
# цикл по набору кармы
#    try
#       карма += one_day()
#    except(ы) с указанием классов исключений, которые нужно поймать
#       добавляем запись в файл
# закрываем файл


import os
import random


class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

def one_day():
    if random.randint(1, 10) == 5:
        return False
    else:
        return random.randint(1, 7)

days = 0
karma = 0
current_dir = os.path.dirname(__file__)
# with open(os.path.join(current_dir, "karma.log"), "w", encoding="utf8") as karma_log:

while karma < 500:
        try:
            today = one_day()
            days += 1
            if today:
                karma += today
                print(f"День: {days}, карма: {karma}")
            else:
                raise Exception("не повезло")
        except Exception as exc:
            print(exc, type(exc))

