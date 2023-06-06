# Задача 8. Симметричная последовательность

# Последовательность чисел называется симметричной, если она одинаково 
# читается как слева направо, так и справа налево. 
# Например, следующие последовательности являются симметричными:
# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1
# Пользователь вводит последовательность из N чисел. 
# Напишите программу, которая определяет, какое минимальное количество 
# и каких чисел надо приписать в конец этой последовательности, 
# чтобы она стала симметричной.

# Пример 1:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2

# Последовательность: [1, 2, 1, 2, 2]
# Нужно приписать чисел: 3
# Сами числа: [1, 2, 1]

# Пример 2:
# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 3
# Число: 4
# Число: 5

# Последовательность: [1, 2, 3, 4, 5]
# Нужно приписать чисел: 4
# Сами числа: [4, 3, 2, 1]


def revers(rev_list):
    invert_list = []
    for i in range(len(rev_list - 1), - 1, - 1):
        invert_list.append(rev_list, i)
    if invert_list == rev_list:
        return True
    else:
        return False
    

num_list = []
prepare_list = []
revers_list = []

n_num = int(input('Кол-во чисел: '))
for _ in range(n_num):
    print('Число: ', end='')
    number = int(input())
    num_list.append(number)

print('Последовательность:', num_list)

for i_num in range(len(num_list)):
    for i in range(i_num, len(num_list)):
        prepare_list.append(num_list[i])
    if revers(prepare_list):
        for i_rev in range(i_num):
            revers_list.append(num_list[i_rev])
