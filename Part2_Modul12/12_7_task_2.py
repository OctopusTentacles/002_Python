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
    def __str__(self):
        return "Убийство. Очень-очень плохо."

class DrunkError(Exception):
    def __str__(self):
        return "Ты сегодня напился."

class CarCrashError(Exception):
    def __str__(self):
        return "Авария, очень плохо"

class GluttonyError(Exception):
    def __str__(self):
        return "Ты сегодня переел."

class DepressionError(Exception):
    def __str__(self):
        return "Успокойся"

def one_day():
    if random.randint(1, 10) == 5:
        return False
    else:
        return random.randint(1, 7)

days = 0
karma = 0
current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, "karma.log"), "w", encoding="utf8") as karma_log:

    while karma < 500:
        try:
            today = one_day()
            days += 1
            if today:
                karma += today
                print(f"День: {days}, карма + {today}, итого: {karma}")
            else:
                karma -= 5
                raise Exception("не повезло")
        except Exception as exc:
            karma_log.write(f"День: {str(days)}, {exc}\n")
            print(f"День: {days}, {exc}, карма - {5}, итого: {karma}")

