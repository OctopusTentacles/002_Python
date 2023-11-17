# Задача 3. Логирование
# Реализуйте декоратор logging, который будет отвечать за логирование функций. 
# На экран выводится название функции и её документация. 
# Если во время выполнения декорируемой функции возникла ошибка, 
# то в файл function_errors.log записываются названия функции и ошибки.

# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения 
# первой же ошибки, а обрабатывала все декорируемые функции и сразу записывала 
# все ошибки в файл.

# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.


import os, random
import functools
from typing import Callable, Any
from datetime import datetime

cur_dir = os.path.dirname(__file__)


def logging(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print(f"Func: {func.__name__} | Doc: {func.__doc__}")
            func(*args, **kwargs)
        except Exception as exc:
            print(exc)
            with open(os.path.join(cur_dir, "function_errors.log"), 
                      "a", encoding="utf-8") as log:
                time_log = datetime.now()
                time_log = time_log.strftime("%d.%m.%Y %H:%M:%S")
                log.write(f"{time_log} | Func: {func.__name__}\t | Error: {exc}\n")

    return wrapped_func
    

@logging
def greeting():
    """ Возвращает приветственное сообщение. """
    return "Привет, пользователь!"

@logging
def division():
    """ Выполняет деление произвольных чисел. """
    num1 = random.randint(1, 3)
    num2 = random.randint(0, 1)
    return num1 / num2

@logging
def my_list():
    """ Создает список и возвращает определенный элемент из списка. """
    my_list = [i for i in range(random.randint(0, 4))]
    return my_list[3]


# =======================================================================================
greeting()
for _ in range(3):
    division()
for _ in range(3):
    my_list()