# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В 
# (можно сгенерировать случайно, при этом А < B). 
# Напишите программу, которая удаляет элементы списка с 
# индексами от А до В. Не используйте дополнительные переменные и методы списков.

import random

num_N = int(input('Длина списка: '))

num_a = random.randint(0, num_N - 2)
num_b = random.randint(num_a + 1, num_N - 1)

my_list = [random.randint(0, num_N) for _ in range(num_N)]
slice_list = my_list[:num_a] + my_list[num_b + 1:] 

print('A', num_a)
print('B', num_b)
print('List', my_list)
print('Slice', slice_list)