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
        return "Не убивай."
    
    def punish(self):
        return 50


class DrunkError(Exception):
    def __str__(self):
        return "Не напивайся."
    
    def punish(self):
        return 10


class CarCrashError(Exception):
    def __str__(self):
        return "Не вреди ближнему."
    
    def punish(self):
        return 25


class GluttonyError(Exception):
    def __str__(self):
        return "Не переедай."
    
    def punish(self):
        return 10


class DepressionError(Exception):
    def __str__(self):
        return "Не прелюбодействуй"
    
    def punish(self):
        return 3


class Monk:
    def __init__(self):
        self.karma = 0

    def one_day(self):
        if random.randint(1, 10) == 5:
            return False
        else:
            return random.randint(1, 7)

    def attempt(self):
        self.days = 0
        current_dir = os.path.dirname(__file__)

        with open(os.path.join(current_dir, "karma.log"), "w", encoding="utf8") as karma_log:
            while self.karma < 500:
                try:
                    today = self.one_day()
                    self.days += 1
                    if today:
                        self.karma += today
                        print(f"День {self.days}: карма + {today}, итого: {self.karma}")
                    else:
                        exception = random.choice([KillError(), DrunkError(), CarCrashError(), 
                                                GluttonyError(), DepressionError()])
                        self.karma -= exception.punish()
                        raise exception
                except Exception as exc:
                    karma_log.write(f"День {str(self.days)}: {exc} Карма - {exception.punish()}\n")
                    print(f"День {self.days}: {exc} Карма - {exception.punish()}, итого: {self.karma}")
                if self.karma <= -100:
                    return False
            return True

monk = Monk()
if monk.attempt():
    print("Вы достигли просветления")
else:
    print("Гори в аду")