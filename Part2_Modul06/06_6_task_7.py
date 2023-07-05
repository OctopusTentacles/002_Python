# Задача 7. Три списка

# Даны три списка.
# Нужно выполнить две задачи:

# найти элементы, которые есть в каждом списке;
# найти элементы из первого списка, которых нет во втором и третьем списках.
# Каждую задачу нужно выполнить двумя способами:

# без использования множеств;
# с использованием множеств.

# Пример выполнения на других данных: 
# array_1 = [1, 2, 3, 4] array_2 = [2, 4] array_3 = [2, 3]

# Вывод:
# Задача 1:
# Решение без множеств: 2
# Решение с множествами: 2

# Задача 2:
# Решение без множеств: 1
# Решение с множествами: 1


array_1 = [1, 2, 3, 4] 
array_2 = [2, 4] 
array_3 = [2, 3]

# array_1 = [1, 5, 10, 20, 40, 80, 100] 
# array_2 = [6, 7, 20, 80, 100] 
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1:')
print('Решение без множеств:', )
print('Решение с множествами:', *set(array_1).intersection(array_2, array_3))



print('\nЗадача 2:')
print('Решение без множеств:', )
print('Решение с множествами:', *set(array_1).difference(array_2, array_3))
