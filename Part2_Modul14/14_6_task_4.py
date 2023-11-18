# Задача 4. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов 
# декорируемой функции.

# Для решения задачи нельзя использовать операторы global и nonlocal 
# об этом мы ещё расскажем).

# Во всех декораторах используется functools.wraps.


import random
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    """ Декоратор, считающий и выводящий количество вызовов
        декорируемой функции.
    """
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("Функция {} была вызвана {} раз.".format(
            func.__name__, wrapper.count
        ))
        return res
    wrapper.count = 0
    return wrapper


@counter
def some_func(): ...


for _ in range(random.randint(1, 13)):
    some_func()