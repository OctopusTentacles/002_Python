# Задача 1. Однострочный код
# Пользователь вводит неопределённое количество чисел. Напишите код, 
# который запрашивает эти числа и сортирует их по возрастанию. 
# Реализуйте решение в одну строку.

# Пример работы консоли:
# Введите числа: 5 8 4 1 0 3

# [0, 1, 3, 4, 5, 8]

from typing import List


num = input("Введите числа: ")
list_num: List[int] = sorted(list(map(int, num.split(' '))))
print(list_num)


print('='*50)
# =============================================================================
# =============================================================================
print()
nums_1: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
nums_2: List[int] = [2, 7, 1, 8, 2, 8, 1, 8]

result: List[int] = list(map(lambda x, y: x + y, nums_1, nums_2))
print(result)

result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_even)
# =============================================================================
animals = ['cat', 'dog', 'cow'] # ['Cat', 'Dog', 'Cow']
# with map:
new_animals = list(map(lambda elem: elem.capitalize(), animals))
# with list comprehension:
new_animals = [elem.capitalize() for elem in animals]
# =============================================================================

result = map(lambda num: num * 3, filter(lambda num: num % 2, nums_1))
print(list(result))