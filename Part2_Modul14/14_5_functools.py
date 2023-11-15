# Модуль functools. Декоратор functools.wraps()

import time
from typing import Callable, Any


def timer(func: Callable) -> Any:
    """ Декоратор timer - выводит время работы функции и возвращает ее результат"""

    def wrapped_func(*args, **kwargs):
        start_at = time.time()
        result = func(*args, **kwargs)
        stop_at = time.time()
        print(round(stop_at - start_at, 2))
        return result
    return wrapped_func

@timer
def hard_func():
    """ Тяжелая функция, занимет много времени на выполнение"""
    return [x ** 2 ** x for x in range(22)]

print(hard_func.__doc__)
print(hard_func.__name__)

hard_func()

