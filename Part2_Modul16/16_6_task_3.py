# Задача 3. Логирование в формате

# Реализуйте декоратор, который будет логировать все методы декорируемого 
# класса (кроме магических методов) и в который можно передавать формат вывода 
# даты и времени логирования.

# Результат:
# Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37. 
# Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37. 
# Тут метод test_sum_1.
# Завершение 'A.test_sum_1', время работы = 0,187 s. 
# Тут метод test_sum_1 у наследника.
# Завершение 'B.test_sum_1', время работы = 0,187 s. 
# Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37. 
# Тут метод test_sum_2 у наследника.
# Завершение 'B.test_sum_2', время работы = 0,370 s.

# Совет: 
# внимательно пересмотрите видео 29.4, если сталкиваетесь с трудностями в этой задаче.

import time
import functools
from typing import Callable, Any, Optional



def timer(_func: Optional[Callable]=None, *, date) -> Callable:
    """ """
    def decorator_time(func: Callable) -> Callable:
        """ """
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            start = time.time()
            result = func(*args, **kwargs)
            stop = time.time()
            print("время работы =", start - stop)
            return result
        return wrapped_func
    if _func is None:
        return decorator_time
    else:
        decorator_time(_func)


@timer("date")
def log_methods(cls):

    @functools.wraps(cls)
    def wrapper(cls):
        for i_def in dir(cls):
            if i_def.startswith('__') is False:
                cur_def = getattr(cls, i_def)
                print("Запускается", cls.__name__, cur_def.__name__)
                cur_def()
        return cls
    return wrapper





@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()