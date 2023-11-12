# Задача 2. Таймер
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить 
# скорость передачи данных на нескольких десятках сайтов. Конечно же, вручную «щёлкать» 
# сайты и замерять время вам было лень, поэтому возникла идея написать «автотест», 
# который всё сделает сам.

# С помощью понятия функции высшего порядка реализуйте функцию-таймер, 
# которая замеряет время работы переданной функции func и выдаёт ответ на экран.

# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.


import time
from typing import Callable, Any

def timer(func: Callable) -> Any:
    start = time.time()
    func()
    stop = time.time()
    return round(stop - start, 2)

def hard_func():
    return [x ** 2 ** x for x in range(22)]


print(timer(hard_func))

# =======================================================================================

def timer(func: Callable, *args, **kwargs) -> Any:
    """ Функция-таймер - выводит время работы функции и возвращает ее результат"""
    start = time.time()
    result = func(*args, **kwargs)
    stop = time.time()
    run_time = round(stop - start, 3)
    print("Функция работала {} сек.".format(run_time))
    return result

def hard_func(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([num ** 3 for num in range(10000)])
    return result


print(timer(hard_func, 200))