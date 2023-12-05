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
from datetime import datetime
from typing import Callable, Any, Optional



def logger(cls, cur_method, form_date) -> Callable:
    """ """
    @functools.wraps(cls)
    def wrapped_func(*args, **kwargs) -> Any:
        # преобразование шаблона даты
        new_form_date = ''
        for i in form_date:
            if i.isalpha():
                new_form_date = ''.join(new_form_date + '%' + i)
            else:
                new_form_date = ''.join(new_form_date + i)

        current_date_time = datetime.now()
        print(current_date_time)
        format_date_time = current_date_time.strftime((form_date))

        print("Запускается '{}.{}'. Дата и время заппуска: {}".format(
            cls.__name__, cur_method.__name__, format_date_time))
        
        start = time.time()
        result = cur_method(*args, **kwargs)
        stop = time.time()

        print("Завершение '{}.{}', время работы = {} s.".format(
            cls.__name__, cur_method.__name__, round(stop - start, 3)
        ))
        return result
    return wrapped_func





def log_methods(form_date):
    """ """
    @functools.wraps(form_date)
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = logger(cls, cur_method, form_date)
                setattr(cls, i_method, decorated_method)

                
                # cur_def()
        return cls
    return decorate





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