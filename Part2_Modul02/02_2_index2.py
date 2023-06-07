# Задача 2. Кратность
#
# Пользователь вводит список из N чисел и число K. 
# Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K.
#
# Пример:
# Кол-во чисел в списке: 4
# Введите 1 число: 1
# Введите 2 число: 20
# Введите 3 число: 30
# Введите 4 число: 4
#
# Введите делитель: 10
# Индекс числа 20: 1
# Индекс числа 30: 2
# Сумма индексов: 3

num_list = []

N = int(input('Кол-во чисел в списке: '))
for i in range(1, N + 1):
    print('Введите', i, 'число:', end = ' ')
    num = int(input())
    num_list.append(num)

divider = int(input('Введите делитель: '))
index = 0
sum_indexes = 0

for i in num_list:
    if i % divider == 0:
        print(f'Индекс числа {i}: {index}')
        sum_indexes += index
    index += 1

print('Сумма индексов:', sum_indexes)

