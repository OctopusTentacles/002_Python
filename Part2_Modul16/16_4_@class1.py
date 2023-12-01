# Задача 1. Createtime
# Реализуйте декоратор класса, который выдаёт дату и время создания, 
# а также список всех методов объекта класса каждый раз, когда объект класса 
# создаётся в основном коде.


import time
import functools
from datetime import datetime
from typing import Callable


def createtime(cls):
    """ Декоратор класса, выводит время создания инстанса класса """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Время создания инстанса класса:", datetime.utcnow())
        return instance
    return wrapper

def timer(func: Callable) -> Callable:
    """ Декоратор время работы функции или метода """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Время работы функции:", end - start)
        return result
    return wrapper

def for_all_methods(decorator: Callable) -> Callable:
    """ Декоратор класса. Получает другой декоратор и 
        применяет его ко всем методам класса
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate

@createtime
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])
        return result
    
    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num**3 for i_num in range(self.max_num)])
        return result



my_funcs_1 = Functions(max_num=1000)
# time.sleep(2)
# my_funcs_2 = Functions(max_num=2000)
# time.sleep(2)
# my_funcs_3 = Functions(max_num=3000)

my_funcs_1.squares_sum()
my_funcs_1.cubes_sum(number=2000)