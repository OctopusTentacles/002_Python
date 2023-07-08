# Задача 1. Создание кортежей

# Заполните один кортеж десятью случайными целыми числами от 0 до 5 
# включительно. Также заполните второй кортеж числами от −5 до 0. 
# Объедините два кортежа, создав тем самым третий кортеж. 
# С помощью метода кортежа определите в нём количество нулей. 
# Выведите на экран третий кортеж и количество нулей в нём.

import random

# a = [random.randint(0, 5) for _ in range(0, 5)]
tuple_1 = tuple(random.randint(0, 5) for _ in range(5))
tuple_2 = tuple(random.randint(-5, 0) for _ in range(5))
tuple_3 = tuple_1 + tuple_2


print(type(tuple_1), tuple_1)
print(type(tuple_2), tuple_2)
print(type(tuple_3), tuple_3)
print('количество нулей', tuple_3.count(0))
