# Задача 1. Результаты
# Одному программисту дали задачу для обработки неких результатов тестирования 
# двух групп людей. Файл первой группы (group_1.txt) находится в 
# папке task, файл второй группы (group_2.txt) — в папке Additional_info.

# Содержимое файла group_1.txt
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 30
 
# Содержимое файла group_2.txt
# Павленко Геннадий 20
# Щербаков Владимир 35
# Marley Bob 15

# На экран нужно было вывести сумму очков первой группы, 
# затем разность очков опять же первой группы и напоследок — 
# произведение очков уже второй группы. 

# Программист оказался не очень опытным, писал код наобум и даже не стал 
# его проверять. И оказалось, этот код просто не работает. Вот что он написал:

# Исправьте код для решения поставленной задачи. 
# Для проверки результата создайте необходимые папки 
# (task, Additional_info, Dont touch me) на своём диске в 
# соответствии с картинкой и также добавьте файлы group_1.txt и group_2.txt.

import os

print(os.path.abspath('..'))
file = open('/Users/artem/Documents/task/group_1.txt', 'r', encoding='UTF-8')

for i_line in file:
    print(i_line)


# file = open('E:\task\group_1.txt', 'read')

# diff = 0

# for i_line in file:
#     info = i_line.split()
#     diff -= info[2]

# file_2 = open('E:\task\group_2.txt', 'read')

# compose = 0

# for i_line in file:
#     info = i_line.split()
#     compose *= info[2]

# print(summa)
# print(diff)
# print(compose)

