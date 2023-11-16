# Задача 3. Логирование
# Реализуйте декоратор logging, который будет отвечать за логирование функций. 
# На экран выводится название функции и её документация. 
# Если во время выполнения декорируемой функции возникла ошибка, 
# то в файл function_errors.log записываются названия функции и ошибки.

# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения 
# первой же ошибки, а обрабатывала все декорируемые функции и сразу записывала 
# все ошибки в файл.

# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

# Во всех декораторах используется functools.wraps.

import os
import datetime
import functools
from typing import Callable, Any

cur_dir = os.path.dirname(__file__)


def logging(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(func.__name__, func.__doc__)
        func(*args, **kwargs)

    return wrapped_func
    

def ():
    pass

def ():
    pass

