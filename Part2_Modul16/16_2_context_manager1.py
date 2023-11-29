# Задача 1. Таймер
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера: 
# функция должна работать с оператором with и замерять время работы 
# вложенного кода.


from contextlib import contextmanager
from collections.abc import Iterator

@contextmanager
def next_num(num: int) -> Iterator[int]:
    print("Входим в функцию")
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print("Обнаружена ошибка:", exc)
    finally:
        print("Код выполняется")
    print("Выход из функции")


with next_num(-1) as next:
    print("Следующее число = {}".format(next))
    print(10 / next)

# =============================================================================

import time
from contextlib import contextmanager
from collections.abc import Iterator


# class Timer:
#     def __init__(self) -> None:
#         print("Время работы кода")
#         self.start = None

#     def __enter__(self) -> 'Timer':
#         self.start = time.time()
#         return self
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print(time.time() - self.start)
#         return True
    
@contextmanager
def timer() -> Iterator:
    start = time.time()
    try: 
        yield
    except Exception as exc:
        print(exc)
    finally: 
        print(time.time() - start)

with timer() as t1:
    print("Первая часть")
    val_1 = 100 * 100 ** 1000000
    val_1 += "abc"

with timer() as t2:
    print("Вторая часть")
    val_2 = 200 * 200 ** 1000000

with timer() as t3:
    print("Третья часть")
    val_3 = 300 * 300 ** 1000000

# =============================================================================

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(end - start)