# Задача 4. По парам
# Напишите программу, которая инициализирует список из 10 случайных целых чисел, 
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.

# Дополнительно: решите задачу несколькими способами.

# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]


import random

random_list = [random.randint(0, 9) for _ in range(10)]
print('\nОригинальный список:', random_list)

new_list = [(value, random_list[index + 1]) 
            for index, value in enumerate(random_list) if index % 2 == 0]
print('Новый список:', new_list)

# ________________________________________________________________________________
random_list = [random.randint(0, 9) for _ in range(10)]
print('\nОригинальный список:', random_list)

new_list = [random_list[::2], random_list[1::2]]
print('Новый список:', new_list)
