# Задача 2. Замедление кода
# Что нужно сделать
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить. 
# Типичный пример — функция, которая постоянно проверяет, изменились ли данные на 
# веб-странице или её код.

# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт 
# несколько секунд.

# Во всех декораторах используется functools.wraps.


import time
import functools
from typing import Callable, Any


def delay(func: Callable) -> Callable:
    """ def in_process - декоратор для задержки выполнения функции
    """
    @functools.wraps(func)
    def wrapped_func() -> Any:
        time.sleep(5)
        func()
    return wrapped_func


@delay
def check_data():
    """ def check_data - вывод статуса"""
    print("Данные обновлены!")


check_data()