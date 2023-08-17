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


def properties(cur_path):

    for i_dir in os.listdir(cur_path):
        find_path = os.path.join(cur_path, i_dir)

        if os.path.isfile(find_path):
            file_amt.append(1)
            files_size.append(os.path.getsize(find_path))

        elif os.path.isdir(find_path):
            dir_amt.append(1)
            properties(find_path)
            
    
dir = os.path.dirname(__file__)
files_size = list()
file_amt = list()
dir_amt = list()


properties(dir)
print(dir)
print('Размер каталога (в Кбайтах):', sum(files_size) / 1024)
print('Количество подкаталогов:', sum(dir_amt))
print('Количество файлов:', sum(file_amt))

# примерный код написал почти сразу, но показалось что это как-то просто
# и как обычно начал мудрить )))))
# мудрил часа три - ничего не получалось - все удалил - 
# подправил начальный код и вот так вышло
# но кажется тут можно сделать лучше, не могу додумать