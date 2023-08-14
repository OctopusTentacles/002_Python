# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, 
# каждое в отдельной строке. Напишите программу, которая выводит 
# их сумму в выходной файл answer.txt.

# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
 
# Содержимое файла answer.txt
# 20

import os

def find_path(cur_path, name):
    for i_elem in os.listdir(cur_path):
        search_path = os.path.join(cur_path, i_elem)
        if i_elem == name:
            return search_path


path = find_path('', 'Part2_Modul09')

print(path)

# numbers_file = open('numbers.txt', 'w')