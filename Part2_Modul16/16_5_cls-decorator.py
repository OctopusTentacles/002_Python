# Декоратор как класс
# Декоратор вывода количества использования функции
# Написание класса-декоратора CountCalls
# Создание декоратора с помощью метода call

from typing import Any, Callable
import functools

class CountCalls:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args: Any, **kwds: Any) -> Callable:
        # x() = x.__call__
        self.num_calls += 1
        print("Вызов номер {num} функции {func}".format(
            num=self.num_calls, func=self.func.__name__
        ))
        return self.func(*args, **kwds)

@CountCalls
def say_hello():
    print("Hello!")


say_hello()
say_hello()
say_hello()

print(say_hello.num_calls)