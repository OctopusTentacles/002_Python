# Задача 4. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов 
# декорируемой функции.

# Для решения задачи нельзя использовать операторы global и nonlocal 
# об этом мы ещё расскажем).

# Во всех декораторах используется functools.wraps.


import random
import functools
from typing import Callable, Any


def counter(self, func: Callable) -> Callable:
    """ """

    self.count = 0
    def wrapper(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        self.count += 1
        print(count)
    return wrapper


def creat_list():
    """ Создает список и возвращает определенный элемент из списка. """
    my_list = [i for i in range(random.randint(0, 4))]
    return my_list
