# Задача 2. Семинар
# На одном семинаре по теории множеств нужно показать наглядный пример, 
# как эти множества работают. Для начала было сгенерировано два набора чисел: 

# Вас попросили написать программу, которая будет наглядно демонстрировать работу 
# со множествами с помощью этих чисел.

# Напишите программу, которая преобразует списки во множества и убирает 
# повторяющиеся элементы. Затем удаляет минимальный элемент из каждого множества 
# и добавляет туда случайное число в диапазоне от 100 до 200. 
# Затем выполните следующие действия со множествами: 

# Вывести все элементы множеств (объединение). 
# Вывести только общие элементы (пересечение).
# Вывести элементы, входящие в nums_2, но не входящие в nums_1.
 
# Пример результата:
# 1-е множество: {1, 2, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 26, 27, 29}
# 2-е множество: {1, 5, 7, 8, 9, 11, 12, 13, 15, 16, 19, 21, 22, 23, 24, 29, 30}

# Минимальный элемент 1-го множества: 1
# Минимальный элемент 2-го множества: 1

# Случайное число для 1-го множества: 126
# Случайное число для 2-го множества: 169

# Объединение множеств: {2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 29, 30, 169, 126}
# Пересечение множеств: {7, 8, 11, 12, 13, 15, 16, 19, 21, 22, 24, 29}
# Элементы, входящие в nums_2, но не входящие в nums_1: {5, 9, 169, 23, 30}


import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 
          11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 
          9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_set1 = set(nums_1)
nums_set2 = set(nums_2)
print('1-е множество:', nums_set1)
print('2-е множество:', nums_set2)

min_set1 = nums_set1.(min(nums_1))

print('Минимальный элемент 1-го множества:', min_set1)
