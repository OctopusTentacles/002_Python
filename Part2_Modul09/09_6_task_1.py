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
# ____________________________________________________________________________

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


way = find_dir('..', 'Part2_Modul09')
# для работы в определенной директории, 
# это не по ТЗ, но мне так удобнее, 
# что бы сопутствующие файлы были в одном месте

if way:
    path = os.path.abspath(way)
    numbers_sum = 0

    numbers_file = open(os.path.join(path, 'numbers.txt'), 'w', encoding='utf8')
    numbers_file.write(str('     2 \n2 \n   2 \n         2'))
    numbers_file.close()
    # Обязательно закрывать файл? Вроде работает без закрытия, но я его открываю
    # еще раз для чтения - это правильно? Иначе выходят ошибки:
    # ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    # io.UnsupportedOperation: not readable
    
    numbers_file = open(os.path.join(path, 'numbers.txt'), 'r', encoding='utf8')
    for line in numbers_file:
        numbers_sum += int(line.strip())
    numbers_file.close()

    answer_file = open(os.path.join(path, 'answer.txt'), 'w', encoding='utf8')
    answer_file.write(str(numbers_sum))
    answer_file.close()


else:
    print('NO such Directory!')

# ____________________________________________________________________________________

def find_dir(cur_puth, file):
    for i_dir in os.listdir(cur_puth):
        find_path = os.path.join(cur_puth, i_dir)
        if i_dir == file:
            return find_path
        elif os.path.isdir(find_path):
            result = find_dir(find_path, file)
            if result:
                return result


def write_file(path_file, name_file, content):
    redact_file = open(os.path.join(path_file, name_file), 'w', encoding='utf8')
    redact_file.write(str(content))
    redact_file.close()
    return redact_file


def read_file_sum(path_file, name_file):
    content_sum = 0
    redact_file = open(os.path.join(path_file, name_file), 'r', encoding='utf8')
    for i_line in redact_file:
        content_sum += int(i_line.strip())
    redact_file.close()
    return content_sum



way = find_dir('..', 'Part2_Modul09')

if way:
    path = os.path.abspath(way)
    
    numbers_file = write_file(path, 
                              'numbers.txt', 
                              '     2 \n2 \n   2 \n         2')
    
    numbers_sum = read_file_sum(path, 'numbers.txt',)

    answer_file = write_file(path, 
                              'answer.txt', 
                              numbers_sum)


else:
    print('NO such Directory!')

# Добавил функции, не знаю как лучше, но оба варианта работают
