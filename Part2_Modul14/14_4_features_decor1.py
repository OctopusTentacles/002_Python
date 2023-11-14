# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные 
# ингредиенты вроде салата, помидоров и других. Всё это в свою очередь содержится между 
# двух половинок булочки. Реализуйте такую функцию и два соответствующих декоратора — 
# ингредиенты и хлеб.

# Пример результата работы программы при вызове функции sandwich:

# </----------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

from typing import Callable, Any


def ingredients(func: Callable) -> Any:
    
    def wrapped_func(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")
    return wrapped_func

def bread(func: Callable) -> Any:
    pass


def sandwich(filling):
    print(filling)


sandwich("--ветчина--")