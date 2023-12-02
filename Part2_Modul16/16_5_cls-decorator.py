# Декоратор как класс
# Декоратор вывода количества использования функции
# Написание класса-декоратора CountCalls
# Создание декоратора с помощью метода call

from typing import Callable
import functools

class CountCalls:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0


def say_hello():
    print("Hello!")


say_hello()
say_hello()
say_hello()