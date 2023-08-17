# Задача 3. Файлы и папки
# Что нужно сделать
# Напишите программу, которая получает на вход путь до каталога 
# (в том числе это может быть просто корень диска) и выводит общее 
# количество файлов и подкаталогов в нём. Также выведите на экран размер 
# каталога в килобайтах (1 килобайт = 1024 байт).

# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму 
# размеров всех вложенных в него файлов. 

# Результат работы программы на примере python_basic\Module14:

# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15

import os


def dir_size(cur_path):
    files_size = list()
    file_amt = 0
    dir_amt = 0

    for i_dir in os.listdir(cur_path):
        find_path = os.path.join(cur_path, i_dir)
        if os.path.isfile(find_path):
            file_amt += 1
            files_size.append(os.path.getsize(find_path))

        elif os.path.isdir(find_path):
            dir_amt += 1
            result = dir_size(find_path)
            if result:
                return result
    
    
    print('Размер каталога (в Кбайтах):', files_size)
    print('Размер каталога (в Кбайтах):', sum(files_size) / 1024)

    print('Количество подкаталогов:', dir_amt)
    print('Количество файлов:', file_amt)



dir = os.path.dirname(__file__)
dir_size(dir)



