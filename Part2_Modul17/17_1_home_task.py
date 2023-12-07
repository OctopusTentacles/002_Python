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

# ==================================================================================
# Реализуйте декоратор singleton, который превращает класс в одноэлементный. 
# При множественной инициализации объекта этого класса будет сохранён только первый 
# инстанс, а все остальные попытки создания будут возвращать первый экземпляр.


def singleton(cls):
    """ Декоратор класса. Превращает класс в синглтон
        (может иметь только один инстанс)
    """
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None #кэш
    return wrapper_singleton



@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)


# Результат:
# 1986890616688
# 1986890616688
# True
