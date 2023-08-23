# Задача 2. Возраст
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.

# Напишите программу, которая считывает файл, даёт имя для каждого возраста 
# (можно просто использовать буквы алфавита) и выводит результат 
# в новый файл result.txt в формате «имя — возраст». 
# Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:

# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

import os

current_directory = os.path.dirname(__file__)

try:
    with open(os.path.join(current_directory, 'ages.txt'), 'x', encoding='utf8') as new_file:
    # режим 'x' - это эксклюзивное создание, 
    # бросается исключение FileExistsError, если файл уже существует.
        for i_line in new_file.readlines():
            print(new_file)
except FileExistsError as exc:
    print('попытка создания файла или директории, которая уже существует', type(exc))

try:
    with open(current_directory, 'r', encoding='utf8') as new_file:
    # режим 'x' - это эксклюзивное создание, 
    # бросается исключение FileExistsError, если файл уже существует.
        for i_line in new_file.readlines():
            print(new_file)
except PermissionError  as exc:
    print('Поймано исключение: ', exc, type(exc))

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

with open(os.path.join(current_directory, 'ages.txt'), 'r', encoding='utf8') as ages_file:
    for i_line in ages_file.readlines():
        ages_file = i_line

try:
    with open(os.path.join(current_directory, 'result.txt'), 'w', encoding='utf8') as result_file:
        result_file.write(names + str(ages_file))
except TypeError as exc:
    print("Поймано исключение: ", exc, type(exc))