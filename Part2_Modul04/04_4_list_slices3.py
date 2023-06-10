# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В 
# (можно сгенерировать случайно, при этом А < B). 
# Напишите программу, которая удаляет элементы списка с 
# индексами от А до В. Не используйте дополнительные переменные и методы списков.

import random

num_N = int(input('Длина списка: '))

while True:
    num_b = random.randint(0, num_N)
    num_a = random.randint(0, num_N)
    if num_a < num_b:
        break

my_list = [random.randint(0, num_N) for _ in range(num_N)]
slice_list = my_list[:num_a] + my_list[num_b + 1:] 

print('A', num_a)
print('B', num_b)
print('List', my_list)
print('Slice', slice_list)