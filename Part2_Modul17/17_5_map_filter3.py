# Задача 3. Функция reduce
# Помимо map и filter, есть ещё одна функция — reduce. 
# Она применяет указанную функцию к элементам последовательности, сводя её к 
# единственному значению. Однако используют reduce довольно редко. Начиная с третьей 
# версии Python, эту функцию даже вынесли из встроенных функций в модуль functools.

# Пример кода с reduce:

# from functools import reduce
# from typing import List

# def my_add(a: int, b: int) -> int:
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result


# numbers: List[int] = [0, 1, 2, 3, 4]
# print(reduce(my_add, numbers))

# Результат:
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10

# Используя функцию reduce, реализуйте код, который считает, 
# сколько раз слово was встречается в списке: 6


from typing import List, Any
from functools import reduce

sentences: List[str] = [
    "Nory was a Catholic", "because her mother was a Catholic", 
    "and Nory’s mother was a Catholic", "because her father was a Catholic", 
    "and her father was a Catholic", "because his mother was a Catholic", "or had been"
    ]

def was(elem_1: Any, elem_2: str) -> int:
    # первый вход elem_1 -> str, дальше он всегда будет None
    # поэтому проверим первый элемент:
    if isinstance(elem_1, str):
        # и посчитаем в нем 'was'.
        elem_1: int = elem_1.count('was')
        # теперь в первом елементе вместо None будет количество 'was'
    elem_1 += elem_2.count('was')
    # print(elem_1, elem_2)
    # возвращаемый элемент будет передаваться на следующем входе в elem_1
    return elem_1


# reduce - через фукцию уменьшает последовательность к единственному значению
#           2 элемента становятся одним, + к одному третий и т.д.
#           если никак не обрабатывать то со второго входа первый элемент всегда None
#           и в конце будет None
print(reduce(was, sentences))
