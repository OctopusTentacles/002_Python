# Задача 1. Сумма чисел 2
# Что нужно сделать
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены 
# пробелами и концами строк. Напишите программу, которая выводит сумму чисел во 
# выходной файл answer.txt.

# Пример:
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2

# Содержимое файла answer.txt
# 8

import os

def find_dir(cur_puth, file):
    for i_dir in os.listdir(cur_puth):
        find_path = os.path.join(cur_puth, i_dir)
        if i_dir == file:
            return find_path
        elif os.path.isdir(find_path):
            result = find_dir(find_path, file)
            if result:
                return result


way = os.path.abspath(find_dir('..', 'Part2_Modul09'))
# для работы в определенной директории, 
# это не по ТЗ, но мне так удобнее, 
# что бы относящиеся друг к другу файлы были в одном месте

if way:
    numbers_sum = 0

    numbers_file = open(os.path.join(way, 'numbers.txt'), 'w', encoding='utf8')
    numbers_file.write(str('     2 \n2 \n   2 \n         2'))
    numbers_file.close()
    # Обязательно закрывать файл? Вроде работает без закрытия, но я его открываю
    # еще раз для чтения - это правильно? Иначе выходят ошибки:
    # ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    # io.UnsupportedOperation: not readable
    
    numbers_file = open(os.path.join(way, 'numbers.txt'), 'r', encoding='utf8')
    for line in numbers_file:
        numbers_sum += int(line.strip())
    numbers_file.close()


else:
    print('NO such Directory!')


