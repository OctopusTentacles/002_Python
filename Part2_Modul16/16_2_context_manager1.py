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