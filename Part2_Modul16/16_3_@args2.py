# Задача 2. Замедление кода 2
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор, 
# который перед выполнением декорируемой функции ждёт несколько секунд. 

# Модернизируйте этот декоратор так, чтобы количество секунд можно было 
# передавать в качестве аргумента. По умолчанию декоратор ждёт одну секунду. 
# Помимо этого сделайте так, чтобы декоратор можно было использовать 
# как с аргументами, так и без них.

import time
import functools
from typing import Callable, Any, Optional


def control_delay(_func: Optional[Callable]=None, *, seconds: int = 1) -> Callable:
    def delay(func: Callable) -> Callable:
        """ def in_process - декоратор для задержки выполнения функции
        """
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapped_func
    
    if _func is None:
        return delay
    else:
        return delay(_func)



@control_delay(seconds=10)
def check_data():
    """ def check_data - вывод статуса"""
    print("Данные обновлены!")


check_data()