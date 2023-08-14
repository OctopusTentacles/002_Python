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
        

way = find_dir('..', 'Part2_Modul09')

if way:
    path = os.path.abspath(way)
    print(path)

    numbers_sum = 0
    numbers_file = open(os.path.join(path, 'numbers.txt'), 'w', encoding='utf8')
    numbers_file.write(str('1 \n2 \n3 \n4 \n10'))
    numbers_file.close()

    print('Содержимое файла numbers.txt:')
    numbers_file = open(os.path.join(path, 'numbers.txt'), 'r', encoding='utf8')
    for line in numbers_file:
        numbers_sum += int(line)
        print(line, end='')
    numbers_file.close()

else:
    print('NO Directory!!!')

