# Задача 7. Считалка

# N человек, пронумерованных числами от 1 до N, стоят в кругу. 
# Они начинают играть в считалку на выбывание, где каждый K-й 
# по счёту человек выбывает из круга, после чего счёт 
# продолжается со следующего за ним человека.

# На вход подаётся количество человек N и номер K. 
# Напишите программу, которая выводит число от 1 до N — 
# это номер человека, который останется в кругу последним.

# Пример:
# Кол-во человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек

# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2

# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5

# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1

# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3

# Остался человек под номером 4


def create_list(n):
    for index in range(1, n + 1):
        people_list.append(index)


people_list = []

n_people = int(input('Кол-во человек: '))
k_number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {k_number}-й человек!')

create_list(n_people)
print('\nТекущий круг людей:', people_list)