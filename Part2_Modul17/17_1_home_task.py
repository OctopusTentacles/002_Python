# Реализуйте декоратор для декораторов: он должен декорировать другую функцию, 
# которая должна быть декоратором, и даёт возможность любому декоратору 
# принимать произвольные аргументы.


import functools
from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """ Декоратор. Дает возможность другому декоратору принимать аргументы """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Декоратор. Шаблон"""
    @functools.wraps(func)
    def wrapper(*f_args, **f_kwargs) -> Callable:
        print("Переданные арги и кварги в декоратор:", dec_args, dec_kwargs)
        return func(*f_args, **f_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)


# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
