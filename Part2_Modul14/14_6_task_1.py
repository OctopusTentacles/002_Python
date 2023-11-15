# Задача 1. Как дела?
# Что нужно сделать
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. 
# Он написал надоедливый декоратор, который при вызове декорируемой функции 
# спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то 
# вроде «А у меня не очень!» и только потом запускает саму функцию. 
# Правда, после такой выходки Васю чуть не уволили с работы.

# Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

# Пример кода:

# @how_are_you
# def test():
#     print('<Тут что-то происходит...>')

# test()
# Результат:
# Как дела? Хорошо.
# А у меня не очень! Ладно, держи свою функцию.
# <Тут что-то происходит...>


import functools
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """ надоедливый декоратор"""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        func(*args, **kwargs)
    return wrapped_func

@how_are_you
def test_1():
    """ функция вывода информации"""
    print('<Тут что-то происходит...>')

@how_are_you
def test_2():
    """ функция вывода информации"""
    print('Василий, ты уволен!')


print(test_1.__name__, test_1.__doc__)
print(test_2.__name__, test_2.__doc__)

test_1()
test_2()
