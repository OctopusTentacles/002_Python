# Задача 4. Весь мир — декоратор…
# Реализуйте декоратор для декораторов: он должен декорировать другую функцию, 
# которая должна быть декоратором, и даёт возможность любому декоратору 
# принимать произвольные аргументы.

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101


import functools
from typing import Callable, Optional


def decorator_with_args_for_any_decorator(decorator: Callable):
    """
    """
    def decorator_maker(*args, **kwargs):
        """
        """
        @functools.wraps(decorator)
        def wrapper(func):

        # print("Переданные арги и кварги в декоратор:", args, kwargs)

            return decorator(func, *args, **kwargs)
        return wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*args1, **kwargs1):

        print("Переданные арги и кварги в декоратор:", args, kwargs)

        return func(*args1, **kwargs1)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)