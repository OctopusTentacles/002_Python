# Задача 2. Директории
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь 
# и временно меняет текущую рабочую директорию на новую. 
# Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок 
# (например, если такого пути не существует). Вне зависимости от результата 
# выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию.

# Результат:
# <тут содержимое папки>

import os
from contextlib import contextmanager

@contextmanager
def in_dir(path):
    cur_dir = os.getcwd()
    
    try:
        os.chdir(path)
        yield
    except FileNotFoundError:
        print(f"Directory {path} not found.")
    finally:
        os.chdir(cur_dir)


with in_dir('C:\\'):
    print(os.listdir())

