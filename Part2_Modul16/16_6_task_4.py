# Задача 4. Весь мир — декоратор…
# Реализуйте декоратор для декораторов: он должен декорировать другую функцию, 
# которая должна быть декоратором, и даёт возможность любому декоратору 
# принимать произвольные аргументы.

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101


import functools
from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """ Декоратор для передачи аргументов.
        :param decorator: декоратор, которому надо передать аргументы.
    """
    def any_decorator(*args, **kwargs) -> Callable:
        """ Декоратор - получает предварительные аргументы.
        """
        @functools.wraps(decorator)
        def wrapper(func: Callable) -> Any:

            return decorator(func, *args, **kwargs)
        return wrapper
    return any_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*f_args, **f_kwargs) -> Any:

        print("Переданные арги и кварги в декоратор:", args, kwargs)

        return func(*f_args, **f_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)