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


group_1 = open('/Users/artem/Documents/task/group_1.txt', 'r', encoding='UTF-8')
group_2 = open('/Users/artem/Documents/task/Additional_info/group_2.txt', 'r', encoding='UTF-8')

summa = 0
diff = 0
compos = 1

for i_line in group_1:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])
        

for i_line in group_2:
    info = i_line.split()
    if info:
        compos *= int(info[2])

group_1.close()
group_2.close()

print(summa)
print(diff)
print(compos)
