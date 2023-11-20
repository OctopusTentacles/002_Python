# Задача 5. Кэширование для ускорения вычислений
# Контекст
# Вы разрабатываете программу для оптимизации вычислений чисел Фибоначчи. 
# Числа Фибоначчи вычисляются рекурсивной функцией, каждое число равно сумме 
# двух предыдущих чисел. Однако вы заметили, что при больших значениях чисел 
# Фибоначчи вычисления занимают значительное время, так как многие значения 
# вычисляются повторно. Вам поручено создать декоратор, который кэширует результаты 
# вызова функции и позволяет избежать повторных вычислений для одних и тех же аргументов.

# Задача
# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) 
# результаты вызова функции и, при повторном вызове с теми же аргументами, 
# возвращает сохранённый результат.

# Примените его к рекурсивной функции вычисления чисел Фибоначчи. 
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и, 
# если такие аргументы уже использовались, должен вернуть сохранённый результат 
# вместо запуска расчёта.

# Советы
# Для хранения результатов удобно использовать словарь, так как поиск элементов 
# внутри словаря будет иметь сложность, равную в среднем O(1).
# При этом не стоит хранить все вычисления в одном словаре, созданном снаружи 
# функций (в глобальной области видимости). Лучше создавать отдельные словари для 
# каждой декорируемой функции.


import functools
from typing import Callable


def decor_cache(func: Callable) -> Callable:
    """ Декоратор, который кэширует результаты вызова функции и, при повторном 
        вызове с теми же аргументами, возвращает сохранённый результат.
    """
    caching = dict()

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> int:
        cache = {}
        if args in caching.keys():
            return caching[args]
        else:
            result = func(*args, **kwargs)
            if result == args:
                cache[args] = result
                caching[args] = cache
        
        
            return result    
    return wrapper



@decor_cache
def fibonacci(number: int) -> int:
    """ Рекурсивная функция вычисления чисел Фибоначчи. """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)



# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
