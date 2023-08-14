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

def find_dir(cur_path, folder):
    for i_dir in os.listdir(cur_path):
        find_path = os.path.join(cur_path, i_dir)
        if i_dir == folder:
            return find_path
        elif os.path.isdir(find_path):
            result = find_dir(find_path, folder)
            if result:
                return result
        
        



path = os.path.abspath(find_dir('..', 'Part2_Modul09'))
print(path)

# numbers_file = open('numbers.txt', 'w')