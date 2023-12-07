# Реализуйте декоратор для декораторов: он должен декорировать другую функцию, 
# которая должна быть декоратором, и даёт возможность любому декоратору 
# принимать произвольные аргументы.


import functools
from typing import Callable, Any


def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Декоратор. Шаблон"""
    @functools.wraps(func)
    def wrapper(*f_args, **f_kwargs) -> Callable:
        print("Переданные арги и кварги в декоратор:", dec_args, dec_kwargs)


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)


# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
