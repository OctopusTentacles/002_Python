# Задача 2. Таймер 2
# Для замера времени передачи различных данных на множество сайтов вы написали 
# специальную функцию, которая сделала всю работу за вас, что позволило большую часть 
# времени смотреть видео с котиками в интернете. Однако, увидев свой код, вы как 
# программист с опытом поняли, что этот код можно написать намного красивее и удобнее.

# Реализуйте декоратор, который замеряет время работы задекорированной функции и 
# выводит ответ на экран. Для проверки примените декоратор к какой-нибудь 
# «тяжеловесной» функции и вызовите её в основной программе.

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
    return [x ** 2 ** x for x in range(22)]

hard_func()